#!/usr/bin/env python3
"""Query, validate, and optionally generate Wildberries API references from Swagger."""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required. Install with: python3 -m pip install -r requirements.txt") from exc


ROOT = Path(__file__).resolve().parents[1]
SWAGGER_DIR = ROOT / "swagger"
GENERATED_DIR = ROOT / "generated"
METHODS = {"get", "post", "put", "patch", "delete", "options", "head", "trace"}
SUPPORTED_LANGS = ("ru", "en")
LANG_DIRS = {"ru": SWAGGER_DIR, "en": SWAGGER_DIR / "en"}
LANG_LABELS = {"ru": "Russian", "en": "English"}


def swagger_source(lang: str) -> str:
    return "swagger/*.yaml" if lang == "ru" else f"swagger/{lang}/*.yaml"


def generated_note(lang: str) -> str:
    if lang == "ru":
        source = "`swagger/*.yaml`"
    else:
        source = "`swagger/*.yaml` with text from `swagger/en/*.yaml`"
    return f"Generated from {source} by `scripts/wb_api.py generate`. Do not edit by hand; Russian Swagger is the canonical source of truth."


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse as a YAML mapping")
    return data


def load_specs(lang: str = "ru") -> list[dict[str, Any]]:
    if lang not in LANG_DIRS:
        raise ValueError(f"Unsupported language: {lang}")
    specs: list[dict[str, Any]] = []
    for path in sorted(LANG_DIRS[lang].glob("*.yaml")):
        spec = load_yaml(path)
        spec["_path"] = path
        spec["_lang"] = lang
        specs.append(spec)
    return specs


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def title(spec: dict[str, Any]) -> str:
    return str(spec.get("info", {}).get("title") or spec["_path"].stem)


def file_slug(spec: dict[str, Any]) -> str:
    info = spec.get("info", {})
    return str(info.get("x-file-name") or spec["_path"].stem.split("-", 1)[-1])


def pointer_parts(ref: str) -> list[str]:
    return [part.replace("~1", "/").replace("~0", "~") for part in ref[2:].split("/")]


def resolve_pointer(spec: dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        return None
    node: Any = spec
    for part in pointer_parts(ref):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def resolve_ref(spec: dict[str, Any], value: Any) -> Any:
    if isinstance(value, dict) and "$ref" in value:
        resolved = resolve_pointer(spec, str(value["$ref"]))
        return resolved if resolved is not None else value
    return value


def ref_name(ref: str) -> str:
    return ref.rsplit("/", 1)[-1]


def server_urls(spec: dict[str, Any], path_item: dict[str, Any], op: dict[str, Any]) -> list[str]:
    servers = op.get("servers") or path_item.get("servers") or spec.get("servers") or []
    return [str(server["url"]) for server in servers if isinstance(server, dict) and server.get("url")]


def security_names(spec: dict[str, Any], op: dict[str, Any]) -> list[str]:
    security = op.get("security", spec.get("security", []))
    names: list[str] = []
    for item in security or []:
        if isinstance(item, dict):
            names.extend(str(key) for key in item)
    return names


def iter_operations(specs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for spec in specs:
        paths = spec.get("paths") or {}
        if not isinstance(paths, dict):
            continue
        for api_path, path_item in paths.items():
            if not isinstance(path_item, dict):
                continue
            inherited_parameters = path_item.get("parameters") or []
            for method, op in path_item.items():
                if method not in METHODS or not isinstance(op, dict):
                    continue
                tags = [str(tag) for tag in op.get("tags", [])]
                records.append(
                    {
                        "file": spec["_path"],
                        "file_rel": rel(spec["_path"]),
                        "lang": str(spec.get("_lang") or "ru"),
                        "slug": file_slug(spec),
                        "title": title(spec),
                        "method": method.upper(),
                        "path": str(api_path),
                        "summary": str(op.get("summary") or ""),
                        "description": str(op.get("description") or ""),
                        "operation_id": str(op.get("operationId") or ""),
                        "tags": tags,
                        "tag": tags[0] if tags else "",
                        "category": str(op.get("x-category") or ""),
                        "token_types": [str(token) for token in op.get("x-token-types", [])],
                        "readonly": bool(op.get("x-readonly-method", False)),
                        "servers": server_urls(spec, path_item, op),
                        "security": security_names(spec, op),
                        "parameters": inherited_parameters + (op.get("parameters") or []),
                        "request_body": op.get("requestBody"),
                        "responses": op.get("responses") or {},
                        "op": op,
                        "spec": spec,
                    }
                )
    return records


def operation_key(record: dict[str, Any]) -> tuple[str, str]:
    return (record["method"], record["path"])


def file_operation_key(record: dict[str, Any]) -> tuple[str, str, str]:
    return (Path(record["file"]).name, record["method"], record["path"])


def records_for_lang(lang: str) -> list[dict[str, Any]]:
    return iter_operations(load_specs(lang))


def records_with_search_overlays(lang: str) -> list[dict[str, Any]]:
    records = records_for_lang(lang)
    overlay_maps: list[dict[tuple[str, str], dict[str, Any]]] = []
    for overlay_lang in SUPPORTED_LANGS:
        if overlay_lang == lang or not LANG_DIRS[overlay_lang].exists():
            continue
        overlay_records = records_for_lang(overlay_lang)
        if overlay_records:
            overlay_maps.append({operation_key(record): record for record in overlay_records})
    for record in records:
        record["search_overlays"] = [
            overlay[operation_key(record)] for overlay in overlay_maps if operation_key(record) in overlay
        ]
    return records


def canonical_records_with_overlays() -> list[dict[str, Any]]:
    return records_with_search_overlays("ru")


def overlay_for_lang(record: dict[str, Any], lang: str) -> dict[str, Any] | None:
    if record.get("lang") == lang:
        return record
    for overlay in record.get("search_overlays", []):
        if overlay.get("lang") == lang:
            return overlay
    return None


def localized(record: dict[str, Any], key: str, lang: str) -> Any:
    overlay = overlay_for_lang(record, lang)
    if overlay and overlay.get(key):
        return overlay[key]
    return record.get(key)


def compact(value: Any, limit: int = 180) -> str:
    text = strip_markup(value)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "..."


def strip_markup(value: Any) -> str:
    text = str(value or "")
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_text(value: Any) -> str:
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", str(value or ""))
    text = strip_markup(text).casefold()
    text = re.sub(r"[_/.\-]+", " ", text)
    return re.sub(r"[^\w]+", " ", text, flags=re.UNICODE).strip()


def tokens(value: Any) -> list[str]:
    return [token for token in normalize_text(value).split() if token]


def search_fields(record: dict[str, Any]) -> list[str]:
    fields = [
        record["method"],
        record["path"],
        record["summary"],
        record["description"],
        record["operation_id"],
        record["tag"],
        " ".join(record["tags"]),
        record["title"],
        record["category"],
        " ".join(record["servers"]),
        record["file_rel"],
    ]
    for overlay in record.get("search_overlays", []):
        fields.extend(
            [
                overlay["summary"],
                overlay["description"],
                overlay["operation_id"],
                overlay["tag"],
                " ".join(overlay["tags"]),
                overlay["title"],
                overlay["category"],
                overlay["file_rel"],
            ]
        )
    return fields


def score_record(record: dict[str, Any], query: str) -> int:
    query_tokens = tokens(query)
    if not query_tokens:
        return 1
    normalized_fields = [normalize_text(field) for field in search_fields(record)]
    haystack = " ".join(normalized_fields)
    if not all(token in haystack for token in query_tokens):
        return 0

    phrase = normalize_text(query)
    score = 1
    weights = [
        ("path", 16),
        ("operation_id", 14),
        ("summary", 12),
        ("tag", 8),
        ("title", 5),
        ("category", 5),
        ("servers", 4),
        ("file_rel", 3),
        ("description", 1),
    ]
    for key, weight in weights:
        field = normalize_text(record.get(key, ""))
        if phrase and phrase in field:
            score += weight * 3
        for token in query_tokens:
            if token in field:
                score += weight
    if str(query).casefold() in record["path"].casefold():
        score += 40
    if record["path"].casefold().endswith(str(query).casefold()):
        score += 20
    return score


def ranked_records(records: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    scored = [(score_record(record, query), record) for record in records]
    return [
        record
        for score, record in sorted(scored, key=lambda item: (-item[0], item[1]["file_rel"], item[1]["path"]))
        if score > 0
    ]


def tag_matches(record: dict[str, Any], needle: str) -> bool:
    haystacks = [record["tag"], " ".join(record["tags"])]
    for overlay in record.get("search_overlays", []):
        haystacks.extend([overlay["tag"], " ".join(overlay["tags"])])
    return any(needle == normalize_text(value) or needle in normalize_text(value) for value in haystacks)


def md_cell(value: Any) -> str:
    text = ", ".join(str(item) for item in value) if isinstance(value, list) else str(value or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text.replace("|", r"\|")


def endpoint_table(records: list[dict[str, Any]], include_file: bool = False, lang: str = "ru") -> list[str]:
    if include_file:
        lines = ["| File | Tag | Method | Path | Hosts | Summary | Operation ID |", "|---|---|---|---|---|---|---|"]
    else:
        lines = ["| Tag | Method | Path | Hosts | Category | Summary | Operation ID |", "|---|---|---|---|---|---|---|"]
    for record in records:
        hosts = [url.replace("https://", "") for url in record["servers"]]
        row = [
            md_cell(localized(record, "tag", lang)),
            f"`{record['method']}`",
            f"`{md_cell(record['path'])}`",
            md_cell(hosts),
        ]
        if include_file:
            row.insert(0, md_cell(record["file_rel"]))
        else:
            row.append(md_cell(record["category"]))
        row.extend([md_cell(localized(record, "summary", lang)), f"`{md_cell(record['operation_id'])}`" if record["operation_id"] else ""])
        lines.append("| " + " | ".join(row) + " |")
    return lines


def schema_summary(spec: dict[str, Any], schema: Any, seen: set[str] | None = None) -> str:
    if seen is None:
        seen = set()
    if not isinstance(schema, dict):
        return ""
    if "$ref" in schema:
        ref = str(schema["$ref"])
        if ref in seen:
            return ref_name(ref)
        resolved = resolve_pointer(spec, ref)
        if not isinstance(resolved, dict):
            return "$ref " + ref_name(ref)
        summary = schema_summary(spec, resolved, seen | {ref})
        return ref_name(ref) if not summary else f"{ref_name(ref)} ({summary})"
    for key in ("allOf", "oneOf", "anyOf"):
        if key in schema:
            return f"{key}({len(schema.get(key) or [])})"
    typ = schema.get("type")
    if typ == "array":
        return "array[" + schema_summary(spec, schema.get("items"), seen) + "]"
    pieces = [str(typ)] if typ else []
    if schema.get("format"):
        pieces.append(str(schema["format"]))
    if schema.get("enum"):
        pieces.append("enum=" + ",".join(str(item) for item in schema["enum"][:8]))
    if schema.get("required"):
        pieces.append("required=" + ",".join(str(item) for item in schema["required"][:8]))
    return " ".join(pieces) or "object"


def overlay_parameter_descriptions(record: dict[str, Any], lang: str) -> dict[tuple[str, str], str]:
    overlay = overlay_for_lang(record, lang)
    if not overlay or overlay is record:
        return {}
    descriptions: dict[tuple[str, str], str] = {}
    for raw_param in overlay["parameters"]:
        param = resolve_ref(overlay["spec"], raw_param)
        if isinstance(param, dict):
            descriptions[(str(param.get("name", "")), str(param.get("in", "")))] = compact(param.get("description"), 140)
    return descriptions


def parameter_lines(record: dict[str, Any], lang: str = "ru") -> list[str]:
    spec = record["spec"]
    lines: list[str] = []
    localized_descriptions = overlay_parameter_descriptions(record, lang)
    for raw_param in record["parameters"]:
        param = resolve_ref(spec, raw_param)
        if not isinstance(param, dict):
            continue
        schema = resolve_ref(spec, param.get("schema"))
        bits = [
            f"`{param.get('name', '')}`",
            f"in={param.get('in', '')}",
            "required=" + str(bool(param.get("required", False))).lower(),
        ]
        summary = schema_summary(spec, schema)
        if summary:
            bits.append(f"schema={summary}")
        desc = localized_descriptions.get((str(param.get("name", "")), str(param.get("in", "")))) or compact(param.get("description"), 140)
        if desc:
            bits.append(f"- {desc}")
        lines.append("- " + " ".join(bits))
    return lines


def request_body_media(record: dict[str, Any]) -> list[tuple[str, Any]]:
    spec = record["spec"]
    body = resolve_ref(spec, record.get("request_body"))
    if not isinstance(body, dict):
        return []
    content = body.get("content") or {}
    if not isinstance(content, dict):
        return []
    result: list[tuple[str, Any]] = []
    for media_type, media in content.items():
        if isinstance(media, dict) and media.get("schema"):
            result.append((str(media_type), media["schema"]))
    return result


def overlay_request_body_description(record: dict[str, Any], lang: str) -> str:
    overlay = overlay_for_lang(record, lang)
    if not overlay or overlay is record:
        return ""
    body = resolve_ref(overlay["spec"], overlay.get("request_body"))
    return compact(body.get("description"), 200) if isinstance(body, dict) else ""


def request_body_lines(record: dict[str, Any], lang: str = "ru") -> list[str]:
    spec = record["spec"]
    body = resolve_ref(spec, record.get("request_body"))
    if not isinstance(body, dict):
        return []
    lines = [f"- required={str(bool(body.get('required', False))).lower()}"]
    for media_type, schema in request_body_media(record):
        lines.append(f"- `{media_type}` schema={schema_summary(spec, schema)}")
    desc = overlay_request_body_description(record, lang) or compact(body.get("description"), 200)
    if desc:
        lines.append(f"- {desc}")
    return lines


def response_items(record: dict[str, Any]) -> list[tuple[str, str, Any, str]]:
    spec = record["spec"]
    items: list[tuple[str, str, Any, str]] = []
    responses = record.get("responses") or {}
    if not isinstance(responses, dict):
        return items
    for code, raw_response in responses.items():
        response = resolve_ref(spec, raw_response)
        if not isinstance(response, dict):
            continue
        desc = compact(response.get("description"), 120)
        content = response.get("content") or {}
        if not isinstance(content, dict) or not content:
            items.append((str(code), "", None, desc))
            continue
        for media_type, media in content.items():
            schema = media.get("schema") if isinstance(media, dict) else None
            items.append((str(code), str(media_type), schema, desc))
    return items


def overlay_response_descriptions(record: dict[str, Any], lang: str) -> dict[tuple[str, str], str]:
    overlay = overlay_for_lang(record, lang)
    if not overlay or overlay is record:
        return {}
    return {(code, media_type): desc for code, media_type, _, desc in response_items(overlay) if desc}


def response_lines(record: dict[str, Any], lang: str = "ru") -> list[str]:
    spec = record["spec"]
    lines: list[str] = []
    grouped: dict[str, list[str]] = defaultdict(list)
    desc_by_code: dict[str, str] = {}
    localized_descriptions = overlay_response_descriptions(record, lang)
    for code, media_type, schema, desc in response_items(record):
        desc_by_code[code] = localized_descriptions.get((code, media_type)) or localized_descriptions.get((code, "")) or desc
        if media_type:
            summary = schema_summary(spec, schema)
            grouped[code].append(f"{media_type}:{summary}" if summary else media_type)
    for code in sorted(desc_by_code, key=lambda item: (not item.isdigit(), item)):
        suffix = f" ({'; '.join(grouped[code])})" if grouped[code] else ""
        lines.append(f"- `{code}` {desc_by_code[code]}{suffix}".rstrip())
    return lines


def schema_type(spec: dict[str, Any], original: Any, resolved: Any) -> str:
    if isinstance(original, dict) and "$ref" in original:
        return ref_name(str(original["$ref"]))
    if not isinstance(resolved, dict):
        return "unknown"
    if resolved.get("type") == "array" or "items" in resolved:
        return "array[" + schema_summary(spec, resolved.get("items")) + "]"
    if resolved.get("type"):
        typ = str(resolved["type"])
        return f"{typ}:{resolved['format']}" if resolved.get("format") else typ
    for key in ("allOf", "oneOf", "anyOf"):
        if key in resolved:
            return key
    return "object"


def schema_lines(
    spec: dict[str, Any],
    schema: Any,
    *,
    max_depth: int,
    depth: int = 0,
    name: str | None = None,
    required: bool = False,
    seen: set[str] | None = None,
) -> list[str]:
    if seen is None:
        seen = set()
    if not isinstance(schema, dict):
        return []
    ref = str(schema["$ref"]) if "$ref" in schema else ""
    resolved = resolve_ref(spec, schema)
    if not isinstance(resolved, dict):
        return []
    indent = "  " * depth
    details = [schema_type(spec, schema, resolved), "required" if required else "", compact(resolved.get("description"), 160)]
    enum = resolved.get("enum")
    if enum:
        details.append("enum=" + ", ".join(str(item) for item in enum[:12]))
    details = [detail for detail in details if detail]

    lines: list[str] = []
    if name is not None:
        suffix = f" ({'; '.join(details)})" if details else ""
        recursive = " (recursive)" if ref and ref in seen else ""
        lines.append(f"{indent}- {name}{suffix}{recursive}")
    if ref:
        if ref in seen:
            return lines
        seen = seen | {ref}
    if depth >= max_depth:
        return lines

    for key in ("allOf", "oneOf", "anyOf"):
        variants = resolved.get(key)
        if isinstance(variants, list):
            if name is None:
                lines.append(f"{indent}- {key}")
            for index, variant in enumerate(variants, start=1):
                lines.extend(
                    schema_lines(
                        spec,
                        variant,
                        max_depth=max_depth,
                        depth=depth + 1,
                        name=f"{key}[{index}]",
                        seen=seen,
                    )
                )
            return lines

    if resolved.get("type") == "array" or "items" in resolved:
        items = resolved.get("items")
        if isinstance(items, dict):
            lines.extend(
                schema_lines(
                    spec,
                    items,
                    max_depth=max_depth,
                    depth=depth + 1,
                    name="items",
                    seen=seen,
                )
            )
        return lines

    properties = resolved.get("properties")
    if isinstance(properties, dict):
        required_names = set(resolved.get("required") or [])
        for prop_name, prop_schema in properties.items():
            lines.extend(
                schema_lines(
                    spec,
                    prop_schema,
                    max_depth=max_depth,
                    depth=depth if name is None else depth + 1,
                    name=str(prop_name),
                    required=prop_name in required_names,
                    seen=seen,
                )
            )
    additional = resolved.get("additionalProperties")
    if isinstance(additional, dict):
        lines.extend(
            schema_lines(
                spec,
                additional,
                max_depth=max_depth,
                depth=depth if name is None else depth + 1,
                name="additionalProperties",
                seen=seen,
            )
        )
    return lines


def generate_endpoint_index(specs: list[dict[str, Any]], records: list[dict[str, Any]], lang: str) -> str:
    lines = [
        "# Wildberries API - Generated Endpoint Index",
        "",
        generated_note(lang),
        "",
        f"Endpoint count: **{len(records)}** across **{len(specs)}** Swagger files.",
        "",
        "Use `python3 scripts/wb_api.py search <query>` or `python3 scripts/wb_api.py detail <METHOD> <PATH>` for compact Swagger-derived output.",
        "",
    ]
    by_file: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_file[record["file"]].append(record)
    for spec in specs:
        file_records = by_file.get(spec["_path"], [])
        display_title = localized(file_records[0], "title", lang) if file_records else title(spec)
        lines.extend([f"## {display_title} ({rel(spec['_path'])})", ""])
        lines.extend(endpoint_table(file_records, lang=lang))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate_reference(spec: dict[str, Any], records: list[dict[str, Any]], lang: str) -> str:
    hosts = sorted({host.replace("https://", "") for record in records for host in record["servers"]})
    categories = sorted({record["category"] for record in records if record["category"]})
    tags = sorted({record["tag"] for record in records if record["tag"]})
    display_title = localized(records[0], "title", lang) if records else title(spec)
    lines = [
        f"# {display_title}",
        "",
        generated_note(lang),
        "",
        f"Source: `{rel(spec['_path'])}`.",
        "",
        f"Endpoint count: **{len(records)}**. Tags: **{len(tags)}**.",
        "",
        f"Hosts: {', '.join(f'`{host}`' for host in hosts) if hosts else 'none declared'}.",
        "",
        f"`x-category` values: {', '.join(f'`{cat}`' for cat in categories) if categories else 'none declared'}.",
        "",
    ]
    by_tag: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_tag[localized(record, "tag", lang) or "Untagged"].append(record)
    for tag_name in sorted(by_tag):
        lines.extend([f"## {tag_name}", ""])
        lines.extend(endpoint_table(by_tag[tag_name], lang=lang))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate_protocol(records: list[dict[str, Any]], specs: list[dict[str, Any]], lang: str) -> str:
    scheme_rows: list[str] = []
    seen_schemes: set[tuple[str, str, str, str, str]] = set()
    for spec in specs:
        schemes = (spec.get("components") or {}).get("securitySchemes") or {}
        if not isinstance(schemes, dict):
            continue
        for name, scheme in schemes.items():
            if not isinstance(scheme, dict):
                continue
            row = (
                str(name),
                str(scheme.get("type", "")),
                str(scheme.get("name", "")),
                str(scheme.get("in", "")),
                rel(spec["_path"]),
            )
            if row not in seen_schemes:
                seen_schemes.add(row)
                scheme_rows.append("| " + " | ".join(md_cell(item) for item in row) + " |")

    hosts: dict[str, dict[str, set[str]]] = defaultdict(lambda: {"categories": set(), "files": set()})
    token_types: Counter[str] = Counter()
    status_codes: dict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        for host in record["servers"]:
            host_key = host.replace("https://", "")
            if record["category"]:
                hosts[host_key]["categories"].add(record["category"])
            hosts[host_key]["files"].add(record["file_rel"])
        for token in record["token_types"]:
            token_types[token] += 1
        for code, _, _, desc in response_items(record):
            status_codes[str(code)][desc] += 1

    lines = [
        "# Wildberries API - Protocol Summary",
        "",
        "Derived live from `swagger/*.yaml`; Russian Swagger is the canonical source of truth.",
        "",
        "## Security Schemes",
        "",
        "| Name | Type | Header/query name | Location | Source |",
        "|---|---|---|---|---|",
        *scheme_rows,
        "",
        "## Hosts Observed In Swagger",
        "",
        "| Host | x-category values | Source files |",
        "|---|---|---|",
    ]
    for host, data in sorted(hosts.items()):
        lines.append("| " + " | ".join([md_cell(host), md_cell(sorted(data["categories"])), md_cell(sorted(data["files"]))]) + " |")
    lines.extend(["", "## Token Type Hints", ""])
    if token_types:
        lines.extend(["Some operations declare `x-token-types`:", "", "| Token type | Operation count |", "|---|---|"])
        for token, count in sorted(token_types.items()):
            lines.append(f"| `{md_cell(token)}` | {count} |")
    else:
        lines.append("No operations declare `x-token-types`.")

    ping_records = [record for record in records if record["path"] == "/ping"]
    lines.extend(["", "## Ping Operations", ""])
    lines.extend(endpoint_table(ping_records, include_file=True, lang=lang) if ping_records else ["No `/ping` operation is declared."])

    lines.extend(["", "## Response Status Codes Observed", "", "| Code | Operation count | Example descriptions |", "|---|---|---|"])
    for code in sorted(status_codes, key=lambda item: (not item.isdigit(), item)):
        examples = [desc for desc, _ in status_codes[code].most_common(3) if desc]
        lines.append(f"| `{md_cell(code)}` | {sum(status_codes[code].values())} | {md_cell(examples)} |")
    return "\n".join(lines).rstrip() + "\n"


def command_map(args: argparse.Namespace) -> int:
    specs = load_specs("ru")
    records = canonical_records_with_overlays()
    by_file: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_file[record["file"]].append(record)
    print("Wildberries API map")
    print(f"Source: {swagger_source('ru')} canonical + swagger/en/*.yaml search overlay ({LANG_LABELS[args.lang]} output, {len(records)} endpoints, {len(specs)} files)")
    for spec in specs:
        file_records = by_file[spec["_path"]]
        hosts = sorted({host.replace("https://", "") for record in file_records for host in record["servers"]})
        categories = sorted({record["category"] for record in file_records if record["category"]})
        tag_counts = Counter(localized(record, "tag", args.lang) or "Untagged" for record in file_records)
        display_title = localized(file_records[0], "title", args.lang) if file_records else title(spec)
        print()
        print(f"{display_title} ({len(file_records)}) - {rel(spec['_path'])}")
        if hosts:
            print(f"  hosts: {', '.join(hosts)}")
        if categories:
            print(f"  x-category: {', '.join(categories)}")
        for tag, count in tag_counts.items():
            print(f"  - {tag} ({count})")
    return 0


def command_generate(args: argparse.Namespace) -> int:
    specs = load_specs("ru")
    records = canonical_records_with_overlays()
    output_dir = (ROOT / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output)
    references_dir = output_dir / "references"
    references_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "endpoints-index.md").write_text(generate_endpoint_index(specs, records, args.lang), encoding="utf-8")
    by_file: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_file[record["file"]].append(record)
    expected = set()
    for spec in specs:
        output = references_dir / f"{file_slug(spec)}.md"
        expected.add(output)
        output.write_text(generate_reference(spec, by_file[spec["_path"]], args.lang), encoding="utf-8")
    protocol = references_dir / "protocol.md"
    expected.add(protocol)
    protocol.write_text(generate_protocol(records, specs, args.lang), encoding="utf-8")
    for stale in references_dir.glob("*.md"):
        if stale not in expected:
            stale.unlink()
    print(f"Generated {len(records)} endpoints into {rel(output_dir) if output_dir.is_relative_to(ROOT) else output_dir}.")
    return 0


def command_search(args: argparse.Namespace) -> int:
    records = ranked_records(canonical_records_with_overlays(), args.query)[: args.limit]
    if not records:
        print("No matching endpoints found.")
        return 1
    print("\n".join(endpoint_table(records, include_file=True, lang=args.lang)))
    return 0


def command_tag(args: argparse.Namespace) -> int:
    needle = normalize_text(args.tag)
    records = [
        record
        for record in canonical_records_with_overlays()
        if tag_matches(record, needle)
    ][: args.limit]
    if not records:
        print(f"No endpoints found for tag: {args.tag}")
        return 1
    print("\n".join(endpoint_table(records, include_file=True, lang=args.lang)))
    return 0


def select_detail_records(args: argparse.Namespace, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if args.operation_id:
        return [record for record in records if record["operation_id"] == args.operation_id]
    if not args.method or not args.path:
        raise SystemExit("detail requires <METHOD> <PATH> or --operation-id <id>")
    method = args.method.upper()
    return [record for record in records if record["method"] == method and record["path"] == args.path]


def command_detail(args: argparse.Namespace) -> int:
    matches_found = select_detail_records(args, canonical_records_with_overlays())
    if not matches_found:
        target = args.operation_id or f"{args.method.upper()} {args.path}"
        print(f"No exact endpoint found for {target}.")
        return 1
    for index, record in enumerate(matches_found):
        if index:
            print("\n---\n")
        print(f"# {record['method']} {record['path']}")
        print()
        print(f"Source: `{record['file_rel']}`")
        overlay = overlay_for_lang(record, args.lang)
        if overlay and overlay is not record:
            print(f"{LANG_LABELS[args.lang]} text overlay: `{overlay['file_rel']}`")
        print(f"Title: {localized(record, 'title', args.lang)}")
        print(f"Summary: {localized(record, 'summary', args.lang)}")
        if record["operation_id"]:
            print(f"Operation ID: `{record['operation_id']}`")
        display_tags = localized(record, "tags", args.lang)
        print(f"Tags: {', '.join(display_tags) if display_tags else 'none'}")
        print(f"Hosts: {', '.join(record['servers']) if record['servers'] else 'none declared'}")
        print(f"x-category: `{record['category']}`" if record["category"] else "x-category: none")
        if record["token_types"]:
            print(f"x-token-types: {', '.join(record['token_types'])}")
        print(f"Security: {', '.join(record['security']) if record['security'] else 'none declared'}")
        print(f"Readonly: {str(record['readonly']).lower()}")
        params = parameter_lines(record, args.lang)
        print("\n## Parameters")
        print("\n".join(params) if params else "None.")
        body = request_body_lines(record, args.lang)
        print("\n## Request Body")
        print("\n".join(body) if body else "None.")
        print("\n## Responses")
        print("\n".join(response_lines(record, args.lang)) or "None declared.")
        description = compact(localized(record, "description", args.lang), 900)
        if description:
            print("\n## Description Excerpt")
            print(description)
        if args.schemas:
            print_schema_details(record, args.schema_depth)
    return 0


def print_schema_details(record: dict[str, Any], max_depth: int) -> None:
    spec = record["spec"]
    request_media = request_body_media(record)
    if request_media:
        print("\n## Request Schemas")
        for media_type, schema in request_media:
            print(f"`{media_type}`")
            lines = schema_lines(spec, schema, max_depth=max_depth)
            print("\n".join(lines) if lines else "- no fields")

    primary_response = None
    for code, media_type, schema, _ in response_items(record):
        if code.startswith("2") and media_type == "application/json" and schema:
            primary_response = (code, media_type, schema)
            break
    if primary_response:
        code, media_type, schema = primary_response
        print(f"\n## Primary Response Schema ({code} {media_type})")
        lines = schema_lines(spec, schema, max_depth=max_depth)
        print("\n".join(lines) if lines else "- no fields")


def command_hosts(args: argparse.Namespace) -> int:
    records = canonical_records_with_overlays()
    hosts: dict[str, set[str]] = defaultdict(set)
    for record in records:
        for host in record["servers"]:
            hosts[host].add(record["category"])
    for host in sorted(hosts):
        categories = ", ".join(sorted(cat for cat in hosts[host] if cat))
        print(f"{host} - {categories}")
    return 0


def command_protocol(args: argparse.Namespace) -> int:
    specs = load_specs("ru")
    print(generate_protocol(canonical_records_with_overlays(), specs, args.lang))
    return 0


def collect_refs(node: Any) -> list[str]:
    refs: list[str] = []
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str):
            refs.append(ref)
        for value in node.values():
            refs.extend(collect_refs(value))
    elif isinstance(node, list):
        for value in node:
            refs.extend(collect_refs(value))
    return refs


def generated_expected(output_dir: Path, specs: list[dict[str, Any]], records: list[dict[str, Any]], lang: str) -> dict[Path, str]:
    by_file: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_file[record["file"]].append(record)
    expected = {output_dir / "endpoints-index.md": generate_endpoint_index(specs, records, lang)}
    references_dir = output_dir / "references"
    expected[references_dir / "protocol.md"] = generate_protocol(records, specs, lang)
    for spec in specs:
        expected[references_dir / f"{file_slug(spec)}.md"] = generate_reference(spec, by_file[spec["_path"]], lang)
    return expected


def parameter_signature(record: dict[str, Any]) -> tuple[tuple[str, str, bool, Any], ...]:
    spec = record["spec"]
    signature: list[tuple[str, str, bool, Any]] = []
    for raw_param in record["parameters"]:
        param = resolve_ref(spec, raw_param)
        if not isinstance(param, dict):
            continue
        schema = resolve_ref(spec, param.get("schema"))
        signature.append(
            (
                str(param.get("name", "")),
                str(param.get("in", "")),
                bool(param.get("required", False)),
                schema_shape(spec, schema),
            )
        )
    return tuple(signature)


def request_signature(record: dict[str, Any]) -> tuple[bool, tuple[tuple[str, Any], ...]]:
    spec = record["spec"]
    body = resolve_ref(spec, record.get("request_body"))
    required = bool(body.get("required", False)) if isinstance(body, dict) else False
    media = tuple((media_type, schema_shape(spec, schema)) for media_type, schema in request_body_media(record))
    return required, media


def response_signature(record: dict[str, Any]) -> tuple[tuple[str, str, Any], ...]:
    spec = record["spec"]
    return tuple((code, media_type, schema_shape(spec, schema)) for code, media_type, schema, _ in response_items(record))


def schema_shape(spec: dict[str, Any], schema: Any, seen: set[str] | None = None, depth: int = 0) -> Any:
    if seen is None:
        seen = set()
    if not isinstance(schema, dict):
        return None
    if "$ref" in schema:
        ref = str(schema["$ref"])
        if ref in seen:
            return ("recursive",)
        resolved = resolve_pointer(spec, ref)
        return schema_shape(spec, resolved, seen | {ref}, depth) if isinstance(resolved, dict) else ("unresolved", ref)
    if depth >= 8:
        return ("max-depth", schema.get("type", "object"))

    pieces: list[Any] = []
    for key in ("type", "format", "nullable", "minimum", "maximum", "minLength", "maxLength", "pattern"):
        if key in schema:
            pieces.append((key, schema[key]))
    if "enum" in schema:
        pieces.append(("enum", tuple(schema.get("enum") or [])))
    if "required" in schema:
        pieces.append(("required", tuple(sorted(schema.get("required") or []))))
    for key in ("allOf", "oneOf", "anyOf"):
        if isinstance(schema.get(key), list):
            pieces.append((key, tuple(schema_shape(spec, item, seen, depth + 1) for item in schema[key])))
    if "items" in schema:
        pieces.append(("items", schema_shape(spec, schema.get("items"), seen, depth + 1)))
    properties = schema.get("properties")
    if isinstance(properties, dict):
        pieces.append(
            (
                "properties",
                tuple((name, schema_shape(spec, value, seen, depth + 1)) for name, value in sorted(properties.items())),
            )
        )
    additional = schema.get("additionalProperties")
    if isinstance(additional, dict):
        pieces.append(("additionalProperties", schema_shape(spec, additional, seen, depth + 1)))
    return tuple(pieces)


def structural_signature(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "operationId": record["operation_id"],
        "servers": tuple(sorted(record["servers"])),
        "security": tuple(sorted(record["security"])),
        "x-token-types": tuple(sorted(record["token_types"])),
        "readonly": record["readonly"],
        "parameters": parameter_signature(record),
        "request": request_signature(record),
        "responses": response_signature(record),
    }


def validate_spec_set(lang: str, specs: list[dict[str, Any]], records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    duplicates = [
        item for item, count in Counter((record["method"], record["path"]) for record in records).items() if count > 1
    ]
    if duplicates:
        for method, path in duplicates:
            errors.append(f"{lang}: duplicate method/path pair {method} {path}")

    unresolved: list[tuple[str, str]] = []
    for spec in specs:
        for ref in collect_refs(spec):
            if ref.startswith("#/") and resolve_pointer(spec, ref) is None:
                unresolved.append((rel(spec["_path"]), ref))
    if unresolved:
        for file_rel, ref in unresolved[:50]:
            errors.append(f"{lang}: unresolved local $ref {file_rel}: {ref}")
        if len(unresolved) > 50:
            errors.append(f"{lang}: ... {len(unresolved) - 50} more unresolved refs")

    missing_titles = [rel(spec["_path"]) for spec in specs if not title(spec)]
    missing_tags = [f"{record['method']} {record['path']}" for record in records if not record["tag"]]
    for item in missing_titles:
        errors.append(f"{lang}: missing info.title in {item}")
    for item in missing_tags[:50]:
        errors.append(f"{lang}: operation missing tags {item}")
    if len(missing_tags) > 50:
        errors.append(f"{lang}: ... {len(missing_tags) - 50} more operations missing tags")
    return errors


def validate_bilingual_mirror(ru_specs: list[dict[str, Any]], ru_records: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    en_specs = load_specs("en")
    en_records = iter_operations(en_specs)
    print(f"Parsed {len(en_records)} English-overlay endpoints from {len(en_specs)} Swagger files.")

    ru_files = {Path(spec["_path"]).name for spec in ru_specs}
    en_files = {Path(spec["_path"]).name for spec in en_specs}
    for filename in sorted(ru_files - en_files):
        errors.append(f"en: missing mirror file swagger/en/{filename}")
    for filename in sorted(en_files - ru_files):
        errors.append(f"en: extra mirror file swagger/en/{filename}")

    ru_map = {file_operation_key(record): record for record in ru_records}
    en_map = {file_operation_key(record): record for record in en_records}
    for key in sorted(set(ru_map) - set(en_map)):
        filename, method, path = key
        errors.append(f"en: missing mirror operation {filename} {method} {path}")
    for key in sorted(set(en_map) - set(ru_map)):
        filename, method, path = key
        errors.append(f"en: extra mirror operation {filename} {method} {path}")

    for key in sorted(set(ru_map) & set(en_map)):
        ru_signature = structural_signature(ru_map[key])
        en_signature = structural_signature(en_map[key])
        for field in sorted(ru_signature):
            if ru_signature[field] != en_signature[field]:
                filename, method, path = key
                warnings.append(f"en: structural drift in {filename} {method} {path}: {field}")
    return errors, warnings


def command_validate(args: argparse.Namespace) -> int:
    specs = load_specs("ru")
    records = iter_operations(specs)
    print(f"Parsed {len(records)} canonical Russian endpoints from {len(specs)} Swagger files.")
    errors = validate_spec_set("ru", specs, records)
    warnings: list[str] = []
    if LANG_DIRS["en"].exists():
        en_specs = load_specs("en")
        en_records = iter_operations(en_specs)
        errors.extend(validate_spec_set("en", en_specs, en_records))
        mirror_errors, mirror_warnings = validate_bilingual_mirror(specs, records)
        errors.extend(mirror_errors)
        warnings.extend(mirror_warnings)
    if errors:
        print("Swagger validation failed:")
        for error in errors[:100]:
            print(f"- {error}")
        if len(errors) > 100:
            print(f"... {len(errors) - 100} more")
        return 1
    if warnings:
        print("English overlay structural warnings:")
        for warning in warnings[:100]:
            print(f"- {warning}")
        if len(warnings) > 100:
            print(f"... {len(warnings) - 100} more")
        print("Russian Swagger remains canonical for schemas, parameters, request bodies, and responses.")

    if args.generated:
        generated_specs = load_specs("ru")
        generated_records = canonical_records_with_overlays()
        output_dir = (ROOT / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output)
        expected = generated_expected(output_dir, generated_specs, generated_records, args.lang)
        missing = [path for path in expected if not path.exists()]
        stale = [path for path, content in expected.items() if path.exists() and path.read_text(encoding="utf-8") != content]
        extra = sorted((output_dir / "references").glob("*.md")) if (output_dir / "references").exists() else []
        extra = [path for path in extra if path not in expected]
        if missing or stale or extra:
            print(f"Generated files under {output_dir} are not current; run `python3 scripts/wb_api.py generate`.")
            for label, paths in (("missing", missing), ("stale", stale), ("extra", extra)):
                for path in paths:
                    print(f"- {label}: {rel(path) if path.is_relative_to(ROOT) else path}")
            return 1
        print("Generated reference files match Swagger.")

    print("Swagger references and bilingual mirror are valid.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(required=True)

    search = subparsers.add_parser("search", help="Ranked search over paths, summaries, tags, descriptions, operation IDs, hosts, and files")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=25)
    search.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Output language; search indexes both Russian and English")
    search.set_defaults(func=command_search)

    detail = subparsers.add_parser("detail", help="Print compact details for an exact endpoint")
    detail.add_argument("method", nargs="?")
    detail.add_argument("path", nargs="?")
    detail.add_argument("--operation-id")
    detail.add_argument("--schemas", action="store_true", help="Expand request and primary response schemas")
    detail.add_argument("--schema-depth", type=int, default=4)
    detail.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Output language")
    detail.set_defaults(func=command_detail)

    tag = subparsers.add_parser("tag", help="List endpoints for a tag")
    tag.add_argument("tag")
    tag.add_argument("--limit", type=int, default=100)
    tag.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Output language; tag matching checks both Russian and English")
    tag.set_defaults(func=command_tag)

    map_cmd = subparsers.add_parser("map", help="Print Swagger-file, tag, host, and category overview")
    map_cmd.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Output language")
    map_cmd.set_defaults(func=command_map)

    hosts = subparsers.add_parser("hosts", help="List hosts and observed x-category values")
    hosts.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Output language")
    hosts.set_defaults(func=command_hosts)

    protocol = subparsers.add_parser("protocol", help="Print Swagger-derived auth, host, token, ping, and status summary")
    protocol.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Output language")
    protocol.set_defaults(func=command_protocol)

    generate = subparsers.add_parser("generate", help="Optionally generate browseable markdown from Swagger")
    generate.add_argument("--output", default="generated")
    generate.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Generated documentation language")
    generate.set_defaults(func=command_generate)

    validate = subparsers.add_parser("validate", help="Validate Swagger parsing, duplicate method/path pairs, and local $ref values")
    validate.add_argument("--generated", action="store_true", help="Also validate optional generated markdown output")
    validate.add_argument("--output", default="generated")
    validate.add_argument("--lang", choices=SUPPORTED_LANGS, default="ru", help="Generated documentation language when using --generated")
    validate.set_defaults(func=command_validate)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

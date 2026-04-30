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
GENERATED = "Generated from `swagger/*.yaml` by `scripts/wb_api.py generate`. Do not edit by hand; Swagger is the source of truth."


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse as a YAML mapping")
    return data


def load_specs() -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for path in sorted(SWAGGER_DIR.glob("*.yaml")):
        spec = load_yaml(path)
        spec["_path"] = path
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
    return [
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


def md_cell(value: Any) -> str:
    text = ", ".join(str(item) for item in value) if isinstance(value, list) else str(value or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text.replace("|", r"\|")


def endpoint_table(records: list[dict[str, Any]], include_file: bool = False) -> list[str]:
    if include_file:
        lines = ["| File | Tag | Method | Path | Hosts | Summary | Operation ID |", "|---|---|---|---|---|---|---|"]
    else:
        lines = ["| Tag | Method | Path | Hosts | Category | Summary | Operation ID |", "|---|---|---|---|---|---|---|"]
    for record in records:
        hosts = [url.replace("https://", "") for url in record["servers"]]
        row = [
            md_cell(record["tag"]),
            f"`{record['method']}`",
            f"`{md_cell(record['path'])}`",
            md_cell(hosts),
        ]
        if include_file:
            row.insert(0, md_cell(record["file_rel"]))
        else:
            row.append(md_cell(record["category"]))
        row.extend([md_cell(record["summary"]), f"`{md_cell(record['operation_id'])}`" if record["operation_id"] else ""])
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


def parameter_lines(record: dict[str, Any]) -> list[str]:
    spec = record["spec"]
    lines: list[str] = []
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
        desc = compact(param.get("description"), 140)
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


def request_body_lines(record: dict[str, Any]) -> list[str]:
    spec = record["spec"]
    body = resolve_ref(spec, record.get("request_body"))
    if not isinstance(body, dict):
        return []
    lines = [f"- required={str(bool(body.get('required', False))).lower()}"]
    for media_type, schema in request_body_media(record):
        lines.append(f"- `{media_type}` schema={schema_summary(spec, schema)}")
    desc = compact(body.get("description"), 200)
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


def response_lines(record: dict[str, Any]) -> list[str]:
    spec = record["spec"]
    lines: list[str] = []
    grouped: dict[str, list[str]] = defaultdict(list)
    desc_by_code: dict[str, str] = {}
    for code, media_type, schema, desc in response_items(record):
        desc_by_code[code] = desc
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


def generate_endpoint_index(specs: list[dict[str, Any]], records: list[dict[str, Any]]) -> str:
    lines = [
        "# Wildberries API - Generated Endpoint Index",
        "",
        GENERATED,
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
        lines.extend([f"## {title(spec)} ({rel(spec['_path'])})", ""])
        lines.extend(endpoint_table(by_file.get(spec["_path"], [])))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate_reference(spec: dict[str, Any], records: list[dict[str, Any]]) -> str:
    hosts = sorted({host.replace("https://", "") for record in records for host in record["servers"]})
    categories = sorted({record["category"] for record in records if record["category"]})
    tags = sorted({record["tag"] for record in records if record["tag"]})
    lines = [
        f"# {title(spec)}",
        "",
        GENERATED,
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
        by_tag[record["tag"] or "Untagged"].append(record)
    for tag_name in sorted(by_tag):
        lines.extend([f"## {tag_name}", ""])
        lines.extend(endpoint_table(by_tag[tag_name]))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate_protocol(records: list[dict[str, Any]], specs: list[dict[str, Any]]) -> str:
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
        "Derived live from `swagger/*.yaml`; Swagger is the source of truth.",
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
    lines.extend(endpoint_table(ping_records, include_file=True) if ping_records else ["No `/ping` operation is declared."])

    lines.extend(["", "## Response Status Codes Observed", "", "| Code | Operation count | Example descriptions |", "|---|---|---|"])
    for code in sorted(status_codes, key=lambda item: (not item.isdigit(), item)):
        examples = [desc for desc, _ in status_codes[code].most_common(3) if desc]
        lines.append(f"| `{md_cell(code)}` | {sum(status_codes[code].values())} | {md_cell(examples)} |")
    return "\n".join(lines).rstrip() + "\n"


def command_map(_: argparse.Namespace) -> int:
    specs = load_specs()
    records = iter_operations(specs)
    by_file: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_file[record["file"]].append(record)
    print("Wildberries API map")
    print(f"Source: swagger/*.yaml ({len(records)} endpoints, {len(specs)} files)")
    for spec in specs:
        file_records = by_file[spec["_path"]]
        hosts = sorted({host.replace("https://", "") for record in file_records for host in record["servers"]})
        categories = sorted({record["category"] for record in file_records if record["category"]})
        tag_counts = Counter(record["tag"] or "Untagged" for record in file_records)
        print()
        print(f"{title(spec)} ({len(file_records)}) - {rel(spec['_path'])}")
        if hosts:
            print(f"  hosts: {', '.join(hosts)}")
        if categories:
            print(f"  x-category: {', '.join(categories)}")
        for tag, count in tag_counts.items():
            print(f"  - {tag} ({count})")
    return 0


def command_generate(args: argparse.Namespace) -> int:
    specs = load_specs()
    records = iter_operations(specs)
    output_dir = (ROOT / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output)
    references_dir = output_dir / "references"
    references_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "endpoints-index.md").write_text(generate_endpoint_index(specs, records), encoding="utf-8")
    by_file: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_file[record["file"]].append(record)
    expected = set()
    for spec in specs:
        output = references_dir / f"{file_slug(spec)}.md"
        expected.add(output)
        output.write_text(generate_reference(spec, by_file[spec["_path"]]), encoding="utf-8")
    protocol = references_dir / "protocol.md"
    expected.add(protocol)
    protocol.write_text(generate_protocol(records, specs), encoding="utf-8")
    for stale in references_dir.glob("*.md"):
        if stale not in expected:
            stale.unlink()
    print(f"Generated {len(records)} endpoints into {rel(output_dir) if output_dir.is_relative_to(ROOT) else output_dir}.")
    return 0


def command_search(args: argparse.Namespace) -> int:
    records = ranked_records(iter_operations(load_specs()), args.query)[: args.limit]
    if not records:
        print("No matching endpoints found.")
        return 1
    print("\n".join(endpoint_table(records, include_file=True)))
    return 0


def command_tag(args: argparse.Namespace) -> int:
    needle = normalize_text(args.tag)
    records = [
        record
        for record in iter_operations(load_specs())
        if needle == normalize_text(record["tag"]) or needle in normalize_text(record["tag"])
    ][: args.limit]
    if not records:
        print(f"No endpoints found for tag: {args.tag}")
        return 1
    print("\n".join(endpoint_table(records, include_file=True)))
    return 0


def select_detail_records(args: argparse.Namespace, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if args.operation_id:
        return [record for record in records if record["operation_id"] == args.operation_id]
    if not args.method or not args.path:
        raise SystemExit("detail requires <METHOD> <PATH> or --operation-id <id>")
    method = args.method.upper()
    return [record for record in records if record["method"] == method and record["path"] == args.path]


def command_detail(args: argparse.Namespace) -> int:
    matches_found = select_detail_records(args, iter_operations(load_specs()))
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
        print(f"Title: {record['title']}")
        print(f"Summary: {record['summary']}")
        if record["operation_id"]:
            print(f"Operation ID: `{record['operation_id']}`")
        print(f"Tags: {', '.join(record['tags']) if record['tags'] else 'none'}")
        print(f"Hosts: {', '.join(record['servers']) if record['servers'] else 'none declared'}")
        print(f"x-category: `{record['category']}`" if record["category"] else "x-category: none")
        if record["token_types"]:
            print(f"x-token-types: {', '.join(record['token_types'])}")
        print(f"Security: {', '.join(record['security']) if record['security'] else 'none declared'}")
        print(f"Readonly: {str(record['readonly']).lower()}")
        params = parameter_lines(record)
        print("\n## Parameters")
        print("\n".join(params) if params else "None.")
        body = request_body_lines(record)
        print("\n## Request Body")
        print("\n".join(body) if body else "None.")
        print("\n## Responses")
        print("\n".join(response_lines(record)) or "None declared.")
        description = compact(record["description"], 900)
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


def command_hosts(_: argparse.Namespace) -> int:
    records = iter_operations(load_specs())
    hosts: dict[str, set[str]] = defaultdict(set)
    for record in records:
        for host in record["servers"]:
            hosts[host].add(record["category"])
    for host in sorted(hosts):
        categories = ", ".join(sorted(cat for cat in hosts[host] if cat))
        print(f"{host} - {categories}")
    return 0


def command_protocol(_: argparse.Namespace) -> int:
    specs = load_specs()
    print(generate_protocol(iter_operations(specs), specs))
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


def generated_expected(output_dir: Path, specs: list[dict[str, Any]], records: list[dict[str, Any]]) -> dict[Path, str]:
    by_file: dict[Path, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_file[record["file"]].append(record)
    expected = {output_dir / "endpoints-index.md": generate_endpoint_index(specs, records)}
    references_dir = output_dir / "references"
    expected[references_dir / "protocol.md"] = generate_protocol(records, specs)
    for spec in specs:
        expected[references_dir / f"{file_slug(spec)}.md"] = generate_reference(spec, by_file[spec["_path"]])
    return expected


def command_validate(args: argparse.Namespace) -> int:
    specs = load_specs()
    records = iter_operations(specs)
    print(f"Parsed {len(records)} endpoints from {len(specs)} Swagger files.")
    duplicates = [
        item for item, count in Counter((record["method"], record["path"]) for record in records).items() if count > 1
    ]
    if duplicates:
        print("Duplicate method/path pairs:")
        for method, path in duplicates:
            print(f"- {method} {path}")
        return 1

    unresolved: list[tuple[str, str]] = []
    for spec in specs:
        for ref in collect_refs(spec):
            if ref.startswith("#/") and resolve_pointer(spec, ref) is None:
                unresolved.append((rel(spec["_path"]), ref))
    if unresolved:
        print("Unresolved local $ref values:")
        for file_rel, ref in unresolved[:50]:
            print(f"- {file_rel}: {ref}")
        if len(unresolved) > 50:
            print(f"... {len(unresolved) - 50} more")
        return 1

    missing_titles = [rel(spec["_path"]) for spec in specs if not title(spec)]
    missing_tags = [f"{record['method']} {record['path']}" for record in records if not record["tag"]]
    if missing_titles or missing_tags:
        if missing_titles:
            print("Swagger files missing info.title:")
            print("\n".join(f"- {item}" for item in missing_titles))
        if missing_tags:
            print("Operations missing tags:")
            print("\n".join(f"- {item}" for item in missing_tags[:50]))
        return 1

    if args.generated:
        output_dir = (ROOT / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output)
        expected = generated_expected(output_dir, specs, records)
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

    print("Swagger references are valid.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(required=True)

    search = subparsers.add_parser("search", help="Ranked search over paths, summaries, tags, descriptions, operation IDs, hosts, and files")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=25)
    search.set_defaults(func=command_search)

    detail = subparsers.add_parser("detail", help="Print compact details for an exact endpoint")
    detail.add_argument("method", nargs="?")
    detail.add_argument("path", nargs="?")
    detail.add_argument("--operation-id")
    detail.add_argument("--schemas", action="store_true", help="Expand request and primary response schemas")
    detail.add_argument("--schema-depth", type=int, default=4)
    detail.set_defaults(func=command_detail)

    tag = subparsers.add_parser("tag", help="List endpoints for a tag")
    tag.add_argument("tag")
    tag.add_argument("--limit", type=int, default=100)
    tag.set_defaults(func=command_tag)

    map_cmd = subparsers.add_parser("map", help="Print Swagger-file, tag, host, and category overview")
    map_cmd.set_defaults(func=command_map)

    hosts = subparsers.add_parser("hosts", help="List hosts and observed x-category values")
    hosts.set_defaults(func=command_hosts)

    protocol = subparsers.add_parser("protocol", help="Print Swagger-derived auth, host, token, ping, and status summary")
    protocol.set_defaults(func=command_protocol)

    generate = subparsers.add_parser("generate", help="Optionally generate browseable markdown from swagger/*.yaml")
    generate.add_argument("--output", default="generated")
    generate.set_defaults(func=command_generate)

    validate = subparsers.add_parser("validate", help="Validate Swagger parsing, duplicate method/path pairs, and local $ref values")
    validate.add_argument("--generated", action="store_true", help="Also validate optional generated markdown output")
    validate.add_argument("--output", default="generated")
    validate.set_defaults(func=command_validate)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

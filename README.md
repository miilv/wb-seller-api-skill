# Wildberries Seller API - Agent Skill

An [Agent Skills](https://agentskills.io) package for working with the **Wildberries Seller API** in compatible coding agents such as Codex, Claude Code, and other tools that load `SKILL.md`.

The repository keeps local Swagger files as the only API documentation source of truth. Russian specs in `swagger/*.yaml` are canonical for schemas and protocol details; English specs in `swagger/en/*.yaml` are used as a validated search and text-label overlay.

## Installation

Clone this repository into the skills directory used by your agent.

Codex user skill:

```bash
git clone https://github.com/miilv/wb-seller-api-skill.git ~/.agents/skills/wildberries-api
```

Codex repository-scoped skill:

```bash
git clone https://github.com/miilv/wb-seller-api-skill.git .agents/skills/wildberries-api
```

Claude Code personal skill:

```bash
git clone https://github.com/miilv/wb-seller-api-skill.git ~/.claude/skills/wildberries-api
```

Claude Code project skill:

```bash
git clone https://github.com/miilv/wb-seller-api-skill.git .claude/skills/wildberries-api
```

Restart or refresh your agent if it does not detect the new skill automatically.

## Usage

Agents can activate the skill automatically when you mention Wildberries API, WB seller integrations, marketplace endpoints, product cards, prices, stocks, orders, supplies, feedbacks, analytics, reports, promotion, tariffs, or finances. You can also invoke it directly in agents that expose skills as commands, for example `/wildberries-api`.

Example prompts:

```text
How do I fetch Wildberries product cards?
Найди endpoint для рейтинга продавца.
Generate a Python client call for FBS order metadata.
Which WB API host should I use for analytics reports?
Show request and response schemas for POST /content/v2/get/cards/list.
```

## Included Files

| File | Description |
|------|-------------|
| `SKILL.md` | Skill instructions and progressive-disclosure workflow |
| `swagger/*.yaml` | Canonical Russian OpenAPI specs for Wildberries Seller API |
| `swagger/en/*.yaml` | English Swagger mirror used for search and text labels |
| `scripts/wb_api.py` | Local helper for Swagger-derived maps, endpoint search, detail lookup, schema expansion, generated docs, and validation |
| `requirements.txt` | Python dependency list for the helper |

## Lookup Helper

Install the helper dependency if needed:

```bash
python3 -m pip install -r requirements.txt
```

Run compact Swagger-derived lookups from the skill directory:

```bash
python3 scripts/wb_api.py validate
python3 scripts/wb_api.py map
python3 scripts/wb_api.py search "seller rating" --limit 5 --lang en
python3 scripts/wb_api.py search "рейтинг продавца" --limit 5
python3 scripts/wb_api.py tag "Product Cards" --lang en
python3 scripts/wb_api.py detail POST /content/v2/get/cards/list --schemas
python3 scripts/wb_api.py detail POST /content/v2/get/cards/list --schemas --lang en
python3 scripts/wb_api.py protocol
python3 scripts/wb_api.py generate --output generated --lang en
```

The helper does not make network calls and is not a Wildberries API client. It reads local Swagger files and prints compact output so agents do not need to load full API specs into context.

`--lang en` changes human-readable labels and descriptions where an English mirror exists. Exact parameters, request bodies, response schemas, auth schemes, hosts, token hints, and validation still come from canonical Russian Swagger.

## Validation

Use `python3 scripts/wb_api.py validate` after changing Swagger or helper code. Validation checks:

- Russian and English specs parse successfully
- duplicate method/path pairs
- unresolved local `$ref` values
- missing titles or operation tags
- Russian/English mirror file and operation coverage
- structural drift warnings between Russian canonical specs and the English overlay
- optional generated markdown freshness with `--generated`

Structural drift in the English overlay is reported as a warning because Russian Swagger remains canonical for API behavior.

## Source

Swagger files are local snapshots of Wildberries Seller API documentation. Replace or regenerate the Swagger snapshots when Wildberries updates the API. Derived markdown references are intentionally not kept in this repository; generate them on demand with `scripts/wb_api.py generate`.

---
name: wildberries-api
description: Swagger-backed Wildberries seller API reference for WB marketplace integrations. Use when building or debugging code that calls Wildberries/WB seller API endpoints, choosing endpoints, checking request/response schemas, authentication headers, hosts, rate limits, or API capabilities.
---

# Wildberries API

Treat local Swagger as the only API source of truth. Russian files in `swagger/*.yaml` are canonical; English files in `swagger/en/*.yaml` are a validated translation overlay for English search and text labels. Use the helper script for compact Swagger-derived lookups; do not load full Swagger files unless the helper output is insufficient.

## Default Workflow

The helper requires PyYAML. If it is missing, install dependencies with `python3 -m pip install -r requirements.txt`.

1. Start with the compact Swagger query script:
   - Get an overview: `python3 scripts/wb_api.py map`
   - Search endpoints in Russian or English: `python3 scripts/wb_api.py search "<query>" --limit 25`
   - Inspect an exact endpoint: `python3 scripts/wb_api.py detail <METHOD> <PATH>`
   - Expand request/response fields: `python3 scripts/wb_api.py detail <METHOD> <PATH> --schemas`
   - Inspect auth, hosts, token hints, ping, and status codes: `python3 scripts/wb_api.py protocol`
   - List observed hosts/categories only: `python3 scripts/wb_api.py hosts`
   - Add `--lang en` when English terminal labels are more useful; exact schemas, parameters, request bodies, and responses still come from canonical Russian Swagger.
2. Open raw `swagger/*.yaml` only when the script output is insufficient for exact schemas, nested examples, enum values, or long endpoint descriptions.
3. If human-readable browse docs are needed, generate them on demand with `python3 scripts/wb_api.py generate`; generated output is ignored by git.
4. Validate parser coverage and the Russian/English mirror before relying on output: `python3 scripts/wb_api.py validate`.

## Answering Rules

- Cite method, path, host, source Swagger file, auth scheme, parameters/body, and relevant response codes.
- Do not invent global protocol details. For rate limits, token types, sandbox behavior, or status meaning, use endpoint descriptions, `x-token-types`, `servers`, `securitySchemes`, and responses from Swagger.
- Prefer compact script output over loading complete Swagger files into context.
- If the local Swagger snapshot does not contain what the user expects, say that directly and ask before checking live docs.

## Code Generation Checklist

- Read credentials from env/config; never hard-code the token.
- Send the token using the Swagger-declared `HeaderApiKey` scheme (`Authorization` header).
- Use the host declared on the operation or inherited by its path/spec.
- Implement pagination, polling, retries, and payload validation only when the endpoint schema or description calls for it.

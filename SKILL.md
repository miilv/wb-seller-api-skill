---
name: wildberries-api
description: Wildberries seller API reference. Use when building integrations with Wildberries marketplace, writing code that calls WB API endpoints, debugging WB API issues, or when the user asks about Wildberries API capabilities, endpoints, authentication, or rate limits.
---

# Wildberries API

The Wildberries API (WB API) provides sellers with tools to manage their store via HTTP REST API. It enables automation of store operations through integration with ERP, WMS, OMS, CRM systems.

## Authentication

All requests require an API token in the `Authorization` header. Tokens are JWT (RFC 7519), valid for **180 days**.

**Token types:**
- **Personal access** (`acc:3`, `for:self`) -- full access, must not be shared with third parties
- **Service** (`acc:4`) -- for a specific cloud service from WB's catalog
- **Base** (`acc:1`) -- limited data access, for testing or fallback
- **Test** (`acc:2`, `t:true`) -- sandbox only, generated test data

Each token has a bitmask field `s` controlling category access (Content, Analytics, Prices, Marketplace, Statistics, Promotion, Feedbacks, Buyers Chat, Supplies, Returns, Documents, Finance, Users).

## Base URLs by API Category

| Category | Production Base URL | Sandbox Base URL |
|----------|-------------------|-----------------|
| Common (News, Seller Info, Tariffs) | `common-api.wildberries.ru` | -- |
| Content | `content-api.wildberries.ru` | `content-api-sandbox.wildberries.ru` |
| Analytics | `seller-analytics-api.wildberries.ru` | -- |
| Prices and Discounts | `discounts-prices-api.wildberries.ru` | `discounts-prices-api-sandbox.wildberries.ru` |
| Marketplace (FBS/DBS/Pickup) | `marketplace-api.wildberries.ru` | -- |
| Statistics | `statistics-api.wildberries.ru` | `statistics-api-sandbox.wildberries.ru` |
| Promotion | `advert-api.wildberries.ru` | `advert-api-sandbox.wildberries.ru` |
| Promotion (Media) | `advert-media-api.wildberries.ru` | -- |
| Promotions Calendar | `dp-calendar-api.wildberries.ru` | -- |
| Feedbacks and Questions | `feedbacks-api.wildberries.ru` | `feedbacks-api-sandbox.wildberries.ru` |
| Buyers Chat | `buyer-chat-api.wildberries.ru` | -- |
| Supplies (FBW) | `supplies-api.wildberries.ru` | -- |
| Buyers Returns | `returns-api.wildberries.ru` | -- |
| Documents | `documents-api.wildberries.ru` | -- |
| Finance | `finance-api.wildberries.ru` | -- |
| User Management | `user-management-api.wildberries.ru` | -- |

## Rate Limiting

Uses token bucket algorithm. Key headers:
- `X-Ratelimit-Remaining` -- requests available without pause
- `X-Ratelimit-Retry` -- seconds to wait after 429
- `X-Ratelimit-Limit` -- max burst size
- `X-Ratelimit-Reset` -- seconds until burst fully restores

A `409` response typically counts as **10 requests** toward the limit.

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 204 | Deleted/Updated/Confirmed |
| 400 | Bad request -- check syntax |
| 401 | Unauthorized -- check token category, expiry |
| 403 | Access denied -- token user deleted or method blocked |
| 404 | Not found -- check URL |
| 409 | Conflict -- check data requirements |
| 413 | Request body too large -- reduce objects |
| 422 | Unprocessable -- contradictory request data |
| 429 | Rate limited -- wait per `X-Ratelimit-Retry` |
| 5xx | Server error -- retry later |

## Connection Test

`GET https://{base-url}/ping` -- works with any token category. Max 3 requests per 30 seconds.

## Documentation Files

The full reference is generated from the official OpenAPI specs at https://dev.wildberries.ru/openapi/. **287 endpoints** across **13 categories**.

For the **complete endpoint index** with all 287 endpoints, see:
- [endpoints-index.md](endpoints-index.md) — quick lookup table of every endpoint

For **endpoint listings per category** (lightweight: method, path, summary), see:
- [references/general.md](references/general.md) — news, seller info, ping, common methods
- [references/products.md](references/products.md) — product cards, categories, media, tags, prices, discounts, content
- [references/orders-fbs.md](references/orders-fbs.md) — FBS orders (fulfillment by seller)
- [references/orders-dbw.md](references/orders-dbw.md) — DBW orders (delivery by Wildberries)
- [references/orders-dbs.md](references/orders-dbs.md) — DBS orders (delivery by seller)
- [references/in-store-pickup.md](references/in-store-pickup.md) — in-store pickup orders
- [references/orders-fbw.md](references/orders-fbw.md) — FBW supplies (fulfillment by Wildberries)
- [references/promotion.md](references/promotion.md) — ad campaigns, media, calendar, marketing
- [references/communications.md](references/communications.md) — feedbacks, questions, buyer chat, reviews
- [references/tariffs.md](references/tariffs.md) — commission, storage, return tariffs
- [references/analytics.md](references/analytics.md) — sales funnel, search queries, stocks, brands
- [references/reports.md](references/reports.md) — statistics, warehouses, retention, returns
- [references/finances.md](references/finances.md) — finance reports, documents, accounting

For **full request/response schemas**, read the raw OpenAPI 3.0.1 YAMLs in [swagger/](swagger/) (one file per category, matches the references above 1-to-1).

## How to Use This Skill

1. When the user asks about a specific endpoint, look it up in `endpoints-index.md` first
2. For a quick category overview, read the relevant `references/*.md`
3. For detailed request/response schemas, read the corresponding `swagger/*.yaml`
4. Always pass the token via `Authorization` header (not query params)
5. Use the correct base URL for the API category (do not mix hosts)
6. Generate working code examples in the user's preferred language

## Code Generation Guidelines

When writing code that interacts with WB API:

1. Always pass the token via `Authorization` header (not query params)
2. Respect rate limits -- implement exponential backoff on 429 responses, read `X-Ratelimit-Retry` header
3. Use the correct base URL for the API category (do not mix hosts)
4. Handle pagination where endpoints support `cursor`/`limit`/`offset` patterns
5. For async reports (warehouse remains, paid storage, paid reception), use the create-task -> poll-status -> download pattern
6. Token category in the JWT `s` bitmask must include the bit for the API category being accessed
7. Sandbox endpoints use `-sandbox` suffix on the base domain where available

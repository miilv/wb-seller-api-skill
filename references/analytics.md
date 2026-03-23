# Analytics API

Base URL: `https://seller-analytics-api.wildberries.ru`
Token category: **Analytics**
Default rate limit: 3 req/min, 20s interval, burst 3

## Sales Funnel

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/analytics/v3/sales-funnel/products` | Product cards stats per period (compare current vs past, max 365 days) |
| POST | `/api/analytics/v3/sales-funnel/products/history` | Product cards stats per day/week (max last 7 days) |
| POST | `/api/analytics/v3/sales-funnel/grouped/history` | Grouped cards stats per day/week by subjects, brands, tags |

## Search Queries (requires Jam subscription)

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v2/search-report/report` | Main search report -- positions, visibility, groups |
| POST | `/api/v2/search-report/table/groups` | Pagination by groups (requires brand/subject/tag filter) |
| POST | `/api/v2/search-report/table/details` | Pagination by products within a group |
| POST | `/api/v2/search-report/product/search-texts` | Top search texts driving traffic for products |
| POST | `/api/v2/search-report/product/orders` | Orders and positions by product search texts (max 7 days) |

## Stocks Report

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v2/stocks-report/products/groups` | Inventory grouped by product group (subject, brand, tag) |
| POST | `/api/v2/stocks-report/products/products` | Inventory by individual products |
| POST | `/api/v2/stocks-report/products/sizes` | Inventory by product size with optional warehouse breakdown |
| POST | `/api/v2/stocks-report/offices` | Inventory by warehouses/regions |

## CSV Report Generation

Max 20 reports/day, up to 1 year of data. Reports available for 48h after generation.

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v2/nm-report/downloads` | Create CSV report task |
| GET | `/api/v2/nm-report/downloads` | List reports with generation statuses |
| POST | `/api/v2/nm-report/downloads/retry` | Retry a failed report |
| GET | `/api/v2/nm-report/downloads/file/{downloadId}` | Download report as ZIP |

Report types: `DETAIL_HISTORY_REPORT`, `GROUPED_HISTORY_REPORT`, `SEARCH_QUERIES_PREMIUM_REPORT_GROUP`, `SEARCH_QUERIES_PREMIUM_REPORT_PRODUCT`, `SEARCH_QUERIES_PREMIUM_REPORT_TEXT`, `STOCK_HISTORY_REPORT_CSV`

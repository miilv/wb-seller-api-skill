# Reports API

## Main Reports (Statistics)

Base URL: `https://statistics-api.wildberries.ru`
Token category: **Statistics**
Rate limit: 1 req/min, burst 1

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/supplier/stocks` | WB warehouse inventory in real time (up to 60,000 rows) |
| GET | `/api/v1/supplier/orders` | Order info, updated every 30 min (up to 80,000 rows, 90 days) |
| GET | `/api/v1/supplier/sales` | Sales and returns, updated every 30 min (up to 80,000 rows, 90 days) |
| GET | `/api/v1/supplier/incomes` | **DEPRECATED** -- Supply data |

## Warehouses Inventory Report

Base URL: `https://seller-analytics-api.wildberries.ru`
Token category: **Analytics**

Async pattern: create task -> poll status -> download

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v1/warehouse_remains` | Create report generation task | 1 req/min, burst 5 |
| GET | `/api/v1/warehouse_remains/tasks/{task_id}/status` | Check task status | 1 req/5s, burst 5 |
| GET | `/api/v1/warehouse_remains/tasks/{task_id}/download` | Download report | 1 req/min, burst 1 |

## Mandatory Labeling Report

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| POST | `/api/v1/analytics/excise-report` | Operations with labeled products (by country) | 10 req/5h, 30min interval |

## Retention Reports

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/analytics/v1/measurement-penalties` | Logistics/storage cost multipliers | 1 req/min |
| GET | `/api/analytics/v1/warehouse-measurements` | Warehouse measurements | 1 req/min |
| GET | `/api/analytics/v1/deductions` | Substitutions and incorrect attachments | 1 req/min |
| GET | `/api/v1/analytics/antifraud-details` | Self-purchase deductions (weekly, Wednesdays) | 1 req/10min |
| GET | `/api/v1/analytics/goods-labeling` | Deductions for missing product labeling (from Mar 2024) | 1 req/min |

## Paid Reception Report

Async pattern: create task -> poll status -> download

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v1/acceptance_report` | Create task (max 31 day period) | 1 req/min |
| GET | `/api/v1/acceptance_report/tasks/{task_id}/status` | Check status | 1 req/5s |
| GET | `/api/v1/acceptance_report/tasks/{task_id}/download` | Download report | 1 req/min |

## Paid Storage Report

Async pattern: create task -> poll status -> download

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v1/paid_storage` | Create task (max 8 day period) | 1 req/min, burst 5 |
| GET | `/api/v1/paid_storage/tasks/{task_id}/status` | Check status | 1 req/5s, burst 5 |
| GET | `/api/v1/paid_storage/tasks/{task_id}/download` | Download report | 1 req/min |

## Sales by Regions

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v1/analytics/region-sale` | Sales by regions (max 31 days) | 1 req/10s, burst 5 |

## Brand Share in Sales

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v1/analytics/brand-share/brands` | Seller's brands (sold in last 90 days) | 1 req/min |
| GET | `/api/v1/analytics/brand-share/parent-subjects` | Parent categories for a brand (from Nov 2022, up to 365 days) | 1 req/5s, burst 20 |
| GET | `/api/v1/analytics/brand-share` | Brand's share in sales (from Nov 2022, up to 365 days) | 1 req/5s, burst 20 |

## Hidden Products

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v1/analytics/banned-products/blocked` | Blocked product cards | 1 req/10s, burst 6 |
| GET | `/api/v1/analytics/banned-products/shadowed` | Products hidden from catalog | 1 req/10s, burst 6 |

## Goods Return Report

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v1/analytics/goods-return` | Goods returns to seller (max 31 days) | 1 req/min |

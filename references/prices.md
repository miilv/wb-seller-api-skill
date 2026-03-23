# Prices and Discounts API

Base URL: `https://discounts-prices-api.wildberries.ru`
Sandbox: `https://discounts-prices-api-sandbox.wildberries.ru`
Token category: **Prices and Discounts**
Default rate limit: 10 req/6s, 600ms interval, burst 5

## Setting Prices

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v2/upload/task` | Set prices and discounts (max 1000 products) |
| POST | `/api/v2/upload/task/size` | Set different prices per size |
| POST | `/api/v2/upload/task/club-discount` | Set WB Club subscription discounts (max 1000) |

## Upload Status

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v2/history/tasks` | Processed upload state data |
| GET | `/api/v2/history/goods/task` | Products in processed upload with errors |
| GET | `/api/v2/buffer/tasks` | Processing (unprocessed) upload state data |
| GET | `/api/v2/buffer/goods/task` | Products in processing upload with errors |

## Querying Prices

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v2/list/goods/filter` | Product data with prices (single article or paginated) |
| POST | `/api/v2/list/goods/filter` | Product data with prices by multiple articles |
| GET | `/api/v2/list/goods/size/nm` | Product sizes data with prices |
| GET | `/api/v2/quarantine/goods` | Products in price quarantine |

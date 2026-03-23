# Finance and Documents APIs

## Balance

Base URL: `https://finance-api.wildberries.ru`
Token category: **Finance**
Rate limit: 1 req/min, burst 1

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/account/balance` | Seller's balance (current balance, available for withdrawal) |

## Financial Reports

Base URL: `https://statistics-api.wildberries.ru`
Token category: **Statistics**
Rate limit: 1 req/min, burst 1

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v5/supplier/reportDetailByPeriod` | Detailed realization (sales) report for a period |

## Documents

Base URL: `https://documents-api.wildberries.ru`
Token category: **Documents**
Rate limit: 1 req/10s, burst 5

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/documents/categories` | Document categories |
| GET | `/api/v1/documents/list` | Seller's documents with filtering and sorting |
| GET | `/api/v1/documents/download` | Download single document by service name and extension |
| POST | `/api/v1/documents/download/all` | Download multiple documents (up to 50). Rate: 1 req/5min |

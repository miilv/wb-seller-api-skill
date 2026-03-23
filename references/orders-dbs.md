# DBS Orders API (Delivery by Seller)

Base URL: `https://marketplace-api.wildberries.ru`
Token category: **Marketplace**
Default rate limit: 300 req/min, 200ms interval, burst 20. A 409 response counts as 10 requests.

## Assembly Orders

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v3/dbs/orders/new` | List all new DBS orders | 300 req/min |
| GET | `/api/v3/dbs/orders` | Completed orders (canceled/sold, up to 30 days) | 300 req/min |
| POST | `/api/v3/dbs/groups/info` | Paid delivery info for orders in one buyer transaction | 300 req/min |
| POST | `/api/v3/dbs/orders/client` | Buyer information by order ID | 300 req/min |
| POST | `/api/marketplace/v3/dbs/orders/b2b/info` | B2B buyer data (INN, KPP, company) | 300 req/min |
| POST | `/api/v3/dbs/orders/delivery-date` | Delivery date/time selected by buyer | 300 req/min |
| POST | `/api/marketplace/v3/dbs/orders/status/info` | Order statuses by list of IDs | 300 req/min |

## Status Transitions

Rate limit: 1 req/s, 1s interval, burst 10

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/marketplace/v3/dbs/orders/status/cancel` | Cancel orders (new/confirm/deliver -> cancel) |
| POST | `/api/marketplace/v3/dbs/orders/status/confirm` | Move to confirm (on assembly) |
| POST | `/api/marketplace/v3/dbs/orders/status/deliver` | Move to deliver (on delivery) |
| POST | `/api/marketplace/v3/dbs/orders/status/receive` | Move to receive (buyer received) |
| POST | `/api/marketplace/v3/dbs/orders/status/reject` | Move to reject (buyer declined) |

## Metadata

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| POST | `/api/marketplace/v3/dbs/orders/meta/info` | Get order metadata | 150 req/min, 400ms interval |
| POST | `/api/marketplace/v3/dbs/orders/meta/delete` | Delete metadata by key | 150 req/min |
| POST | `/api/marketplace/v3/dbs/orders/meta/sgtin` | Add Data Matrix codes | 500 req/min, 120ms interval |
| POST | `/api/marketplace/v3/dbs/orders/meta/uin` | Add UIN | 500 req/min |
| POST | `/api/marketplace/v3/dbs/orders/meta/imei` | Add IMEI | 500 req/min |
| POST | `/api/marketplace/v3/dbs/orders/meta/gtin` | Add GTIN (Belarus) | 500 req/min |
| POST | `/api/marketplace/v3/dbs/orders/meta/customs-declaration` | Add customs declaration number | 500 req/min |

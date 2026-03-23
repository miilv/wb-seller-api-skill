# In-Store Pickup Orders API

Base URL: `https://marketplace-api.wildberries.ru`
Token category: **Marketplace**
Default rate limit: 300 req/min, 200ms interval, burst 20. A 409 response counts as 10 requests.

## Assembly Orders

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v3/click-collect/orders/new` | List all new pickup orders | 300 req/min |
| GET | `/api/v3/click-collect/orders` | Completed orders (sold/canceled, up to 30 days) | 300 req/min |
| POST | `/api/v3/click-collect/orders/status` | Order statuses by list of IDs | 300 req/min |
| POST | `/api/v3/click-collect/orders/client` | Buyer info by order ID | 300 req/min |
| POST | `/api/v3/click-collect/orders/client/identity` | Verify order belongs to buyer by code | 30 req/min, 2s interval |

## Status Transitions

Rate limit: 100 req/min, 600ms interval, burst 20

| Method | Path | Description |
|--------|------|-------------|
| PATCH | `/api/v3/click-collect/orders/{orderId}/confirm` | Move to confirm (on assembly) |
| PATCH | `/api/v3/click-collect/orders/{orderId}/prepare` | Move to prepare (ready for pickup) |
| PATCH | `/api/v3/click-collect/orders/{orderId}/receive` | Move to receive (buyer picked up) |
| PATCH | `/api/v3/click-collect/orders/{orderId}/reject` | Move to reject (buyer refusal) |
| PATCH | `/api/v3/click-collect/orders/{orderId}/cancel` | Cancel order |

## Metadata

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v3/click-collect/orders/{orderId}/meta` | Get order metadata | 300 req/min |
| DELETE | `/api/v3/click-collect/orders/{orderId}/meta` | Delete metadata by key | 300 req/min |
| PUT | `/api/v3/click-collect/orders/{orderId}/meta/sgtin` | Set Data Matrix code | 1000 req/min, 60ms interval |
| PUT | `/api/v3/click-collect/orders/{orderId}/meta/uin` | Set UIN | 1000 req/min |
| PUT | `/api/v3/click-collect/orders/{orderId}/meta/imei` | Set IMEI | 1000 req/min |
| PUT | `/api/v3/click-collect/orders/{orderId}/meta/gtin` | Set GTIN (Belarus) | 1000 req/min |

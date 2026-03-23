# FBS Orders API (Fulfillment by Seller)

Base URL: `https://marketplace-api.wildberries.ru`
Token category: **Marketplace**
Default rate limit: 300 req/min, 200ms interval, burst 20. A 409 response counts as 10 requests.

## Assembly Orders

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v3/orders/new` | List all new assembly orders | 300 req/min |
| GET | `/api/v3/orders` | Orders info (paginated, max 30 days) | 300 req/min |
| POST | `/api/v3/orders/status` | Order statuses by list of IDs | 300 req/min |
| GET | `/api/v3/supplies/orders/reshipment` | Orders requiring re-shipment | 300 req/min |
| PATCH | `/api/v3/orders/{orderId}/cancel` | Cancel an order | 100 req/min, 600ms interval |
| POST | `/api/v3/orders/stickers` | Order stickers (svg/zpl/png, max 100) | 300 req/min |
| POST | `/api/v3/orders/stickers/cross-border` | Cross-border stickers (PDF, max 100) | 300 req/min |
| POST | `/api/v3/orders/status/history` | Status history for cross-border orders | 300 req/min |
| POST | `/api/v3/orders/client` | Client info (cross-border Turkey only) | 300 req/min |

## Order Metadata

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| POST | `/api/marketplace/v3/orders/meta` | Get metadata for orders (max 100) | 300 req/min |
| DELETE | `/api/v3/orders/{orderId}/meta` | Remove metadata by key | 300 req/min |
| PUT | `/api/v3/orders/{orderId}/meta/sgtin` | Set Data Matrix code (Chestny ZNAK) | 1000 req/min, 60ms interval |
| PUT | `/api/v3/orders/{orderId}/meta/uin` | Set UIN | 1000 req/min |
| PUT | `/api/v3/orders/{orderId}/meta/imei` | Set IMEI | 1000 req/min |
| PUT | `/api/v3/orders/{orderId}/meta/gtin` | Set GTIN (Belarus) | 1000 req/min |
| PUT | `/api/v3/orders/{orderId}/meta/expiration` | Set expiration date | 1000 req/min |
| PUT | `/api/marketplace/v3/orders/{orderId}/meta/customs-declaration` | Set customs declaration number | 1000 req/min |

## Supplies

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v3/supplies` | Create a new supply |
| GET | `/api/v3/supplies` | List supplies (paginated) |
| PATCH | `/api/marketplace/v3/supplies/{supplyId}/orders` | Add orders to supply (max 100) |
| GET | `/api/v3/supplies/{supplyId}` | Supply details |
| DELETE | `/api/v3/supplies/{supplyId}` | Delete supply (must be empty) |
| GET | `/api/marketplace/v3/supplies/{supplyId}/order-ids` | Order IDs in a supply |
| PATCH | `/api/v3/supplies/{supplyId}/deliver` | Close supply, move orders to delivery |
| GET | `/api/v3/supplies/{supplyId}/barcode` | Supply QR code (after delivery) |
| GET | `/api/v3/supplies/{supplyId}/trbx` | List boxes in supply |
| POST | `/api/v3/supplies/{supplyId}/trbx` | Add boxes to supply |
| DELETE | `/api/v3/supplies/{supplyId}/trbx` | Delete boxes from supply |
| POST | `/api/v3/supplies/{supplyId}/trbx/stickers` | Box QR-code stickers |

## Passes

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/api/v3/passes/offices` | Offices requiring a pass | 300 req/min |
| GET | `/api/v3/passes` | List seller's passes | 300 req/min |
| POST | `/api/v3/passes` | Create a pass (valid 48h) | 1 req/10min |
| PUT | `/api/v3/passes/{passId}` | Update a pass | 300 req/min |
| DELETE | `/api/v3/passes/{passId}` | Delete a pass | 300 req/min |

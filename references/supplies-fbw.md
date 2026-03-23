# FBW Supplies API (Fulfillment by Wildberries)

Base URL: `https://supplies-api.wildberries.ru`
Token category: **Supplies**

## Information for Forming Supplies

Rate limit: 6 req/min, 10s interval, burst 6

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/acceptance/options` | Warehouses and package types available for supply by barcodes |
| GET | `/api/v1/warehouses` | List of Wildberries warehouses |
| GET | `/api/v1/transit-tariffs` | Available transit directions between warehouses. Burst 10 |
| GET | `/api/v1/acceptance/coefficients` | **DEPRECATED** -- Acceptance coefficients (moving to Tariffs) |

## Supplies Information

Rate limit: 30 req/min, 2s interval, burst 10

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/supplies` | List supplies (default last 1000, with filtering) |
| GET | `/api/v1/supplies/{ID}` | Supply details by supply or order ID |
| GET | `/api/v1/supplies/{ID}/goods` | Products in a supply |
| GET | `/api/v1/supplies/{ID}/package` | Package info for a supply |

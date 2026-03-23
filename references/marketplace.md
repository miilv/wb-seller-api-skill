# Marketplace API (Warehouses & Inventory)

Base URL: `https://marketplace-api.wildberries.ru`
Token category: **Marketplace**
Default rate limit: 300 req/min, 200ms interval, burst 20. A 409 response counts as 10 requests.

## Seller Warehouses

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v3/offices` | List all offices to link to a seller warehouse |
| GET | `/api/v3/warehouses` | List all seller's warehouses |
| POST | `/api/v3/warehouses` | Create a seller's warehouse |
| PUT | `/api/v3/warehouses/{warehouseId}` | Update warehouse details (office change 1x/day) |
| DELETE | `/api/v3/warehouses/{warehouseId}` | Delete a seller's warehouse |
| GET | `/api/v3/dbw/warehouses/{warehouseId}/contacts` | Contacts for a DBW seller warehouse |
| PUT | `/api/v3/dbw/warehouses/{warehouseId}/contacts` | Update DBW warehouse contacts (max 5) |

## Inventory

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| PUT | `/api/v3/stocks/{warehouseId}` | Update inventory (max 1000 SKUs) | 300 req/min |
| DELETE | `/api/v3/stocks/{warehouseId}` | Delete inventory (irreversible) | 10 req/min, 6s interval, burst 2 |
| POST | `/api/v3/stocks/{warehouseId}` | Get inventory for given SKUs/chrtIds | 300 req/min |

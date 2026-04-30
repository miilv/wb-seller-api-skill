# FBW Supplies — Fulfillment by WB

_Поставки FBW_

**Source:** [`swagger/07-orders-fbw.yaml`](../swagger/07-orders-fbw.yaml)

**7 endpoints** across 2 tag(s).

## Информация для формирования поставок

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v1/acceptance/options` | Опции приёмки |
| `GET` | `/api/v1/warehouses` | Список складов |
| `GET` | `/api/v1/transit-tariffs` | Транзитные направления |

## Информация о поставках

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v1/supplies` | Список поставок |
| `GET` | `/api/v1/supplies/{ID}` | Детали поставки |
| `GET` | `/api/v1/supplies/{ID}/goods` | Товары поставки |
| `GET` | `/api/v1/supplies/{ID}/package` | Упаковка поставки |


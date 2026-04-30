# DBW Orders — Delivery by Wildberries

_Заказы DBW_

**Source:** [`swagger/04-orders-dbw.yaml`](../swagger/04-orders-dbw.yaml)

**17 endpoints** across 2 tag(s).

## Метаданные DBW

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/marketplace/v3/dbw/orders/meta/details` | Получить метаданные сборочных заданий |
| `GET` | `/api/v3/dbw/orders/{orderId}/meta` | Получить метаданные сборочного задания |
| `DELETE` | `/api/v3/dbw/orders/{orderId}/meta` | Удалить метаданные сборочного задания |
| `PUT` | `/api/v3/dbw/orders/{orderId}/meta/sgtin` | Закрепить за сборочным заданием код маркировки Честного знака |
| `PUT` | `/api/v3/dbw/orders/{orderId}/meta/uin` | Закрепить за сборочным заданием УИН (уникальный идентификационный номер) |
| `PUT` | `/api/v3/dbw/orders/{orderId}/meta/imei` | Закрепить за сборочным заданием IMEI |
| `PUT` | `/api/v3/dbw/orders/{orderId}/meta/gtin` | Закрепить за сборочным заданием GTIN |

## Сборочные задания DBW

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v3/dbw/orders/new` | Получить список новых сборочных заданий |
| `GET` | `/api/v3/dbw/orders` | Получить информацию о завершенных сборочных заданиях |
| `POST` | `/api/v3/dbw/orders/delivery-date` | Дата и время доставки |
| `POST` | `/api/marketplace/v3/dbw/orders/client` | Информация о покупателе |
| `POST` | `/api/v3/dbw/orders/status` | Получить статусы сборочных заданий |
| `PATCH` | `/api/v3/dbw/orders/{orderId}/confirm` | Перевести на сборку |
| `POST` | `/api/v3/dbw/orders/stickers` | Получить стикеры сборочных заданий |
| `PATCH` | `/api/v3/dbw/orders/{orderId}/assemble` | Перевести в доставку |
| `POST` | `/api/v3/dbw/orders/courier` | Информация о курьере |
| `PATCH` | `/api/v3/dbw/orders/{orderId}/cancel` | Отменить сборочное задание |


# FBS Orders — Fulfillment by Seller

_Заказы FBS_

**Source:** [`swagger/03-orders-fbs.yaml`](../swagger/03-orders-fbs.yaml)

**35 endpoints** across 4 tag(s).

## Метаданные FBS

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/marketplace/v3/orders/meta` | Получить метаданные сборочных заданий |
| `DELETE` | `/api/v3/orders/{orderId}/meta` | Удалить метаданные сборочного задания |
| `PUT` | `/api/v3/orders/{orderId}/meta/sgtin` | Закрепить за сборочным заданием код маркировки Честного знака |
| `PUT` | `/api/v3/orders/{orderId}/meta/uin` | Закрепить за сборочным заданием УИН |
| `PUT` | `/api/v3/orders/{orderId}/meta/imei` | Закрепить за сборочным заданием IMEI |
| `PUT` | `/api/v3/orders/{orderId}/meta/gtin` | Закрепить за сборочным заданием GTIN |
| `PUT` | `/api/v3/orders/{orderId}/meta/expiration` | Закрепить за сборочным заданием срок годности товара |
| `PUT` | `/api/marketplace/v3/orders/{orderId}/meta/customs-declaration` | Закрепить за сборочным заданием номер ГТД |

## Поставки FBS

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v3/supplies` | Создать новую поставку |
| `GET` | `/api/v3/supplies` | Получить список поставок |
| `PATCH` | `/api/marketplace/v3/supplies/{supplyId}/orders` | Добавить сборочные задания к поставке |
| `GET` | `/api/v3/supplies/{supplyId}` | Получить информацию о поставке |
| `DELETE` | `/api/v3/supplies/{supplyId}` | Удалить поставку |
| `GET` | `/api/marketplace/v3/supplies/{supplyId}/order-ids` | Получить ID сборочных заданий поставки |
| `PATCH` | `/api/v3/supplies/{supplyId}/deliver` | Передать поставку в доставку |
| `GET` | `/api/v3/supplies/{supplyId}/barcode` | Получить QR-код поставки |
| `GET` | `/api/v3/supplies/{supplyId}/trbx` | Получить список грузомест поставки |
| `POST` | `/api/v3/supplies/{supplyId}/trbx` | Добавить грузоместа к поставке |
| `DELETE` | `/api/v3/supplies/{supplyId}/trbx` | Удалить грузоместа из поставки |
| `POST` | `/api/v3/supplies/{supplyId}/trbx/stickers` | Получить стикеры грузомест поставки |

## Пропуска FBS

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v3/passes/offices` | Получить список складов, для которых требуется пропуск |
| `GET` | `/api/v3/passes` | Получить список пропусков |
| `POST` | `/api/v3/passes` | Создать пропуск |
| `PUT` | `/api/v3/passes/{passId}` | Обновить пропуск |
| `DELETE` | `/api/v3/passes/{passId}` | Удалить пропуск |

## Сборочные задания FBS

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v3/orders/new` | Получить список новых сборочных заданий |
| `GET` | `/api/v3/orders` | Получить информацию о сборочных заданиях |
| `POST` | `/api/v3/orders/status` | Получить статусы сборочных заданий |
| `GET` | `/api/v3/supplies/orders/reshipment` | Получить все сборочные задания для повторной отгрузки |
| `PATCH` | `/api/v3/orders/{orderId}/cancel` | Отменить сборочное задание |
| `POST` | `/api/v3/orders/stickers` | Получить стикеры сборочных заданий |
| `POST` | `/api/v3/orders/stickers/cross-border` | Получить стикеры сборочных заданий трансграничных поставок |
| `POST` | `/api/v3/orders/status/history` | История статусов для сборочных заданий трансграничных поставок |
| `POST` | `/api/v3/orders/client` | Заказы с информацией по клиенту |
| `GET` | `/api/marketplace/v3/fbs/orders/archive` | Получить список архивных сборочных заданий |


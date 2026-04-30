# DBS Orders — Delivery by Seller

_Заказы DBS_

**Source:** [`swagger/05-orders-dbs.yaml`](../swagger/05-orders-dbs.yaml)

**21 endpoints** across 2 tag(s).

## Метаданные DBS

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/marketplace/v3/dbs/orders/meta/details` | Получить метаданные сборочных заданий |
| `POST` | `/api/marketplace/v3/dbs/orders/meta/info` | Получить метаданные сборочных заданий |
| `POST` | `/api/marketplace/v3/dbs/orders/meta/delete` | Удалить метаданные сборочных заданий |
| `POST` | `/api/marketplace/v3/dbs/orders/meta/sgtin` | Закрепить коды маркировки Честного знака за сборочными заданиями |
| `POST` | `/api/marketplace/v3/dbs/orders/meta/uin` | Закрепить УИН за сборочными заданиями |
| `POST` | `/api/marketplace/v3/dbs/orders/meta/imei` | Закрепить IMEI за сборочными заданиями |
| `POST` | `/api/marketplace/v3/dbs/orders/meta/gtin` | Закрепить GTIN за сборочными заданиями |
| `POST` | `/api/marketplace/v3/dbs/orders/meta/customs-declaration` | Закрепить за сборочными заданиями номер ГТД |

## Сборочные задания DBS

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v3/dbs/orders/new` | Получить список новых сборочных заданий |
| `GET` | `/api/v3/dbs/orders` | Получить информацию о завершенных сборочных заданиях |
| `POST` | `/api/v3/dbs/groups/info` | Получить информацию о платной доставке |
| `POST` | `/api/v3/dbs/orders/client` | Информация о покупателе |
| `POST` | `/api/marketplace/v3/dbs/orders/b2b/info` | Информация о покупателе B2B |
| `POST` | `/api/v3/dbs/orders/delivery-date` | Дата и время доставки |
| `POST` | `/api/marketplace/v3/dbs/orders/status/info` | Получить статусы сборочных заданий |
| `POST` | `/api/marketplace/v3/dbs/orders/status/cancel` | Отменить сборочные задания |
| `POST` | `/api/marketplace/v3/dbs/orders/status/confirm` | Перевести сборочные задания на сборку |
| `POST` | `/api/marketplace/v3/dbs/orders/stickers` | Получить стикеры для сборочных заданий с доставкой в ПВЗ |
| `POST` | `/api/marketplace/v3/dbs/orders/status/deliver` | Перевести сборочные задания в доставку |
| `POST` | `/api/marketplace/v3/dbs/orders/status/receive` | Сообщить о получении заказов |
| `POST` | `/api/marketplace/v3/dbs/orders/status/reject` | Сообщить об отказе от заказов |


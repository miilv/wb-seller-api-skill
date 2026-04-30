# In-Store Pickup Orders

_Заказы Самовывоз_

**Source:** [`swagger/06-in-store-pickup.yaml`](../swagger/06-in-store-pickup.yaml)

**Server(s):** `https://marketplace-api.wildberries.ru`

**28 endpoints** across 2 tag(s).

## Метаданные Самовывоз

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/marketplace/v3/click-collect/orders/meta/info` | Получить метаданные сборочных заданий |
| `POST` | `/api/marketplace/v3/click-collect/orders/meta/delete` | Удалить метаданные сборочных заданий |
| `POST` | `/api/marketplace/v3/click-collect/orders/meta/sgtin` | Закрепить коды маркировки Честного знака за сборочными заданиями |
| `POST` | `/api/marketplace/v3/click-collect/orders/meta/uin` | Закрепить УИН за сборочными заданиями |
| `POST` | `/api/marketplace/v3/click-collect/orders/meta/imei` | Закрепить IMEI за сборочными заданиями |
| `POST` | `/api/marketplace/v3/click-collect/orders/meta/gtin` | Закрепить GTIN за сборочными заданиями |
| `GET` | `/api/v3/click-collect/orders/{orderId}/meta` | Получить метаданные сборочного задания |
| `DELETE` | `/api/v3/click-collect/orders/{orderId}/meta` | Удалить метаданные сборочного задания |
| `PUT` | `/api/v3/click-collect/orders/{orderId}/meta/sgtin` | Закрепить за сборочным заданием код маркировки товара |
| `PUT` | `/api/v3/click-collect/orders/{orderId}/meta/uin` | Закрепить за сборочным заданием УИН (уникальный идентификационный номер) |
| `PUT` | `/api/v3/click-collect/orders/{orderId}/meta/imei` | Закрепить за сборочным заданием IMEI |
| `PUT` | `/api/v3/click-collect/orders/{orderId}/meta/gtin` | Закрепить за сборочным заданием GTIN |

## Сборочные задания Самовывоз

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v3/click-collect/orders/new` | Получить список новых сборочных заданий |
| `POST` | `/api/marketplace/v3/click-collect/orders/status/confirm` | Перевести сборочные задания на сборку |
| `POST` | `/api/marketplace/v3/click-collect/orders/status/prepare` | Сообщить, что сборочные задания готовы к выдаче |
| `PATCH` | `/api/v3/click-collect/orders/{orderId}/confirm` | Перевести на сборку |
| `PATCH` | `/api/v3/click-collect/orders/{orderId}/prepare` | Сообщить, что сборочное задание готово к выдаче |
| `POST` | `/api/v3/click-collect/orders/client` | Информация о покупателе |
| `POST` | `/api/v3/click-collect/orders/client/identity` | Проверить, что заказ принадлежит покупателю |
| `POST` | `/api/marketplace/v3/click-collect/orders/status/receive` | Сообщить, что заказы приняты покупателями |
| `POST` | `/api/marketplace/v3/click-collect/orders/status/reject` | Сообщить об отказе от заказов |
| `PATCH` | `/api/v3/click-collect/orders/{orderId}/receive` | Сообщить, что заказ принят покупателем |
| `PATCH` | `/api/v3/click-collect/orders/{orderId}/reject` | Сообщить, что покупатель отказался от заказа |
| `POST` | `/api/marketplace/v3/click-collect/orders/status/info` | Получить статусы сборочных заданий |
| `POST` | `/api/v3/click-collect/orders/status` | Получить статусы сборочных заданий |
| `GET` | `/api/v3/click-collect/orders` | Получить информацию о завершённых сборочных заданиях |
| `POST` | `/api/marketplace/v3/click-collect/orders/status/cancel` | Отменить сборочные задания |
| `PATCH` | `/api/v3/click-collect/orders/{orderId}/cancel` | Отменить сборочное задание |


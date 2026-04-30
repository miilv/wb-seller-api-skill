# Заказы Самовывоз

**Server(s):** `https://marketplace-api.wildberries.ru`

Управление [сборочными заданиями](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) и [метаданными](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz) заказов модели Самовывоз.

## Метаданные Самовывоз

### `POST /api/marketplace/v3/click-collect/orders/meta/info`

**Получить метаданные сборочных заданий**

Метод возвращает метаданные [сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz).

Перечень метаданных, доступных для сборочного задания, можно получить в [списке новых сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1v3~1click-collect~1orders~1new/get), поле `requiredMeta`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов получения и удаления метаданных Самовыво...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `meta` (array[object]) **(required)** — Метаданные сборочных заданий
  - `error` (string) **(required)** — Сообщение об ошибке.   - `""` — нет ошибок - `NotFound` — сборочное задание не найдено
  - `gtin` (string) — GTIN
  - `imei` (string) — IMEI
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `sgtin` (array[string]) — Код маркировки [Честного знака](https://честныйзнак.рф/)
  - `uin` (string) — УИН

---

### `POST /api/marketplace/v3/click-collect/orders/meta/delete`

**Удалить метаданные сборочных заданий**

Метод удаляет значения указанных [метаданных](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) для нескольких сборочных заданий.

Одним запросом можно удалить метаданные только одного типа: `imei`, `uin`, `gtin` или `sgtin`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов получения и удаления метаданных Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| ---...

**Request body:**

- `key` (string) **(required)** — Тип метаданных для удаления (`imei`, `uin`, `gtin`, `sgtin`). Передаётся только одно значение
- `ordersIds` (array[integer]) **(required)** — Список ID сборочных заданий

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `POST /api/marketplace/v3/click-collect/orders/meta/sgtin`

**Закрепить коды маркировки Честного знака за сборочными заданиями**

Метод обновляет код маркировки [Честного знака](https://честныйзнак.рф/) в [метаданных](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) нескольких сборочных заданий.

Закрепить код маркировки Честного знака можно, только если в [метаданных сборочного задания](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) есть поле `sgtin`, а сборочное задание находится...

**Request body:**

- `orders` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `sgtins` (array[string]) **(required)** — Массив кодов маркировки. Допускается от 16 до 135 символов для кода одной маркировки

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `POST /api/marketplace/v3/click-collect/orders/meta/uin`

**Закрепить УИН за сборочными заданиями**

Метод обновляет УИН, уникальные идентификационные номера, в [метаданных сборочных заданий](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post). У одного сборочного задания может быть
только один УИН. Добавлять УИН можно только для сборочных заданий в [статусе](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
`confirm` и доставка которых осуществляе...

**Request body:**

- `orders` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `uin` (string) **(required)** — УИН

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `POST /api/marketplace/v3/click-collect/orders/meta/imei`

**Закрепить IMEI за сборочными заданиями**

Метод обновляет IMEI в [метаданных сборочных заданий](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post). У одного сборочного задания может
быть только один IMEI. Добавлять IMEI можно только для сборочных заданий в
[статусе](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm`, если их доставка осуществляется силами WB.

[Лимит запросов](/op...

**Request body:**

- `orders` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `imei` (string) **(required)** — IMEI

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `POST /api/marketplace/v3/click-collect/orders/meta/gtin`

**Закрепить GTIN за сборочными заданиями**

Метод обновляет GTIN, уникальный ID товара в Беларуси, в [метаданных](/openapi/in-store-pickup#tag/Metadannye-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post) нескольких сборочных
заданий. У одного сборочного задания может быть только один GTIN.
Добавлять GTIN можно только для сборочных заданий в [статусе](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm` и
доставка которых о...

**Request body:**

- `orders` (array[object]) **(required)**
  - `gtin` (string) **(required)** — GTIN
  - `orderId` (integer) **(required)** — ID сборочного задания

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `GET /api/v3/click-collect/orders/{orderId}/meta`

**Получить метаданные сборочного задания**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов закрепления метаданных Самовывоз:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 300 запросов | 200 мс | 20 запросов |
| Сервисный | 1 мин | 300 запросов | 200 мс | 20 запросов |
| Базовый | 1 ч | 10 запросов | 6 мин | 1 запрос |

О...

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Response 200:**

- `meta` (object) — Метаданные сборочного задания

---

### `DELETE /api/v3/click-collect/orders/{orderId}/meta`

**Удалить метаданные сборочного задания**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания
- `key` (in query, string) **(required)** — Название метаданных для удаления (`imei`, `uin`, `gtin`, `sgtin`). Передается только одно значение.

---

### `PUT /api/v3/click-collect/orders/{orderId}/meta/sgtin`

**Закрепить за сборочным заданием код маркировки товара**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Request body:**

- `sgtins` (array[string]) — Массив кодов маркировки. Допускается от 16 до 135 символов для кода одной маркировки

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `PUT /api/v3/click-collect/orders/{orderId}/meta/uin`

**Закрепить за сборочным заданием УИН (уникальный идентификационный номер)**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов закрепления метаданных Самовывоз:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1000 запросов | 60 мс | 20 запросов |
| Сервисный | 1 мин | 1000 запросов | 60 мс | 20 запросов |
| Базовый | 1 ч | 10 запросов | 6 мин | 1 запрос |

О...

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Request body:**

- `uin` (string) — УИН

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `PUT /api/v3/click-collect/orders/{orderId}/meta/imei`

**Закрепить за сборочным заданием IMEI**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Request body:**

- `imei` (string) — IMEI

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `PUT /api/v3/click-collect/orders/{orderId}/meta/gtin`

**Закрепить за сборочным заданием GTIN**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Request body:**

- `gtin` (string) — GTIN

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

## Сборочные задания Самовывоз

### `GET /api/v3/click-collect/orders/new`

**Получить список новых сборочных заданий**

Метод возвращает список всех новых [сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz), которые есть у продавца на момент запроса.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Response 200:**

- `orders` (array[object]) — Список сборочных заданий
  - `ddate` (string) — Планируемая дата доставки
  - `salePrice` (integer) — Цена продавца в валюте продажи с учётом скидки продавца, без учёта скидки WB Клуба, умноженная на 100. Предоставляется в информационных целях
  - `requiredMeta` (array[string]) — Список метаданных, доступных для сборочного задания
  - `article` (string) — Артикул продавца
  - `rid` (string) — Уникальный ID заказа.   Примечание: поле `rid` — это поле `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvr
  - `createdAt` (string(date-time)) — Дата и время создания сборочного задания
  - `warehouseAddress` (string) — Адрес магазина (склада продавца), на который поступило сборочное задание
  - `orderCode` (string) — Уникальный ID заказа покупателя
  - `payMode` (string) — Режим оплаты:   - `prepaid` — предоплатный   - `postpaid` — постоплатный   - `unknown` — неизвестный
  - `skus` (array[string]) — Массив баркодов товара
  - `id` (integer) — ID сборочного задания
  - `warehouseId` (integer) — ID склада продавца, на который поступило сборочное задание
  - `nmId` (integer) — Артикул WB
  - `chrtId` (integer) — ID размера товара в системе WB
  - `price` (integer) — Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предостав
  - `finalPrice` (integer) — Сумма к оплате покупателем в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предоставляется 
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. П
  - `convertedFinalPrice` (integer) — Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк

---

### `POST /api/marketplace/v3/click-collect/orders/status/confirm`

**Перевести сборочные задания на сборку**

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `new` — новый — в статус `confirm` — на сборке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 се...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `POST /api/marketplace/v3/click-collect/orders/status/prepare`

**Сообщить, что сборочные задания готовы к выдаче**

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `confirm` — на сборке — в статус `prepare` — готово к выдаче.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- ...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `PATCH /api/v3/click-collect/orders/{orderId}/confirm`

**Перевести на сборку**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `PATCH /api/v3/click-collect/orders/{orderId}/prepare`

**Сообщить, что сборочное задание готово к выдаче**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `POST /api/v3/click-collect/orders/client`

**Информация о покупателе**

Метод возвращает информацию о покупателе по ID сборочного задания.

Доступно только для сборочных заданий в статусах:
  - `confirm` — на сборке
  - `prepare` — готов к выдаче

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object])
  - `phone` (string) — Телефон для связи с покупателем. Чтобы связаться с покупателем наберите этот номер и введите добавочный код. Данный номер не является прямым номером п
  - `firstName` (string) — Имя покупателя
  - `orderID` (integer) — ID сборочного задания
  - `phoneCode` (integer) — Добавочный код

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `POST /api/v3/click-collect/orders/client/identity`

**Проверить, что заказ принадлежит покупателю**

Метод сообщает, принадлежит ли проверяемый заказ покупателю или нет по переданному коду.

Доступно, если хотя бы одно сборочное задание из заказа находится в статусе prepare - готов к выдаче.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 30 запросов | 2 сек | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Request body:**

- `orderCode` (string) — Уникальный ID заказа покупателя
- `passcode` (string) — Код подтверждения

**Response 200:**

- `ok` (boolean) — Принадлежит ли заказ покупателю:   - `true` — принадлежит   - `false` — значение не применяется. Если заказ не принадлежит покупателю, вы получите отв

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 404:**

- `code` (string)
- `data` (object)
- `message` (string)

**Response 409:**

- `code` (string)
- `data` (object)
- `message` (string)

---

### `POST /api/marketplace/v3/click-collect/orders/status/receive`

**Сообщить, что заказы приняты покупателями**

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `prepare` — готово к выдаче — в статус `receive` — получено покупателем.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- |...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `POST /api/marketplace/v3/click-collect/orders/status/reject`

**Сообщить об отказе от заказов**

Метод переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статуса](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `prepare` — готово к выдаче — в статус `reject` — отказ при получении.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- | -...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `PATCH /api/v3/click-collect/orders/{orderId}/receive`

**Сообщить, что заказ принят покупателем**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 100 запросов | 600 мс | 20 запросов |
| Сервисный | 1 мин | 100 запросов | 600 мс | 20 запросов |
| Базовый | 1 ч | 10 запросов | 6 мин | 1 запрос |

Один запрос...

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `PATCH /api/v3/click-collect/orders/{orderId}/reject`

**Сообщить, что покупатель отказался от заказа**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 100 запросов | 600 мс | 20 запросов |
| Сервисный | 1 мин | 100 запросов | 600 мс | 20 запросов |
| Базовый | 1 ч | 50 запросов | 72 сек | 1 запрос |

Один запро...

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `POST /api/marketplace/v3/click-collect/orders/status/info`

**Получить статусы сборочных заданий**

Метод возвращает статусы [сборочных заданий](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) по их ID.

`supplierStatus` — статус сборочного задания. Триггер его изменения - действие самого продавца.

Возможные значения `supplierStatus`:
| Статус   | Описание            | Как перевести сборочное задание в данный статус |
| -------  | ---------           | --------------------------------------|
| `new`      | **Новое сборочное задание** |
| `confirm`  | **На сборке**  | 	[Перевести с...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object]) — Информация о статусах
  - `errors` (array[object]) — Информация об ошибке
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `supplierStatus` (string) — Статус сборочного задания, установленный продавцом
  - `wbStatus` (string) — Статус сборочного задания в системе Wildberries

---

### `POST /api/v3/click-collect/orders/status`

**Получить статусы сборочных заданий**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object]) — Список статусов сборочных заданий
  - `id` (integer) — ID сборочного задания
  - `supplierStatus` (string) — Статус сборочного задания, установленный продавцом
  - `wbStatus` (string) — Статус сборочного задания в системе WB

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `GET /api/v3/click-collect/orders`

**Получить информацию о завершённых сборочных заданиях**

Метод возвращает информацию о завершённых сборочных заданиях после продажи или отмены заказа.

Можно получить данные за заданный период, максимум 30 календарных дней одним запросом.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `limit` (in query, integer) **(required)** — Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
- `next` (in query, integer) **(required)** — Параметр пагинации. Устанавливает значение, с которого необходимо получить следующий пакет данных. Для получения полного списка данных должен быть рав
- `dateFrom` (in query, integer) **(required)** — Дата начала периода в формате Unix timestamp
- `dateTo` (in query, integer) **(required)** — Дата конца периода в формате Unix timestamp

**Response 200:**

- `next` (integer) — Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения следующего пакета данных
- `orders` (array[object]) — Список сборочных заданий
  - `article` (string) — Артикул продавца
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `chrtId` (integer) — ID размера товара в системе WB
  - `createdAt` (string(date-time)) — Дата и время создания сборочного задания
  - `price` (integer) — Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предостав
  - `finalPrice` (integer) — Сумма к оплате покупателем в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предоставляется 
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. П
  - `convertedFinalPrice` (integer) — Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `id` (integer) — ID сборочного задания
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк
  - `nmId` (integer) — Артикул WB
  - `orderCode` (string) — Уникальный ID заказа покупателя
  - `payMode` (string) — Режим оплаты:   - `prepaid` — предоплатный   - `postpaid` — постоплатный   - `unknown` — неизвестный
  - `rid` (string) — Уникальный ID заказа.   Примечание: поле `rid` — это поле `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvr
  - `skus` (array[string]) — Массив баркодов товара
  - `warehouseAddress` (string) — Адрес магазина (склада продавца), на который поступило сборочное задание
  - `warehouseId` (integer) — ID склада продавца, на который поступило сборочное задание

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---

### `POST /api/marketplace/v3/click-collect/orders/status/cancel`

**Отменить сборочные задания**

Переводит [сборочные задания](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz) из [статусов](/openapi/in-store-pickup#tag/Sborochnye-zadaniya-Samovyvoz/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post) `new`, `confirm`, `prepare` в статус `cancel` — отменено продавцом.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | ---...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (object) **(required)** — Уникальный ID запроса
- `results` (array[object]) **(required)**
  - `orderId` (integer) **(required)** — ID сборочного задания
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `errors` (array[object]) — Детали ошибки

---

### `PATCH /api/v3/click-collect/orders/{orderId}/cancel`

**Отменить сборочное задание**

Данный метод устарел. Он будет удалён [19 мая](https://dev.wildberries.ru/release-notes?id=474)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий Самовывоз:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 100 запросов | 600 мс | 20 запросов |
| Сервисный | 1 мин | 100 запросов | 600 мс | 20 запросов |
| Базовый | 1 ч | 10 запросов | 6 мин | 1 запрос |

Один запрос...

**Parameters:**

- `orderId` (in path, integer) **(required)** — ID сборочного задания

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные, обогащающие ошибку

---


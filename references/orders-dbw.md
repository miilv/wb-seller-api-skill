# Заказы DBW

С помощью методов Заказы DBW (Доставка курьером WB) вы можете:
  - получать информацию о [сборочных заданиях](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW), управлять статусами и отменять сборочные задания
  - получать, добавлять, редактировать и удалять [метаданные](/openapi/orders-dbw#tag/Metadannye-DBW) сборочных заданий

  Узнать, как использовать методы в бизнес-кейсах, можно в [инструкции](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-036a-7721-98e8-bed5f1a4f72d/zakazy-dbw) по работе с заказами DBW

## Метаданные DBW

### `POST /api/marketplace/v3/dbw/orders/meta/details`

**Получить метаданные сборочных заданий**

Метод возвращает метаданные [сборочных заданий](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders/get) и статусы их валидации.

Перечень метаданных, доступных для сборочного задания, можно получить в [списке новых сборочных заданий](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1new/get), поле `requiredMeta`.

Возможные метаданные:
  - `imei` — [IMEI](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (string) **(required)** — Уникальный ID запроса
- `orders` (array[object]) — Метаданные сборочных заданий и статусы их валидации

**Response 400:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

**Response 403:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `GET /api/v3/dbw/orders/{orderId}/meta`

**Получить метаданные сборочного задания**

Данный метод устарел. Он будет удалён [27 июля](https://dev.wildberries.ru/release-notes?id=508)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `meta` (object)
  - `imei` (object) — IMEI
  - `uin` (object) — УИН
  - `gtin` (object) — GTIN
  - `sgtin` (object) — Код маркировки [Честного знака](https://честныйзнак.рф/)

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `DELETE /api/v3/dbw/orders/{orderId}/meta`

**Удалить метаданные сборочного задания**

Метод удаляет значение [метаданных сборочного задания](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get) для переданного ключа.

Возможные метаданные:
  - `imei` — [IMEI](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1imei/put)
  - `uin` — [УИН](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1uin/put)
  - `gtin` — [GTIN](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1a...

**Parameters:**

- `?` (in ?, )
- `key` (in query, string) — Название метаданных для удаления (`imei`, `uin`, `gtin`, `sgtin`). Передается только одно значение

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/dbw/orders/{orderId}/meta/sgtin`

**Закрепить за сборочным заданием код маркировки Честного знака**

Метод позволяет закрепить за сборочным заданием код маркировки [Честного знака](https://честныйзнак.рф/).

Закрепить код маркировки Честного знака можно только если в [метаданных сборочного задания](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get) есть поле `sgtin`, а сборочное задание находится в [статусе](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post) `confirm`.

Получить загруженные коды маркировки можно ...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `sgtins` (array[string]) — Массив кодов маркировки

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/dbw/orders/{orderId}/meta/uin`

**Закрепить за сборочным заданием УИН (уникальный идентификационный номер)**

Метод обновляет УИН в [метаданных сборочного задания](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get) — уникальный идентификационный номер.

У одного сборочного задания может быть только один УИН.

Добавлять маркировку можно только для заказов, которые находятся в [статусе](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post) `confirm`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на о...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `uin` (string) **(required)** — УИН

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/dbw/orders/{orderId}/meta/imei`

**Закрепить за сборочным заданием IMEI**

Метод обновляет IMEI в [метаданных сборочного задания](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get).

У одного сборочного задания может быть только один IMEI.

Добавлять маркировку можно только для заказов, которые находятся в [статусе](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post) `confirm`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех метод...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `imei` (string) **(required)** — IMEI

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/dbw/orders/{orderId}/meta/gtin`

**Закрепить за сборочным заданием GTIN**

Метод обновляет GTIN в [метаданных сборочного задания](/openapi/orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get) — уникальный ID товара в Беларуси.

У одного сборочного задания может быть только один GTIN.

Добавлять маркировку можно только для заказов, которые находятся в [статусе](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post) `confirm`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на од...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `gtin` (string) **(required)** — GTIN

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

## Сборочные задания DBW

### `GET /api/v3/dbw/orders/new`

**Получить список новых сборочных заданий**

Метод возвращает список всех новых [сборочных заданий](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW), которые есть у продавца на момент запроса.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

**Response 200:**

- `orders` (array[object]) — Список новых сборочных заданий
  - `address` (object) — Адрес покупателя для доставки
  - `salePrice` (integer) — Цена в валюте продажи с учетом скидки продавца, без учета скидки WB Клуба, умноженная на 100. Предоставляется в информационных целях
  - `requiredMeta` (array[string]) — Список метаданных, доступных для сборочного задания. [Указывать IMEI](./orders-dbw#tag/Metadannye-DBW/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1met
  - `comment` (string) — Комментарий покупателя
  - `options` (object) — Опции заказа
  - `orderUid` (string) — ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый `orderUid`
  - `groupId` (string(UUID)) — ID группы сборочных заданий.   Объединяет сборочные задания, поступившие на один склад (`warehouseId`) в рамках одной транзакции покупателя (`orderUid
  - `article` (string) — Артикул продавца
  - `colorCode` (string) — Код цвета (только для колеруемых товаров)
  - `rid` (string) — Уникальный ID заказа.   Примечание: `rid` — это `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvraty-pokupa
  - `createdAt` (string(date-time)) — Дата создания сборочного задания
  - `skus` (array[string]) — Массив баркодов товара
  - `id` (integer(int64)) — ID сборочного задания
  - `warehouseId` (integer) — ID склада продавца, на который поступило сборочное задание
  - `nmId` (integer) — Артикул WB
  - `chrtId` (integer) — ID размера товара в системе WB
  - `price` (integer) — Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предостав
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк

---

### `GET /api/v3/dbw/orders`

**Получить информацию о завершенных сборочных заданиях**

Метод возвращает информацию о завершенных [сборочных заданиях](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW).

Можно получить данные за заданный период, максимум 30 календарных дней одним запросом.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | -...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `dateFrom` (in query, integer) **(required)** — Дата начала периода в формате Unix timestamp
- `dateTo` (in query, integer) **(required)** — Дата конца периода в формате Unix timestamp

**Response 200:**

- `next` (object)
- `orders` (array[object])
  - `address` (object) — Адрес покупателя для доставки
  - `options` (object) — Опции заказа
  - `orderUid` (string) — ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый `orderUid`
  - `groupId` (string(UUID)) — ID группы сборочных заданий.   Объединяет сборочные задания, поступившие на один склад (`warehouseId`) в рамках одной транзакции покупателя (`orderUid
  - `article` (string) — Артикул продавца
  - `colorCode` (string) — Код цвета (только для колеруемых товаров)
  - `rid` (string) — Уникальный ID заказа.   Примечание: `rid` — это `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvraty-pokupa
  - `createdAt` (string(date-time)) — Дата создания сборочного задания
  - `skus` (array[string]) — Массив баркодов товара
  - `id` (integer(int64)) — ID сборочного задания
  - `warehouseId` (integer) — ID склада продавца, на который поступило сборочное задание
  - `nmId` (integer) — Артикул WB
  - `chrtId` (integer) — ID размера товара в системе WB
  - `price` (integer) — Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предостав
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `comment` (string) — Комментарий покупателя
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/dbw/orders/delivery-date`

**Дата и время доставки**

Метод возвращает информацию о выбранных покупателем дате и времени доставки сборочных заданий.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 за...

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/marketplace/v3/dbw/orders/client`

**Информация о покупателе**

Метод возвращает информацию о покупателях по ID сборочных заданий.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object]) — Информация о покупателях
  - `replacementPhone` (string) — Подменный номер для связи с покупателем.   Пустое значение `""` указывает, что номер ещё не назначен
  - `phone` (string) — Номер телефона для связи с покупателем:   - если в поле `phoneCode` не указан добавочный код, вы можете позвонить покупателю по указанному номеру. Доп
  - `firstName` (string) — Имя покупателя
  - `fullName` (string) — Полное имя покупателя, используется для оформления документов
  - `additionalPhones` (array[string]) — Дополнительные номера телефонов для связи с покупателем.   Используйте, чтобы позвонить покупателю, если недоступен основной номер из `phone`.   Пусто
  - `additionalPhoneCodes` (array[integer]) — Дополнительные добавочные коды.   Используйте, если не получилось дозвониться по добавочному коду из `phoneCode`.  Пустое значение указывает, коды ещё
  - `orderId` (integer) — ID сборочного задания
  - `phoneCode` (integer) — Добавочный код.   Используйте, чтобы связаться с покупателем по номеру из `phone`.  Если код не указан, вы можете связаться с покупателем без кода

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/dbw/orders/status`

**Получить статусы сборочных заданий**

Метод возвращает статусы сборочных заданий по их ID.

`supplierStatus` — статус сборочного задания.
Триггер его изменения — действие самого продавца.

Возможные значения `supplierStatus`:
| Статус   | Описание            | Как перевести сборочное задание в данный статус |
| -------  | ---------           | --------------------------------------|
| `new`      | **Новое сборочное задание** | |
| `confirm`  | **На сборке**      |  [Перевести сборочное задание на сборку](/openapi/orders-dbw#tag/Sbor...

**Request body:**

- `orders` (array[integer]) **(required)** — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PATCH /api/v3/dbw/orders/{orderId}/confirm`

**Перевести на сборку**

Метод переводит [сборочное задание](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW) в [статус](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post) `confirm` — на сборке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| --- | --- ...

**Parameters:**

- `?` (in ?, )

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/dbw/orders/stickers`

**Получить стикеры сборочных заданий**

Метод возвращает список стикеров для [сборочных заданий](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1new/get) в [статусах](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post):
  - `confirm` — на сборке
  - `complete` — в доставке

За один запрос можно получить максимум 100 стикеров.

Доступные форматы стикеров:
  - SVG
  - ZPLV (вертикальный)
  - ZPLH (горизонтальный)
  - PNG

Доступны размеры:
  - 580x400 px при `width=58&...

**Parameters:**

- `type` (in query, enum: svg, zplv, zplh, png) **(required)** — Тип стикера
- `width` (in query, enum: 58, 40) **(required)** — Ширина стикера
- `height` (in query, enum: 40, 30) **(required)** — Высота стикера

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `stickers` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PATCH /api/v3/dbw/orders/{orderId}/assemble`

**Перевести в доставку**

Метод переводит [сборочное задание](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders/get) в [статус](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post) `complete` — в доставке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит ...

**Parameters:**

- `?` (in ?, )

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/dbw/orders/courier`

**Информация о курьере**

Метод возвращает контактные данные и номер автомобиля курьера по ID сборочного задания. 
 Для сборочных заданий в статусах `confirm`, `complete`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object])
  - `courierInfo` (object) — Информация о курьере
  - `orderID` (integer) — ID сборочного задания

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PATCH /api/v3/dbw/orders/{orderId}/cancel`

**Отменить сборочное задание**

Метод отменяет [сборочное задание](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW) и переводит в [статус](/openapi/orders-dbw#tag/Sborochnye-zadaniya-DBW/paths/~1api~1v3~1dbw~1orders~1status/post) `cancel` — отменено продавцом.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    управление сборочными заданиями
 

| Тип | Период | Лимит | Интервал | ...

**Parameters:**

- `?` (in ?, )

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---


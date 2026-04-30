# Заказы DBS

Узнать больше о заказах DBS можно в [справочном центре](https://seller.wildberries.ru/instructions/category/6572e024-7428-4db1-86a8-a4c7dbebbfcf?goBackOption=prevRoute&categoryId=5a8e1202-0865-45b7-acae-5d0afc7add56)

Управление [сборочными заданиями](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) и [метаданными](/openapi/orders-dbs#tag/Metadannye-DBS) заказов DBS (Delivery by Seller).

## Метаданные DBS

### `POST /api/marketplace/v3/dbs/orders/meta/details`

**Получить метаданные сборочных заданий**

Метод возвращает метаданные [сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) и статусы их валидации. 

Перечень метаданных, доступных для сборочного задания, можно получить в [списке новых сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1v3~1dbs~1orders~1new/get), поле `requiredMeta`.

Возможные метаданные:
  - `imei` — [IMEI](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post)
  - `uin` — [УИН](/op...

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

### `POST /api/marketplace/v3/dbs/orders/meta/info`

**Получить метаданные сборочных заданий**

Данный метод устарел. Он будет удалён [27 июля](https://dev.wildberries.ru/release-notes?id=508)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов получения и удаления метаданных DBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 150 запросов | 400 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `meta` (array[object]) — Метаданные сборочных заданий
  - `error` (string) — Сообщение об ошибке.   Если `error: not found`, сборочное задание не найдено
  - `gtin` (string) — GTIN
  - `imei` (string) — IMEI
  - `orderId` (integer) — ID сборочного задания
  - `sgtin` (array[string]) — Код маркировки [Честного знака](https://честныйзнак.рф/)
  - `uin` (string) — УИН
  - `customsDeclaration` (object) — Номер грузовой таможенной декларации

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

### `POST /api/marketplace/v3/dbs/orders/meta/delete`

**Удалить метаданные сборочных заданий**

Метод удаляет значение указанных [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) для нескольких сборочных заданий.

В одном запросе можно удалить метаданные только одного типа. Укажите тип метаданных в запросе:
  - `imei` — [IMEI](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post)
  - `uin` — [УИН](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1...

**Request body:**

- `key` (string) **(required)** — Название метаданных для удаления (**imei**, **uin**, **gtin**, **sgtin**). Передаётся только одно значение
- `orderIds` (array[integer]) **(required)** — Список ID сборочных заданий

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

**Response 409:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `POST /api/marketplace/v3/dbs/orders/meta/sgtin`

**Закрепить коды маркировки Честного знака за сборочными заданиями**

Метод обновляет код маркировки [Честного знака](https://честныйзнак.рф/) в [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) нескольких сборочных заданий.

Закрепить код маркировки Честного знака можно, только если в [метаданных сборочного задания](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) есть поле `sgtin`, а сборочное задание находится в [статусе](/openapi/orders-dbs#tag/Sboro...

**Request body:**

- `orders` (array[object]) **(required)**
  - `orderId` (integer) — ID сборочного задания
  - `sgtins` (array[string]) — Массив кодов маркировки. Допускается от 16 до 135 символов для кода одной маркировки

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

**Response 409:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `POST /api/marketplace/v3/dbs/orders/meta/uin`

**Закрепить УИН за сборочными заданиями**

Метод обновляет УИН, уникальный идентификационный номер, в [метаданных сборочных заданий](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).

У одного сборочного задания может быть только один УИН.
Добавлять УИН можно только для сборочных заданий, которые доставляются WB и находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm`.

[Лимит запросов](/openapi/api-inf...

**Request body:**

- `orders` (array[object]) **(required)**
  - `orderId` (integer) — ID сборочного задания
  - `uin` (string) — УИН

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

**Response 409:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `POST /api/marketplace/v3/dbs/orders/meta/imei`

**Закрепить IMEI за сборочными заданиями**

Метод обновляет IMEI в [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) нескольких сборочных заданий.

У одного сборочного задания может быть только один IMEI.
Добавлять IMEI можно только для сборочных заданий, которые доставляются WB и находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/L...

**Request body:**

- `orders` (array[object]) **(required)**
  - `orderId` (integer) — ID сборочного задания
  - `imei` (string) — IMEI

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

**Response 409:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `POST /api/marketplace/v3/dbs/orders/meta/gtin`

**Закрепить GTIN за сборочными заданиями**

Метод обновляет GTIN, уникальный ID товара в Беларуси, в [метаданных](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post) нескольких сборочных заданий.

У одного сборочного задания может быть только один GTIN.
Добавлять GTIN можно только для сборочных заданий, которые доставляются WB и находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm`.

[Лимит запросов](/open...

**Request body:**

- `orders` (array[object]) **(required)**
  - `gtin` (string) — GTIN
  - `orderId` (integer) — ID сборочного задания

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

**Response 409:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `POST /api/marketplace/v3/dbs/orders/meta/customs-declaration`

**Закрепить за сборочными заданиями номер ГТД**

Метод обновляет номер ГТД — грузовой таможенной декларации — в [метаданных сборочных заданий](/openapi/orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).

У одного сборочного задания может быть только один ГТД.

Добавлять номер ГТД можно только для сборочных заданий, которые находятся в [статусе](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1v3~1dbs~1orders~1status/post) `deliver`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limi...

**Request body:**

- `orders` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

## Сборочные задания DBS

### `GET /api/v3/dbs/orders/new`

**Получить список новых сборочных заданий**

Метод возвращает список всех новых [сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS), которые есть у продавца на момент запроса.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий DBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

**Response 200:**

- `orders` (array[object]) — Список новых сборочных заданий
  - `salePrice` (integer) — Цена в валюте продажи с учетом скидки продавца, без учета скидки WB Клуба, умноженная на 100. Предоставляется в информационных целях
  - `requiredMeta` (array[string]) — Список метаданных, доступных для сборочного задания. [Указывать IMEI](./orders-dbs#tag/Metadannye-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~
  - `comment` (string) — Комментарий покупателя
  - `options` (object) — Опции заказа
  - `address` (object) — Адрес покупателя для доставки. При доставке заказов в ПВЗ указан адрес ПВЗ
  - `orderUid` (string) — ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый `orderUID`
  - `groupId` (string(UUID)) — ID группы сборочных заданий.   Объединяет сборочные задания, поступившие на один склад (`warehouseId`) в рамках одной транзакции покупателя (`orderUid
  - `article` (string) — Артикул продавца
  - `colorCode` (string) — Код цвета (только для колеруемых товаров)
  - `rid` (string) — Уникальный ID заказа.   Примечание: `rid` — это `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvraty-pokupa
  - `createdAt` (string(date-time)) — Дата создания сборочного задания
  - `deliveryType` (enum) — Values: `dbs, edbs, dbsPickupPoint`. Тип доставки:   - `dbs` — доставка силами продавца   - `dbsPickupPoint` — доставка силами продавца в ПВЗ   - `edbs` — экспресс-доставка силами продавц
  - `skus` (array[string]) — Массив баркодов товара
  - `id` (integer(int64)) — ID сборочного задания
  - `warehouseId` (integer) — ID склада продавца, на который поступило сборочное задание
  - `nmId` (integer) — Артикул WB
  - `chrtId` (integer) — ID размера товара в системе WB
  - `price` (integer) — Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предостав
  - `finalPrice` (integer) — Сумма к оплате покупателем в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предоставляется 
  - `convertedFinalPrice` (integer) — Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100. Предоставляется в информационных целях
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк
  - `wbStickerId` (integer) — ID стикера. Отображается только для заказов в ПВЗ

---

### `GET /api/v3/dbs/orders`

**Получить информацию о завершенных сборочных заданиях**

Метод возвращает информацию о завершенных [сборочных заданиях](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) после продажи или отмены заказа.

Можно получить данные за заданный период, максимум 30 календарных дней одним запросом.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий DBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `dateFrom` (in query, integer) **(required)** — Дата начала периода в формате Unix timestamp
- `dateTo` (in query, integer) **(required)** — Дата конца периода в формате Unix timestamp

**Response 200:**

- `next` (object)
- `orders` (array[object])
  - `address` (object) — Адрес покупателя для доставки. При доставке заказов в ПВЗ указан адрес ПВЗ
  - `deliveryType` (string) — Тип доставки:   - `dbs` — доставка силами продавца   - `dbsPickupPoint` — доставка силами продавца в ПВЗ   - `edbs` — экспресс-доставка силами продавц
  - `options` (object) — Опции заказа
  - `orderUid` (string) — ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый `orderUID`
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
  - `scanPrice` (integer) — Цена приёмки заказов в ПВЗ, в копейках. Отображается только для заказов в ПВЗ
  - `price` (integer) — Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предостав
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `convertedFinalPrice` (integer) — Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100. Предоставляется в информационных целях
  - `finalPrice` (integer) — Сумма к оплате покупателем в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предоставляется 
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `comment` (string) — Комментарий покупателя
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк
  - `wbStickerId` (integer) — ID стикера. Отображается только для заказов в ПВЗ

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/dbs/groups/info`

**Получить информацию о платной доставке**

Метод возвращает информацию о платной доставке сборочных заданий, которые поступили на один склад (`warehouseId`) в рамках одной транзакции покупателя (`orderUid`).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий DBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Request body:**

- `groups` (array[string]) — Список значений `groupId`. Можно получить из [новых](./orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1v3~1dbs~1orders~1new/get) и [завершенных](.

**Response 200:**

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/dbs/orders/client`

**Информация о покупателе**

Метод возвращает информацию о покупателе по ID сборочных заданий.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий DBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object]) — Информация о покупателе
  - `replacementPhone` (string) — Подменный номер для связи с покупателем.   Пустое значение `""` указывает, что номер еще не назначен
  - `firstName` (string) — Имя покупателя
  - `fullName` (string) — Полное имя, используется для оформления документов. Например, документы на автомобиль
  - `orderID` (integer) — ID сборочного задания
  - `phone` (string) — Резервный подменный номер телефона для связи с покупателем.   Используйте, если недоступен основной номер из `replacementPhone`. Чтобы позвонить покуп
  - `phoneCode` (integer) — Добавочный код.   Пустое значение `""` указывает, что код ещё не назначен
  - `additionalPhoneCodes` (array[string]) — Дополнительные добавочные коды.   Используйте, если не получилось дозвониться по добавочному коду из `phoneCode`.  Пустое значение `""` указывает, что

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/marketplace/v3/dbs/orders/b2b/info`

**Информация о покупателе B2B**

Метод возвращает данные B2B-покупателей по ID сборочных заданий:
  - ИНН
  - КПП
  - Наименование организации

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий DBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (string) **(required)** — Уникальный ID запроса
- `results` (array[object])
  - `data` (object)
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) **(required)** — Есть ли ошибки
  - `orderId` (integer) **(required)** — ID сборочного задания

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

### `POST /api/v3/dbs/orders/delivery-date`

**Дата и время доставки**

Метод возвращает информацию о выбранных покупателем дате и времени доставки сборочных заданий.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий DBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/marketplace/v3/dbs/orders/status/info`

**Получить статусы сборочных заданий**

Метод возвращает статусы [сборочных заданий](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) по их ID.

`supplierStatus` — статус сборочного задания. Триггер его изменения — действие самого продавца.

Возможные значения `supplierStatus`:
| Статус   | Описание            | Как перевести сборочное задание в данный статус |
| -------  | ---------           | --------------------------------------|
| `new`      | **Новое сборочное задание** | |
| `confirm`  | **На сборке**      |  [Перевести сбороч...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object]) — Информация о статусах
  - `errors` (array[object]) — Информация об ошибке
  - `orderId` (integer) — ID сборочного задания
  - `supplierStatus` (string) — Статус сборочного задания, установленный продавцом
  - `wbStatus` (string) — Статус сборочного задания в системе Wildberries

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

**Response 404:**

- `detail` (object) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `POST /api/marketplace/v3/dbs/orders/status/cancel`

**Отменить сборочные задания**

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статусов](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `new` и `confirm` в статус `cancel` — отменено продавцом.
Отменить сборочные задания в статусе `deliver` невозможно.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 сек ...

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

### `POST /api/marketplace/v3/dbs/orders/status/confirm`

**Перевести сборочные задания на сборку**

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `new` в статус `confirm` — на сборке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 сек | 1 запрос | 1 сек | 10 запросов |

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

### `POST /api/marketplace/v3/dbs/orders/stickers`

**Получить стикеры для сборочных заданий с доставкой в ПВЗ**

Метод доступен по [типам токенов](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API): Персональный, Сервисный 

Метод возвращает стикеры для сборочных заданий с доставкой в ПВЗ в [статусах](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post):
  - `confirm` — на сборке
  - `deliver` — в доставке

Получить стикеры можно только в размере 580x400 px в формате PDF.

[Лимит запросов](/openapi/api-information#...

**Parameters:**

- `type` (in query, enum: pdf) **(required)** — Формат стикера
- `width` (in query, enum: 58) **(required)** — Ширина стикера
- `height` (in query, enum: 40) **(required)** — Высота стикера

**Request body:**

- `orders` (array[integer]) **(required)** — Список ID сборочных заданий

**Response 200:**

- `stickers` (array[object]) — Стикеры

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/marketplace/v3/dbs/orders/status/deliver`

**Перевести сборочные задания в доставку**

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `confirm` в статус `deliver` — в доставке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 сек | 1 запрос | 1 сек | 10 запросов |

**Request body:**

- `ordersIds` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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

### `POST /api/marketplace/v3/dbs/orders/status/receive`

**Сообщить о получении заказов**

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `deliver` в статус `receive` — получено покупателем.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 сек | 1 запрос | 1 сек | 10 запросов |

**Request body:**

- `orders` (array[object]) **(required)**
  - `code` (string) — Код подтверждения.   Отображается у покупателя на сайте и в приложении Wildberries
  - `orderId` (integer) — ID сборочного задания

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])

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

### `POST /api/marketplace/v3/dbs/orders/status/reject`

**Сообщить об отказе от заказов**

Метод переводит [сборочные задания](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS) из [статуса](/openapi/orders-dbs#tag/Sborochnye-zadaniya-DBS/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post) `deliver` в статус `reject` — отказ покупателя при получении.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 сек | 1 запрос | 1 сек | 10 запросов |

**Request body:**

- `orders` (array[object]) **(required)**
  - `code` (string) — Код подтверждения.   Отображается у покупателя на сайте и в приложении Wildberries
  - `orderId` (integer) — ID сборочного задания

**Response 200:**

- `requestId` (string) — Уникальный ID запроса
- `results` (array[object])
  - `errors` (array[object]) — Детали ошибки
  - `isError` (boolean) — Есть ли ошибки
  - `orderId` (integer) — ID сборочного задания с успешно обновлёнными данными

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


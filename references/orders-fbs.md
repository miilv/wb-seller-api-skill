# Заказы FBS

С помощью методов раздела Заказы FBS (Fulfillment by Seller) вы можете:
  - получать информацию о [сборочных заданиях](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS) и их статусах, отменять сборочные задания, получать стикеры
  - добавлять, редактировать и удалять [метаданные](/openapi/orders-fbs#tag/Metadannye-FBS) сборочных заданий
  - управлять [поставками](/openapi/orders-fbs#tag/Postavki-FBS)
  - создавать, редактировать и удалять [пропуска](/openapi/orders-fbs#tag/Propuska-FBS) на склады WB

  Узнать, как использовать методы в бизнес-кейсах, можно в [инструкции](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-0771-7571-aea9-11d5b597f34c/zakazy-fbs) по работе с заказами FBS

  Узнать больше о заказах FBS можно в [справочном центре](https://seller.wildberries.ru/instructions/ru/ru/category/b3e60238-fd4c-49ce-8668-ff688725a12d)

## Метаданные FBS

### `POST /api/marketplace/v3/orders/meta`

**Получить метаданные сборочных заданий**

Метод возвращает метаданные [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) по списку их ID.

Перечень метаданных, доступных для сборочного задания, можно получить в [списке новых сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1new/get), поля `requiredMeta` и `optionalMeta`.

Возможные метаданные:
  - `imei` — [IMEI](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1ime...

**Request body:**

- `orders` (array[integer]) **(required)**

**Response 200:**

- `orders` (array[object])
  - `id` (integer) — ID сборочного задания
  - `metaDetails` (object) — Метаданные сборочного задания
  - `meta` (object)

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 403:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 404:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `DELETE /api/v3/orders/{orderId}/meta`

**Удалить метаданные сборочного задания**

Метод удаляет значение [метаданных сборочного задания](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1marketplace~1v3~1orders~1meta/post) для переданного ключа.

Возможные метаданные:
  - `imei` — [IMEI](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1imei/put)
  - `uin` — [УИН](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1uin/put)
  - `gtin` — [GTIN](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1v3~1orders~1...

**Parameters:**

- `?` (in ?, )
- `key` (in query, string) — Название метаданных для удаления (`imei`, `uin`, `gtin`, `sgtin`, `customsDeclaration`). Передается только одно значение.

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/orders/{orderId}/meta/sgtin`

**Закрепить за сборочным заданием код маркировки Честного знака**

Метод позволяет закрепить за [сборочным заданием](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) код маркировки [Честного знака](https://честныйзнак.рф).

Закрепить код маркировки Честного знака можно только если в [метаданных сборочного задания](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1marketplace~1v3~1orders~1meta/post) есть поле `sgtin`, а сборочное задание находится в [статусе](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1s...

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

### `PUT /api/v3/orders/{orderId}/meta/uin`

**Закрепить за сборочным заданием УИН**

Метод обновляет УИН в [метаданных сборочного задания](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1marketplace~1v3~1orders~1meta/post) — уникальный идентификационный номер.

У одного сборочного задания может быть только один УИН.

Добавлять маркировку можно только для заказов, которые доставляются WB и находятся в [статусе](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `confirm`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaproso...

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

### `PUT /api/v3/orders/{orderId}/meta/imei`

**Закрепить за сборочным заданием IMEI**

Метод обновляет IMEI в [метаданных сборочного задания](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1marketplace~1v3~1orders~1meta/post).

У одного сборочного задания может быть только один IMEI. Если у устройства два IMEI — **IMEI** и **IMEI2** или **IMEI1** и **IMEI2** — укажите только **IMEI** или **IMEI1**. **IMEI2** указывать не нужно.

Добавлять маркировку можно только для заказов, которые находятся в [статусе](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1...

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

### `PUT /api/v3/orders/{orderId}/meta/gtin`

**Закрепить за сборочным заданием GTIN**

Метод обновляет GTIN в [метаданных сборочного задания](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1marketplace~1v3~1orders~1meta/post) — уникальный ID товара в Беларуси.

У одного сборочного задания может быть только один GTIN.

Добавлять маркировку можно только для заказов, которые доставляются WB и находятся в [статусе](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `confirm`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov...

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

### `PUT /api/v3/orders/{orderId}/meta/expiration`

**Закрепить за сборочным заданием срок годности товара**

Метод закрепляет за [сборочным заданием](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) срок годности товара. Товар годен до указанной даты.

Добавить срок годности можно только для заказов, которые доставляются WB и находятся в [статусе](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `confirm`.

Получить загруженные данные можно в [метаданных сборочного задания](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1marketplace~1...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `expiration` (string(date (dd.mm.yyyy))) — Дата, до которой годен товар. Не менее 30 дней с текущей даты

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/marketplace/v3/orders/{orderId}/meta/customs-declaration`

**Закрепить за сборочным заданием номер ГТД**

Метод обновляет номер грузовой таможенной декларации (ГТД) в [метаданных сборочного задания](/openapi/orders-fbs#tag/Metadannye-FBS/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta/get).

У одного сборочного задания может быть только один номер ГТД.

Добавлять номер ГТД можно только для сборочных заданий, которые находятся в [статусе](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `confirm` или `complete`

[Лимит запросов](/openapi/api-information#tag/Vvedenie/...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `customsDeclaration` (string) — Номер ГТД

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

## Поставки FBS

### `POST /api/v3/supplies`

**Создать новую поставку**

Метод создаёт новую [поставку](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get).

Ограничения:
- Только для [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) по модели FBS.
- При добавлении в поставку все передаваемые сборочные задания в [статусе](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `new` будут автоматически переведены в статус `confirm` — на сборке.
- Если вы перев...

**Request body:**

- `name` (string) — Наименование поставки

**Response 201:**

- `id` (string) — ID поставки

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `GET /api/v3/supplies`

**Получить список поставок**

Метод возвращает список [поставок](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )

**Response 200:**

- `next` (object)
- `supplies` (array[object]) — Список поставок
  - `id` (string) — ID поставки
  - `isB2b` (boolean) — Признак B2B-продажи:   - `true` — B2B-продажа   - `false` — не B2B-продажа   - `null` — признак отсутствует, сборочные задания не добавлены к поставке
  - `done` (boolean) — Флаг закрытия поставки:   - `true` — закрыта   - `false` — открыта
  - `createdAt` (string(date-time)) — Дата создания поставки (RFC3339)
  - `closedAt` (string(date-time)) — Дата закрытия поставки (RFC3339)
  - `scanDt` (string(date-time)) — Дата скана поставки (RFC3339)
  - `name` (string) — Наименование поставки
  - `cargoType` (enum) — Values: `0, 1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `crossBorderType` (enum(int32)) — Values: `0, 1`. Тип поставки:   - `0` — внутренняя поставка   - `1` — трансграничная поставка   - `null` — значение отсутствует
  - `destinationOfficeId` (integer(int64)) — ID склада назначения поставки. Если `null`, склад назначения не указан
  - `recommendedWhId` (integer(int64)) — ID рекомендуемого склада для приёмки поставки для Москвы и МО.   Рекомендуется ближайший к покупателям склад, который определяется автоматически при п

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PATCH /api/marketplace/v3/supplies/{supplyId}/orders`

**Добавить сборочные задания к поставке**

Метод добавляет до 100 [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) к поставке и переводит их в [статус](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `confirm` — на сборке.

Может перемещать сборочные задания:
  - между активными поставками
  - из закрытой поставки в активную, если сборочные задания требуют [повторной отгрузки](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1supplies~1or...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `orders` (array[integer]) — ID сборочных заданий

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `GET /api/v3/supplies/{supplyId}`

**Получить информацию о поставке**

Метод возвращает подробную информацию о поставке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `id` (string) — ID поставки
- `isB2b` (boolean) — Признак B2B-продажи:   - `true` — B2B-продажа   - `false` — не B2B-продажа   - `null` — признак отсутствует, сборочные задания не добавлены к поставке
- `done` (boolean) — Флаг закрытия поставки:   - `true` — закрыта   - `false` — открыта
- `createdAt` (string(date-time)) — Дата создания поставки (RFC3339)
- `closedAt` (string(date-time)) — Дата закрытия поставки (RFC3339)
- `scanDt` (string(date-time)) — Дата скана поставки (RFC3339)
- `name` (string) — Наименование поставки
- `cargoType` (enum) — Values: `0, 1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
- `crossBorderType` (enum(int32)) — Values: `0, 1`. Тип поставки:   - `0` — внутренняя поставка   - `1` — трансграничная поставка   - `null` — значение отсутствует
- `destinationOfficeId` (integer(int64)) — ID склада назначения поставки. Если `null`, склад назначения не указан
- `recommendedWhId` (integer(int64)) — ID рекомендуемого склада для приёмки поставки для Москвы и МО.   Рекомендуется ближайший к покупателям склад, который определяется автоматически при п

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `DELETE /api/v3/supplies/{supplyId}`

**Удалить поставку**

Метод удаляет [поставку](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get), если она активна и за ней не закреплено ни одно [сборочное задание](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов...

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

### `GET /api/marketplace/v3/supplies/{supplyId}/order-ids`

**Получить ID сборочных заданий поставки**

Метод возвращает список ID сборочных заданий, закреплённых за поставкой.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `supplyId` (in path, string) **(required)** — ID поставки

**Response 200:**

- `orderIds` (array[integer]) — ID сборочных заданий

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PATCH /api/v3/supplies/{supplyId}/deliver`

**Передать поставку в доставку**

Метод закрывает [поставку](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get) и переводит все [сборочные задания](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) в ней в [статус](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `complete` — в доставке. После закрытия поставки добавить новые сборочные задания к ней нельзя.

Если поставка не была передана в доставку, то при приёмке первого товара пос...

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
  - `orders` (array[object]) — Сборочные задания, метаданные которых не прошли или ещё не завершили валидацию

---

### `GET /api/v3/supplies/{supplyId}/barcode`

**Получить QR-код поставки**

Метод возвращает QR-код [поставки](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get) в форматах:
  - SVG
  - ZPLV (вертикальный)
  - ZPLH (горизонтальный)
  - PNG

QR-код поставки можно получить только если поставка [передана в доставку](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1deliver/patch).

Размер — 580x400 px.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов ...

**Parameters:**

- `?` (in ?, )
- `type` (in query, enum: svg, zplv, zplh, png) **(required)** — Тип стикера

**Response 200:**

- `barcode` (string) — Закодированное значение стикера (ID поставки)
- `file` (string(byte)) — Полное представление стикера в заданном формате (кодировка base64)

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `GET /api/v3/supplies/{supplyId}/trbx`

**Получить список грузомест поставки**

Возвращает список грузомест поставки.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `trbxes` (array[object])
  - `id` (string) — ID грузоместа

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/supplies/{supplyId}/trbx`

**Добавить грузоместа к поставке**

Метод добавляет требуемое количество [грузомест](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/get) в [поставку](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get).

Грузоместа необходимо добавлять только в поставки, отгружаемые на ПВЗ.

Грузоместа можно добавить только в открытую поставку. Вы можете добавить столько же грузомест, сколько всего товаров в поставке, плюс ещё один.

[Лимит запросов](/openapi/api-information#tag...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `amount` (integer) **(required)** — Количество грузомест, которые необходимо добавить к поставке

**Response 201:**

- `trbxIds` (array[string]) — Список ID грузомест, которые были созданы

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `DELETE /api/v3/supplies/{supplyId}/trbx`

**Удалить грузоместа из поставки**

Метод удаляет грузоместа из поставки.

Можно удалить только пока поставка на сборке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )

**Request body:**

- `trbxIds` (array[string]) **(required)** — Список ID грузомест, которые необходимо удалить

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/supplies/{supplyId}/trbx/stickers`

**Получить стикеры грузомест поставки**

Метод возвращает QR-стикеры в форматах:
  - SVG
  - ZPLV (вертикальный)
  - ZPLH (горизонтальный)
  - PNG

Размер стикеров — 580x400 px.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )
- `type` (in query, enum: svg, zplv, zplh, png) **(required)** — Тип стикера

**Request body:**

- `trbxIds` (array[string]) **(required)** — Список ID грузомест, по которым необходимо вернуть стикеры

**Response 200:**

- `stickers` (array[object])
  - `barcode` (string) — Закодированное значение стикера
  - `file` (string(byte)) — Полное представление стикера в заданном формате (кодировка base64)

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

## Пропуска FBS

### `GET /api/v3/passes/offices`

**Получить список складов, для которых требуется пропуск**

Метод возвращает список складов для привязки к [пропуску продавца](/openapi/orders-fbs#tag/Propuska-FBS/paths/~1api~1v3~1passes/get).

  Данные, которые возвращает метод, могут меняться. Рекомендуем периодически синхронизировать список

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запро...

**Response 200:**

_(array of objects:)_
- `name` (string) — Название
- `address` (string) — Адрес
- `id` (integer(int64)) — ID

---

### `GET /api/v3/passes`

**Получить список пропусков**

Метод возвращает список всех [созданных](/openapi/orders-fbs#tag/Propuska-FBS/paths/~1api~1v3~1passes/post) пропусков продавца.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Response 200:**

_(array of objects:)_
- `firstName` (string) — Имя водителя
- `dateEnd` (string) — Дата окончания действия пропуска
- `lastName` (string) — Фамилия водителя
- `carModel` (string) — Марка машины
- `carNumber` (string) — Номер машины
- `officeName` (string) — Название склада
- `officeAddress` (string) — Адрес склада
- `officeId` (integer(int64)) — ID склада
- `id` (integer(int64)) — ID пропуска

---

### `POST /api/v3/passes`

**Создать пропуск**

Метод создаёт [пропуск продавца](/openapi/orders-fbs#tag/Propuska-FBS/paths/~1api~1v3~1passes/get) с привязкой к складу WB.

Пропуск действует 48 часов со времени создания.

  Максимум 1 запрос в 10 [минут](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца

**Request body:**

- `firstName` (string) **(required)** — Имя водителя
- `lastName` (string) **(required)** — Фамилия водителя
- `carModel` (string) **(required)** — Марка машины
- `carNumber` (string) **(required)** — Номер машины
- `officeId` (integer(int64)) **(required)** — ID склада

**Response 201:**

- `id` (integer) — ID пропуска продавца

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/passes/{passId}`

**Обновить пропуск**

Метод обновляет данные [пропуска продавца](/openapi/orders-fbs#tag/Propuska-FBS/paths/~1api~1v3~1passes/get). В том числе, можно обновить данные привязанного склада WB.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )

**Request body:**

- `firstName` (string) **(required)** — Имя водителя
- `lastName` (string) **(required)** — Фамилия водителя
- `carModel` (string) **(required)** — Марка машины
- `carNumber` (string) **(required)** — Номер машины
- `officeId` (integer(int64)) **(required)** — ID склада

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `DELETE /api/v3/passes/{passId}`

**Удалить пропуск**

Метод удаляет пропуск продавца [из списка](/openapi/orders-fbs#tag/Propuska-FBS/paths/~1api~1v3~1passes/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )

---

## Сборочные задания FBS

### `GET /api/v3/orders/new`

**Получить список новых сборочных заданий**

Метод возвращает список всех новых [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get), которые есть у продавца на момент запроса.

Наличие в сборочных заданиях метаданных, указанных в полях requiredMeta и optionalMeta, влияет только на возможность перевести поставку в доставку. Если ваш товар подлежит обязательной маркировке средствами
идентификации, необходимо указывать метаданные независимо от того, в каком поле они были получены (п. 4.6 Оферты).

...

**Response 200:**

- `orders` (array[object]) — Список новых сборочных заданий
  - `address` (object) — Точный адрес покупателя для доставки, если применимо. Из-за особенностей адреса некоторые поля могут быть пустыми
  - `ddate` (string) — Планируемая дата доставки.  Поле отображается для сборочных заданий со сверхгабаритными товарами `СГТ`, `cargoType: 2`
  - `sellerDate` (string) — Рекомендуемая дата доставки СГТ в сортировочный центр или на склад.   Поле отображается для сборочных заданий со сверхгабаритными товарами `СГТ`, `car
  - `salePrice` (integer) — Цена продавца в валюте продажи с учётом скидки продавца, без учёта скидки WB Клуба, умноженная на 100. Предоставляется в информационных целях
  - `requiredMeta` (array[string]) — Список метаданных, которые необходимо добавить в сборочное задание, чтобы поставку с этим сборочным заданием можно было перевести в доставку
  - `optionalMeta` (array[string]) — Список метаданных, которые можно добавить в сборочное задание.  Поставку со сборочным заданием без этих метаданных можно перевести в доставку, но они 
  - `deliveryType` (enum) — Values: `fbs`. Тип доставки: - `fbs` — доставка на склад Wildberries (FBS)
  - `comment` (string) — Комментарий покупателя
  - `scanPrice` (number(uint32)) — Цена приёмки в копейках. Отображается после фактической приёмки заказа. Для данного метода всегда будет возвращаться `null`. Предоставляется в информа
  - `orderUid` (string) — ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый `orderUid`
  - `article` (string) — Артикул продавца
  - `colorCode` (string) — Код цвета (только для колеруемых товаров)
  - `rid` (string) — Уникальный ID заказа.   Примечание: `rid` — это `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvraty-pokupa
  - `createdAt` (string(date-time)) — Дата создания сборочного задания (RFC3339)
  - `offices` (array[string]) — Список офисов, куда следует привезти товар
  - `skus` (array[string]) — Список баркодов
  - `id` (integer(int64)) — ID сборочного задания
  - `warehouseId` (integer) — ID склада продавца, на который поступило сборочное задание
  - `officeId` (integer(int64)) — ID склада WB, к которому привязан склад продавца
  - `nmId` (integer) — Артикул WB
  - `chrtId` (integer) — ID размера товара в системе WB
  - `price` (integer) — Цена в валюте продажи с учётом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи — в поле `currencyCode`. Предоставляетс
  - `finalPrice` (integer) — Сумма к оплате покупателем в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи указан в поле `currencyCode`. Предоставляется 
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Предоставляется в информационных целях
  - `convertedFinalPrice` (integer) — Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `crossBorderType` (enum(int32)) — Values: `0, 1`. Тип сборочного задания:   - `0` — внутренняя поставка   - `1` — трансграничная поставка
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк
  - `options` (object) — Опции заказа

---

### `GET /api/v3/orders`

**Получить информацию о сборочных заданиях**

Метод возвращает информацию о сборочных заданиях без их актуального [статуса](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post).

Можно получить данные за заданный период, максимум 30 календарных дней одним запросом.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | ...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `dateFrom` (in query, integer) — Дата начала периода в формате Unix timestamp. По умолчанию — дата за 30 дней до запроса
- `dateTo` (in query, integer) — Дата конца периода в формате Unix timestamp

**Response 200:**

- `next` (object)
- `orders` (array[object])
  - `address` (object) — Точный адрес покупателя для доставки, если применимо. Из-за особенностей адреса некоторые поля могут быть пустыми
  - `scanPrice` (number(uint32)) — Цена приёмки в копейках. Отображается после фактической приёмки заказа
  - `deliveryType` (enum) — Values: `fbs`. Тип доставки: - `fbs` — доставка на склад Wildberries (FBS)
  - `supplyId` (string) — ID поставки. Возвращается, если заказ закреплён за поставкой
  - `orderUid` (string) — ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый `orderUid`
  - `article` (string) — Артикул продавца
  - `colorCode` (string) — Код цвета (только для колеруемых товаров)
  - `rid` (string) — Уникальный ID заказа.   Примечание: `rid` — это `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvraty-pokupa
  - `createdAt` (string(date-time)) — Дата создания сборочного задания (RFC3339)
  - `offices` (array[string]) — Список офисов, куда следует привезти товар
  - `skus` (array[string]) — Список баркодов
  - `id` (integer(int64)) — ID сборочного задания
  - `warehouseId` (integer) — ID склада продавца, на который поступило сборочное задание
  - `officeId` (integer(int64)) — ID склада WB, к которому привязан склад продавца
  - `nmId` (integer) — Артикул WB
  - `chrtId` (integer) — ID размера товара в системе WB
  - `price` (integer) — Цена в валюте продажи с учётом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Код валюты продажи — в поле `currencyCode`. Предоставляетс
  - `convertedPrice` (integer) — Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100. Предоставляется в информационных целях
  - `currencyCode` (integer(ISO 4217)) — Код валюты продажи
  - `convertedCurrencyCode` (integer(ISO 4217)) — Код валюты страны продавца
  - `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
  - `crossBorderType` (enum(int32)) — Values: `0, 1`. Тип сборочного задания:   - `0` — внутренняя поставка   - `1` — трансграничная поставка
  - `comment` (string) — Комментарий покупателя
  - `isZeroOrder` (boolean) — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк
  - `options` (object) — Опции заказа

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/orders/status`

**Получить статусы сборочных заданий**

Метод возвращает статусы [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) по их ID.

`supplierStatus` — статус сборочного задания. Триггер его изменения — действие самого продавца.

Возможные значения `supplierStatus`:

| Статус   | Описание            | Как перевести сборочное задание в данный статус |
|-------|----------------------|--------------------------------------|
| `new`      | **Новое сборочное задание** |  |
| `confirm`  | **На сборке*...

**Request body:**

- `orders` (array[integer]) **(required)** — Список ID сборочных заданий

**Response 200:**

- `orders` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `GET /api/v3/supplies/orders/reshipment`

**Получить все сборочные задания для повторной отгрузки**

Метод возвращает все [сборочные задания](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get), требующие повторной отгрузки.

Повторная отгрузка требуется, если поставка была отсканирована в пункте приёмки, но при этом в ней всё ещё есть неотсканированные товары. Спустя определённое время необходимо доставить эти товары заново. Данные сборочные задания можно перевести в [другую активную поставку](/openapi/orders-fbs#tag/Postavki-FBS/paths/~1api~1marketplace~1v3~1supplies~...

**Response 200:**

- `orders` (array[object]) — Список сборочных заданий

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PATCH /api/v3/orders/{orderId}/cancel`

**Отменить сборочное задание**

Метод отменяет [сборочное задание](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) и переводит в [статус](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `cancel` — отменено продавцом.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 20 запросов |

Один запрос с кодом ответа 409 уч...

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

### `POST /api/v3/orders/stickers`

**Получить стикеры сборочных заданий**

Метод возвращает список стикеров для [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS).

Можно получить стикер в форматах:
  - SVG
  - ZPLV (вертикальный)
  - ZPLH (горизонтальный)
  - PNG

Ограничения:
  - За один запрос можно получить максимум 100 стикеров.
  - Стикеры можно получить только для сборочных заданий в [статусах](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) `confirm` — на сборке и `complete` — в доставке.

Доступны размеры...

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

### `POST /api/v3/orders/stickers/cross-border`

**Получить стикеры сборочных заданий трансграничных поставок**

Метод возвращает список стикеров [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) трансграничных поставок в формате PDF.

Для каждого сборочного задания в ответе указывается статус генерации стикера:
  - `awaitingTrackNumber` — стикер не готов. Ожидается трек-номер от перевозчика.
  - `ready` — стикер готов

  Стикер может генерироваться с задержкой. Повторяйте запрос, пока не получите статус ready.

Ограничения:
  - За один запрос можно получить м...

**Request body:**

- `orders` (array[integer]) — Список ID сборочных заданий

**Response 200:**

- `stickers` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/orders/status/history`

**История статусов для сборочных заданий трансграничных поставок**

Метод возвращает историю [статусов](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders~1status/post) для [сборочных заданий](/openapi/orders-fbs#tag/Sborochnye-zadaniya-FBS/paths/~1api~1v3~1orders/get) трансграничных поставок.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 м...

**Request body:**

- `orders` (array[integer]) — ID сборочных заданий

**Response 200:**

- `orders` (array[object]) — Список сборочных заданий

---

### `POST /api/v3/orders/client`

**Заказы с информацией по клиенту**

Метод позволяет получать информацию о покупателе по ID сборочного задания.

Только для трансграничных поставок из **Турции**.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных заданий, поставок и пропусков FBS:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Request body:**

- `orders` (array[integer]) — Список заказов

**Response 200:**

- `orders` (array[object]) — Информация по клиенту для трансграничных поставок из Турции
  - `firstName` (string) — Имя клиента
  - `fullName` (string) — Фамилия, Имя, Отчество
  - `lastName` (string) — Фамилия клиента
  - `middleName` (string) — Отчество клиента
  - `orderID` (integer) — Номер заказа
  - `phone` (string) — Телефон для связи с клиентом
  - `phoneCode` (string) — Не используется

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `GET /api/marketplace/v3/fbs/orders/archive`

**Получить список архивных сборочных заданий**

Метод возвращает сборочные задания, созданные более 3 месяцев назад.

Часть сборочных заданий попадает в архив позже, чем через 3 месяца после создания, так как поставка переходит в архив только после того, как все заказы в ней будут завершены.
Например, так происходит, если продавец не доставил один из заказов в поставке и заказ был отменён автоматически через несколько дней.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для методов сборочных ...

**Parameters:**

- `year` (in query, integer) **(required)** — Год создания заказа
- `month` (in query, integer) **(required)** — Месяц создания заказа
- `next` (in query, integer) **(required)** — Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных. Для получения полного списка данных должен быть равен `0`
- `limit` (in query, integer) **(required)** — Количество сборочных заданий в ответе

**Response 200:**

- `next` (integer(int64)) **(required)** — Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения следующего пакета данных
- `orders` (array[object]) **(required)** — Архивные сборочные задания
  - `cargoType` (string) **(required)** — Тип товара:   - `mgt` — малогабаритный товар (МГТ)   - `sgt` — сверхгабаритный товар (СГТ)   - `kgtPlus` — крупногабаритный товар (КГТ+)
  - `colorCode` (string) **(required)** — Код цвета для колеруемых товаров
  - `createdAt` (string) **(required)** — Дата создания заказа
  - `crossBorder` (object) **(required)** — Информация о заказе по модели кроссбордер
  - `crossBorderType` (string) **(required)** — Тип сборочного задания:   - `local` — внутренняя поставка   - `crossBorder` — трансграничная поставка
  - `id` (integer) **(required)** — ID сборочного задания
  - `isZeroOrder` (boolean) **(required)** — Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым остатком   - `true` — заказ сделан на товар с нулевым остатк
  - `metaDetails` (object) **(required)** — Метаданные сборочного задания
  - `options` (object) **(required)** — Опции заказа
  - `orderUid` (string) **(required)** — ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый `orderUid`
  - `priceInfo` (object) **(required)** — Информация о цене заказа
  - `product` (object) **(required)** — Информация о товаре
  - `rid` (string) **(required)** — Уникальный ID заказа.   Примечание: `rid` — это `srid` в ответах методов:   - [Заявки покупателей на возврат](./user-communication#tag/Vozvraty-pokupa
  - `scanPrice` (integer) **(required)** — Цена приёмки заказа в копейках
  - `status` (object) **(required)** — Последние статусы сборочного задания
  - `stickerId` (integer) **(required)** — ID стикера
  - `supplyId` (string) **(required)** — ID поставки
  - `warehouseId` (integer) **(required)** — ID склада продавца, с которого был отгружен товар

---


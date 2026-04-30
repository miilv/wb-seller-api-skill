# Поставки FBW

Узнать больше о поставках FBW можно в [справочном центре](https://seller.wildberries.ru/instructions/subcategory/5a8e1202-0865-45b7-acae-5d0afc7add56?goBackOption=prevRoute&categoryId=479385c6-de01-4b4d-ad4e-ed941e65582e)

В разделе описаны методы получения:
  - [информации для формирования поставок](/openapi/orders-fbw#tag/Informaciya-dlya-formirovaniya-postavok)
  - [информации о поставках](/openapi/orders-fbw#tag/Informaciya-o-postavkah)

## Информация для формирования поставок

### `POST /api/v1/acceptance/options`

**Опции приёмки**

Метод возвращает информацию о том, какие склады и типы упаковки доступны для поставки. Список складов определяется по баркоду и количеству товара.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 6 запросов | 10 сек | 6 запросов |
| Сервисный | 1 мин | 6 запросов | 10 сек | 6 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |

**Parameters:**

- `warehouseID` (in query, integer) — ID склада.   Если параметр не указан, возвращаются данные по всем складам.  **Максимум одно значение**

**Request body:**

_(array of objects:)_
- `quantity` (integer) — Суммарное количество товаров, планируемых для поставки.    **Максимум 999999**
- `barcode` (string) — Баркод из карточки товара

**Response 200:**

- `result` (array[object])
- `requestId` (string) — ID запроса при наличии ошибок

**Response 400:**

- `status` (integer) — HTTP статус-код
- `title` (string) — ID ошибки
- `detail` (string) — Описание ошибки
- `requestId` (string) — ID запроса
- `origin` (string) — Сервис, вернувший ошибку

---

### `GET /api/v1/warehouses`

**Список складов**

Метод возвращает список складов WB.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 6 запросов | 10 сек | 6 запросов |
| Сервисный | 1 мин | 6 запросов | 10 сек | 6 запросов |
| Базовый | 12 ч | 1 запрос | 12 ч | 1 запрос |

**Response 200:**

_(array of objects:)_
- `ID` (integer) — ID склада
- `name` (string) — Название склада
- `address` (string) — Адрес склада
- `workTime` (string) — Режим работы склада
- `isActive` (boolean) — Доступен ли в качестве склада назначения: - `true` — да - `false` — нет
- `isTransitActive` (boolean) — Доступен ли в качестве транзитного склада: - `true` — да - `false` — нет

---

### `GET /api/v1/transit-tariffs`

**Транзитные направления**

Метод возвращает информацию о доступных транзитных направлениях.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 6 запросов | 10 сек | 10 запросов |
| Сервисный | 1 мин | 6 запросов | 10 сек | 10 запросов |
| Базовый | 12 ч | 1 запрос | 12 ч | 1 запрос |

**Response 200:**

_(array of objects:)_
- `transitWarehouseName` (string) — Транзитный склад
- `destinationWarehouseName` (string) — Склад назначения
- `activeFrom` (string(date-time)) — С какого числа доступно транзитное направление
- `boxTariff` (array[object]) — Тариф за транзит коробов. Если `null`, транзит для коробов недоступен
  - `from` (integer) — Объём поставки от, литры
  - `to` (integer) — Объём поставки до, литры
  - `value` (number) — Тариф, ₽ за литр
- `palletTariff` (integer) — Тариф за паллету, ₽

---

## Информация о поставках

### `POST /api/v1/supplies`

**Список поставок**

Метод возвращает список поставок, по умолчанию — последние 1000 поставок.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Сервисный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |

**Parameters:**

- `limit` (in query, integer) — Количество записей в ответе
- `offset` (in query, integer) — После какого элемента выдавать данные

**Request body:**

- `dates` (array[object]) — Фильтр по датам
  - `from` (string(ISO 8601)) — Дата начала периода
  - `till` (string(ISO 8601)) — Дата окончания периода
  - `type` (enum) **(required)** — Values: `factDate, createDate, supplyDate, updatedDate`. Тип дат:   - `factDate` — дата фактической отгрузки поставки   - `createDate` — дата создания поставки   - `supplyDate` — плановая дата отгрузки поста
- `statusIDs` (array[object]) — Фильтр поставок по статусам. Возможные значения:   - `1` — Не запланировано   - `2` — Запланировано   - `3` — Отгрузка разрешена   - `4` — Идёт приёмк

**Response 200:**

_(array of objects:)_
- `phone` (string) — Телефон пользователя, создавшего поставку
- `supplyID` (integer) — ID поставки. Если `null`, это заказ, тогда используйте значение поля `preorderID`
- `preorderID` (integer) — ID заказа (незапланированная поставка). Для всех виртуальных поставок будет `0`
- `createDate` (string) — Дата и время создания поставки
- `supplyDate` (string) — Плановая дата отгрузки поставки
- `factDate` (string) — Дата фактической отгрузки поставки
- `updatedDate` (string) — Дата изменения поставки
- `statusID` (enum) — Values: `1, 2, 3, 4, 5, 6`. ID статуса поставки:   - `1` — Не запланировано   - `2` — Запланировано   - `3` — Отгрузка разрешена   - `4` — Идёт приёмка   - `5` — Принято   - `6` 
- `boxTypeID` (object) — ID типа поставки:   - `0` — Без коробов (виртуальная поставка)   - `1` и `2` — Короба   - `5` — Монопаллеты   - `6` — Суперсейф
- `isBoxOnPallet` (boolean) — Тип поставки — **Поштучная палета**:   - `true` — да   - `false` — нет    Поле возвращается только при `"boxTypeID": 2`

**Response 400:**

- `status` (integer) — HTTP статус-код
- `title` (string) — ID ошибки
- `detail` (string) — Описание ошибки
- `requestId` (string) — ID запроса
- `origin` (string) — Сервис, вернувший ошибку

---

### `GET /api/v1/supplies/{ID}`

**Детали поставки**

Метод возвращает детали поставки по ID.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Сервисный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |

**Parameters:**

- `ID` (in path, integer) **(required)** — ID поставки или заказа
- `isPreorderID` (in query, boolean) — Поиск по:   - `true` — ID заказа, если в `ID` передаёте ID заказа   - `false` — ID поставки, если в `ID` передаёте ID поставки

**Response 200:**

- `phone` (string) — Телефон пользователя, создавшего поставку
- `statusID` (enum) — Values: `1, 2, 3, 4, 5, 6`. ID статуса поставки:   - `1` — Не запланировано   - `2` — Запланировано   - `3` — Отгрузка разрешена   - `4` — Идёт приёмка   - `5` — Принято   - `6` 
- `virtualTypeID` (integer) — ID типа виртуальной поставки. Отображается только для поставок с `"boxTypeID":0`.   - `0` — Перенос остатков   - `1` — Обезличка   - `4` — QR-поставка
- `boxTypeID` (integer) — ID типа поставки:   - `0` — Без коробов (виртуальная поставка)   - `1` и `2` — Короба   - `5` — Монопаллеты   - `6` — Суперсейф
- `createDate` (string) — Дата и время создания поставки
- `supplyDate` (string) — Плановая дата отгрузки поставки
- `factDate` (string) — Дата фактической отгрузки поставки
- `updatedDate` (string) — Дата изменения поставки
- `warehouseID` (integer) — ID склада, на который планируется поставка
- `warehouseName` (string) — Название склада, на который планируется поставка
- `actualWarehouseID` (integer) — ID склада, на который поставка была привезена
- `actualWarehouseName` (string) — Название склада, на который поставка привезена
- `transitWarehouseID` (integer) — ID транзитного склада
- `transitWarehouseName` (string) — Название транзитного склада
- `acceptanceCost` (number) — Предварительная стоимость приёмки, ₽
- `paidAcceptanceCoefficient` (number) — Коэффициент приёмки
- `rejectReason` (string) — Причина, по которой поставка не может быть принята
- `supplierAssignName` (string) — Краткое название продавца
- `storageCoef` (string) — Коэффициент хранения
- `deliveryCoef` (string) — Коэффициент логистики
- `quantity` (integer) — Добавлено в поставку/заказ, шт
- `readyForSaleQuantity` (integer) — Поступило в продажу, шт
- `acceptedQuantity` (integer) — Принято, шт
- `unloadingQuantity` (integer) — Количество товара, находящегося на раскладке, шт
- `depersonalizedQuantity` (integer) — Количество обезличенного товара, шт
- `isBoxOnPallet` (boolean) — Тип поставки — **Поштучная палета**:   - `true` — да   - `false` — нет    Поле возвращается только при `"boxTypeID": 2`

**Response 400:**

- `status` (integer) — HTTP статус-код
- `title` (string) — ID ошибки
- `detail` (string) — Описание ошибки
- `requestId` (string) — ID запроса
- `origin` (string) — Сервис, вернувший ошибку

**Response 404:**

- `status` (integer) — HTTP статус-код
- `title` (string) — ID ошибки
- `detail` (string) — Описание ошибки
- `requestId` (string) — ID запроса
- `origin` (string) — Сервис, вернувший ошибку

---

### `GET /api/v1/supplies/{ID}/goods`

**Товары поставки**

Метод возвращает информацию о товарах в поставке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Сервисный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |

**Parameters:**

- `limit` (in query, integer) — Количество записей в ответе
- `offset` (in query, integer) — После какого элемента выдавать данные
- `isPreorderID` (in query, boolean) — Поиск по:   - `true` — ID заказа, если в `ID` передаёте ID заказа   - `false` — ID поставки, если в `ID` передаёте ID поставки
- `ID` (in path, integer) **(required)** — ID поставки или заказа

**Response 200:**

_(array of objects:)_
- `barcode` (string) — Баркод товара
- `vendorCode` (string) — Артикул продавца
- `nmID` (integer) — Артикул WB
- `needKiz` (boolean) — Нужен ли [код маркировки Честного знака](https://честныйзнак.рф/) для этого товара:   - `false` — не нужен   - `true` — нужен
- `tnved` (string) — Код ТНВЭД.  Если `"needKiz":true`, а `"tnved":null`, нужно заполнить характеристику товара **ТН ВЭД** в [личном кабинете](https://seller.wildberries.r
- `techSize` (string) — Размер товара, указанный продавцом
- `color` (string) — Цвет товара
- `supplierBoxAmount` (integer) — Указано в упаковке, шт
- `quantity` (integer) — Указано в поставке/заказе, шт
- `readyForSaleQuantity` (integer) — Поступило в продажу, шт
- `acceptedQuantity` (integer) — Принято, шт
- `unloadingQuantity` (integer) — Количество товара на раскладке, шт

**Response 400:**

- `status` (integer) — HTTP статус-код
- `title` (string) — ID ошибки
- `detail` (string) — Описание ошибки
- `requestId` (string) — ID запроса
- `origin` (string) — Сервис, вернувший ошибку

---

### `GET /api/v1/supplies/{ID}/package`

**Упаковка поставки**

Метод возвращает информацию об упаковке поставки.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Сервисный | 1 мин | 30 запросов | 2 сек | 10 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |

**Parameters:**

- `ID` (in path, integer) **(required)** — ID поставки

**Response 200:**

_(array of objects:)_
- `packageCode` (string) — Штрих-код упаковки
- `quantity` (integer) — Суммарное количество товара в упаковке, шт
- `barcodes` (array[object]) — Список упакованных товаров
  - `barcode` (string) — Баркод
  - `quantity` (integer) — Количество, шт

**Response 400:**

- `status` (integer) — HTTP статус-код
- `title` (string) — ID ошибки
- `detail` (string) — Описание ошибки
- `requestId` (string) — ID запроса
- `origin` (string) — Сервис, вернувший ошибку

---


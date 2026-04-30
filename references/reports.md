# Отчёты

Узнать больше об отчётах можно в [справочном центре](https://seller.wildberries.ru/instructions/subcategory/5f2162c5-069b-416d-a4e1-48da2a76e6b0)

С помощью этих методов вы можете получать [основные отчёты](/openapi/reports#tag/Osnovnye-otchyoty) и отчёты о:
  1. [Остатках на складах](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah)
  2. [Товарах с обязательной маркировкой](/openapi/reports#tag/Otchyot-o-tovarah-c-obyazatelnoj-markirovkoj)
  3. [Удержаниях](/openapi/reports#tag/Otchyoty-ob-uderzhaniyah)
  4. [Операциях при приёмке](/openapi/reports#tag/Operacii-pri-priyomke)
  5. [Платном хранении](/openapi/reports#tag/Platnoe-hranenie)
  6. [Продажах по регионам](/openapi/reports#tag/Prodazhi-po-regionam)
  7. [Доле бренда в продажах](/openapi/reports#tag/Dolya-brenda-v-prodazhah)
  8. [Скрытых товарах](/openapi/reports#tag/Skrytye-tovary)
  9. [Возвратах и перемещении товаров](/openapi/reports#tag/Otchyot-o-vozvratah-i-peremeshenii-tovarov)

## Доля бренда в продажах

### `GET /api/v1/analytics/brand-share/brands`

**Бренды продавца**

Метод возвращает список брендов продавца для отчёта о [доле бренда в продажах](https://seller.wildberries.ru/analytics-reports/brand-share). 

Можно получить только бренды, которые:
- Продавались за последние 90 дней.
- Есть на складе WB.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Сервисный | 1 мин | 1 з...

---

### `GET /api/v1/analytics/brand-share/parent-subjects`

**Родительские категории бренда**

Метод возвращает родительские категории бренда продавца для отчёта о [доле бренда в продажах](https://seller.wildberries.ru/analytics-reports/brand-share).

Можно получить отчёт максимум за 365 дней. Данные доступны с 1 ноября 2022.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 5 сек | 1 запрос | 5 сек | 20 запросов |
| Сервисный | 5 сек | 1 запрос ...

**Parameters:**

- `locale` (in query, string) — Язык поля ответа `parentName`:   - `ru` — русский   - `en` — английский   - `zh` — китайский
- `brand` (in query, string) **(required)** — Бренд
- `?` (in ?, )
- `?` (in ?, )

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `GET /api/v1/analytics/brand-share`

**Получить отчёт**

Метод возвращает отчёт о [доле бренда продавца в продажах](https://seller.wildberries.ru/analytics-reports/brand-share). 

Можно получить отчёт максимум за 365 дней. Данные доступны с 1 ноября 2022.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 5 сек | 1 запрос | 5 сек | 20 запросов |
| Сервисный | 5 сек | 1 запрос | 5 сек | 20 запросов |
| Базовый ...

**Parameters:**

- `parentId` (in query, integer) **(required)** — ID родительской категории
- `brand` (in query, string) **(required)** — Бренд
- `?` (in ?, )
- `?` (in ?, )

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

## Операции при приёмке

### `GET /api/v1/acceptance_report`

**Создать отчёт**

Метод создаёт [задание на генерацию](/openapi/reports#tag/Operacii-pri-priyomke/paths/~1api~1v1~1acceptance_report~1tasks~1%7Btask_id%7D~1status/get) отчёта об [операциях при приёмке](/openapi/reports#tag/Operacii-pri-priyomke/paths/~1api~1v1~1acceptance_report~1tasks~1%7Btask_id%7D~1download/get).

Можно получить отчёт максимум за 31 день.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | ---...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )

**Response 200:**

- `data` (object)
  - `taskId` (string) — ID задания на генерацию

---

### `GET /api/v1/acceptance_report/tasks/{task_id}/status`

**Проверить статус**

Метод возвращает статус [задания на генерацию](/openapi/reports#tag/Operacii-pri-priyomke/paths/~1api~1v1~1acceptance_report/get) отчёта об [операциях при приёмке](/openapi/reports#tag/Operacii-pri-priyomke/paths/~1api~1v1~1acceptance_report~1tasks~1%7Btask_id%7D~1download/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 5 сек | 1 запрос | 5 сек ...

**Parameters:**

- `task_id` (in path, string) **(required)** — ID задания на генерацию

**Response 200:**

- `data` (object)
  - `id` (string) — ID задания
  - `status` (string) — Статус задания:   * `new` — новое   * `processing` —  обрабатывается   * `done` — отчёт готов   * `purged` — отчёт удалён   * `canceled` — отклонено

---

### `GET /api/v1/acceptance_report/tasks/{task_id}/download`

**Получить отчёт**

Метод возвращает отчёт об [операциях при приёмке](https://seller.wildberries.ru/analytics-reports/acceptance-report) по ID [задания на генерацию](/openapi/reports#tag/Operacii-pri-priyomke/paths/~1api~1v1~1acceptance_report/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Сервисный | 1 мин | 1 запрос | 1 ми...

**Parameters:**

- `task_id` (in path, string) **(required)** — ID задания на генерацию

**Response 200:**

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

## Основные отчёты

### `GET /api/v1/supplier/stocks`

**Склады**

Данный метод устарел. Он будет удалён [23 июня](https://dev.wildberries.ru/release-notes?id=494)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Сервисный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Базовый | 3 ч | 1 запрос | 3 ч | 1 запрос |

**Parameters:**

- `dateFrom` (in query, string) **(required)** — Дата и время последнего изменения по товару.   Для получения полного остатка следует указывать максимально раннее значение.   Например, `2019-06-20`  

**Response 200:**

_(array of objects:)_
- `lastChangeDate` (string) — Дата и время обновления информации в сервисе. Это поле соответствует параметру `dateFrom` в запросе. Если часовой пояс не указан, то берётся Московско
- `warehouseName` (string) — Название склада
- `supplierArticle` (string) — Артикул продавца
- `nmId` (integer) — Артикул WB
- `barcode` (string) — Баркод
- `quantity` (integer) — Количество, доступное для продажи (сколько можно добавить в корзину)
- `inWayToClient` (integer) — В пути к клиенту
- `inWayFromClient` (integer) — В пути от клиента
- `quantityFull` (integer) — Полное (непроданное) количество, которое числится за складом (= `quantity` + в пути)
- `category` (string) — Категория
- `subject` (string) — Предмет
- `brand` (string) — Бренд
- `techSize` (string) — Размер
- `Price` (number) — Цена
- `Discount` (number) — Скидка
- `isSupply` (boolean) — Договор поставки (внутренние технологические данные)
- `isRealization` (boolean) — Договор реализации (внутренние технологические данные)
- `SCCode` (string) — Код контракта (внутренние технологические данные)

**Response 400:**

---

### `GET /api/v1/supplier/orders`

**Заказы**

Метод возвращает информацию о заказах.
Данные обновляются раз в 30 минут.

1 строка = 1 заказ = 1 сборочное задание = 1 единица товара.
Для определения заказа рекомендуем использовать поле `srid`.

Информация о заказе хранится 90 дней с момента оформления.

В ответах могут отсутствовать заказы, по которым не подтверждена оплата. Например, заказы с отложенными платежами или оплатой в рассрочку. При этом, если по таким заказам есть продажи, вы можете получить их с помощью [детализаций к отчётам ре...

**Parameters:**

- `dateFrom` (in query, string) **(required)** — Дата и время последнего изменения по заказу.   Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точностью до 
- `?` (in ?, )

**Response 200:**

_(array of objects:)_
- `date` (string) — Дата и время заказа. Это поле соответствует параметру `dateFrom` в запросе, если параметр `flag`=1. Если часовой пояс не указан, то берётся Московское
- `lastChangeDate` (string) — Дата и время обновления информации в сервисе. Это поле соответствует параметру `dateFrom` в запросе, если параметр `flag`=0 или не указан. Если часово
- `warehouseName` (string) — Склад отгрузки
- `warehouseType` (enum) — Values: `Склад WB, Склад продавца`. Тип склада хранения товаров
- `countryName` (string) — Страна
- `oblastOkrugName` (string) — Округ
- `regionName` (string) — Регион
- `supplierArticle` (string) — Артикул продавца
- `nmId` (integer) — Артикул WB
- `barcode` (string) — Баркод
- `category` (string) — Категория
- `subject` (string) — Предмет
- `brand` (string) — Бренд
- `techSize` (string) — Размер товара
- `incomeID` (integer) — Номер поставки
- `isSupply` (boolean) — Договор поставки
- `isRealization` (boolean) — Договор реализации
- `totalPrice` (number) — Цена без скидок
- `discountPercent` (integer) — Скидка продавца, %
- `spp` (number) — Скидка WB, %
- `finishedPrice` (number) — Цена с учетом всех скидок, кроме суммы по WB Кошельку
- `priceWithDisc` (number) — Цена со скидкой продавца, в том числе со скидкой WB Клуба
- `isCancel` (boolean) — Отмена заказа:   - `true` — заказ отменен
- `cancelDate` (string) — Дата и время отмены заказа. Если заказ не был отменен, то "0001-01-01T00:00:00".Если часовой пояс не указан, то берётся Московское время UTC+3.
- `sticker` (string) — ID стикера
- `gNumber` (string) — ID корзины покупателя. Заказы одной транзакции будут иметь одинаковый `gNumber`
- `srid` (string) — Уникальный ID заказа.  Примечание для использующих API Маркетплейс: `srid` равен `rid` в ответах методов сборочных заданий.

**Response 400:**

---

### `GET /api/v1/supplier/sales`

**Продажи**

Метод возвращает информацию о продажах и возвратах.
Данные обновляются раз в 30 минут.

1 строка = 1 заказ = 1 сборочное задание = 1 единица товара.
Для определения заказа рекомендуем использовать поле `srid`.

Информация о заказе хранится 90 дней с момента оформления.

  Данные этого отчёта являются предварительными и служат для оперативного мониторинга

  - В ответах могут отсутствовать заказы, по которым не подтверждена оплата, даже если эти заказы есть в детализациях к отчётам реализации. На...

**Parameters:**

- `dateFrom` (in query, string) **(required)** — Дата и время последнего изменения по продаже/возврату.   Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точ
- `?` (in ?, )

**Response 200:**

_(array of objects:)_
- `date` (string) — Дата и время продажи. Это поле соответствует параметру `dateFrom` в запросе, если параметр `flag`=1. Если часовой пояс не указан, то берётся Московско
- `lastChangeDate` (string) — Дата и время обновления информации в сервисе. Это поле соответствует параметру `dateFrom` в запросе, если параметр `flag`=0 или не указан. Если часово
- `warehouseName` (string) — Склад отгрузки
- `warehouseType` (enum) — Values: `Склад WB, Склад продавца`. Тип склада хранения товаров
- `countryName` (string) — Страна
- `oblastOkrugName` (string) — Округ
- `regionName` (string) — Регион
- `supplierArticle` (string) — Артикул продавца
- `nmId` (integer) — Артикул WB
- `barcode` (string) — Баркод
- `category` (string) — Категория
- `subject` (string) — Предмет
- `brand` (string) — Бренд
- `techSize` (string) — Размер товара
- `incomeID` (integer) — Номер поставки
- `isSupply` (boolean) — Договор поставки
- `isRealization` (boolean) — Договор реализации
- `totalPrice` (number) — Цена без скидок
- `discountPercent` (integer) — Скидка продавца, %
- `spp` (number) — Скидка WB, %
- `paymentSaleAmount` (integer) — Скидка за оплату WB Кошельком, ₽
- `forPay` (number) — К перечислению продавцу. Синхронизация данных занимает до 24 часов, в течение этого времени в поле может отображаться значение `0`
- `finishedPrice` (number) — Фактическая цена с учётом всех скидок (к взиманию с покупателя). Синхронизация данных занимает до 24 часов, в течение этого времени в поле может отобр
- `priceWithDisc` (number) — Цена со скидкой продавца, в том числе со скидкой WB Клуба, от которой рассчитывается сумма к перечислению продавцу `forPay`. Синхронизация данных зани
- `saleID` (string) — Уникальный ID продажи/возврата - `S**********` — продажа - `R**********` — возврат (на склад WB)
- `sticker` (string) — ID стикера
- `gNumber` (string) — ID корзины покупателя. Заказы одной транзакции будут иметь одинаковый `gNumber`
- `srid` (string) — Уникальный ID заказа.  Примечание для использующих API Маркетплейс: `srid` равен `rid` в ответах методов сборочных заданий.

**Response 400:**

---

## Отчёт о возвратах и перемещении товаров

### `GET /api/v1/analytics/goods-return`

**Получить отчёт**

Метод возвращает отчёт о [возвратах товаров продавцу](https://seller.wildberries.ru/analytics-reports/goods-return). 

Можно получить отчёт максимум за 31 день.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Сервисный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос ...

**Parameters:**

- `dateFrom` (in query, string) **(required)** — Дата начала отчётного периода
- `dateTo` (in query, string) **(required)** — Дата окончания отчётного периода

**Response 200:**

- `report` (array[object]) — Отчёт

---

## Отчёт о товарах c обязательной маркировкой

### `POST /api/v1/analytics/excise-report`

**Получить отчёт**

Метод возвращает отчёт с [операциями по товарам с обязательной маркировкой](https://seller.wildberries.ru/analytics-reports/excise-report).

Данный отчёт можно сохранить в [формате таблиц](https://dev.wildberries.ru/cases/1).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 5 ч | 10 запросов | 30 мин | 10 запросов |
| Сервисный | 5 ч | 10 запросов | 30...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )

**Request body:**

- `countries` (array[string]) — Код стран по стандарту ISO 3166-2. Чтобы получить данные по всем странам, оставьте параметр пустым

**Response 200:**

- `response` (object)
  - `data` (object)

---

## Отчёт об остатках на складах

### `GET /api/v1/warehouse_remains`

**Создать отчёт**

Метод создаёт [задание на генерацию](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1status/get) отчёта об [остатках на складах WB](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1download/get).

Параметры `groupBy` и `filter` (группировки и фильтры) можно задать в любой комбинации — аналогично [версии](https://seller.wildberries.ru/analytics-reports/warehouse-remains) в ли...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа `subjectName` и `warehouseName`:   - `ru` — русский   - `en` — английский   - `zh` — китайский. Значения `warehouseName` на английск
- `groupByBrand` (in query, boolean) — Разбивка по брендам
- `groupBySubject` (in query, boolean) — Разбивка по предметам
- `groupBySa` (in query, boolean) — Разбивка по артикулам продавца
- `groupByNm` (in query, boolean) — Разбивка по артикулам WB. Если `groupByNm=true`, в ответе будет поле `volume`
- `groupByBarcode` (in query, boolean) — Разбивка по баркодам
- `groupBySize` (in query, boolean) — Разбивка по размерам
- `filterPics` (in query, integer) — Фильтр по фото:   - `-1` — без фото   - `0` — не применять фильтр   - `1` — с фото
- `filterVolume` (in query, integer) — Фильтр по объёму:   - `-1` — без габаритов   - `0` — не применять фильтр   - `3` — свыше трёх литров

**Response 200:**

- `data` (object)
  - `taskId` (string) — ID задания на генерацию

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `GET /api/v1/warehouse_remains/tasks/{task_id}/status`

**Проверить статус**

Метод возвращает статус [задания на генерацию](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains/get) отчёта об [остатках на складах WB](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1download/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 5 сек ...

**Parameters:**

- `task_id` (in path, string) **(required)** — ID задания на генерацию

**Response 200:**

- `data` (object)
  - `id` (string) — ID задания
  - `status` (string) — Статус задания:   * `new` — новое   * `processing` —  обрабатывается   * `done` — отчёт готов   * `purged` — отчёт удалён   * `canceled` — отклонено

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `GET /api/v1/warehouse_remains/tasks/{task_id}/download`

**Получить отчёт**

Метод возвращает отчёт об [остатках на складах WB](https://seller.wildberries.ru/analytics-reports/warehouse-remains) по ID [задания на генерацию](/openapi/reports#tag/Otchyot-ob-ostatkah-na-skladah/paths/~1api~1v1~1warehouse_remains/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Сервисный | 1 мин | 1 зап...

**Parameters:**

- `task_id` (in path, string) **(required)** — ID задания на генерацию

**Response 200:**

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

## Отчёты об удержаниях

### `GET /api/analytics/v1/measurement-penalties`

**Удержания за занижение габаритов упаковки**

Operation ID: `getMeasurementPenalties`

Метод возвращает отчёт об [удержаниях за занижение габаритов упаковки](https://seller.wildberries.ru/analytics-reports/dimensions-penalties)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Сервисный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Базовый | 6 ч | 1 запрос | 6 ч | 1 запрос |

**Parameters:**

- `dateFrom` (in query, string) — Начало отчётного периода. По умолчанию используется дата, когда были впервые получены данные для отчёта
- `dateTo` (in query, string) **(required)** — Конец отчётного периода
- `limit` (in query, integer) **(required)** — Количество удержаний в ответе
- `offset` (in query, integer) — Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента

**Response 200:**

- `data` (object) **(required)** — Данные ответа
  - `reports` (array[object]) **(required)** — Удержания
  - `total` (integer) **(required)** — Количество удержаний в отчёте. Без учёта `limit` и `offset`

**Response 400:**

- `title` (string) — Заголовок ошибки
- `status` (integer) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) — Заголовок ошибки
- `status` (integer) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---

### `GET /api/analytics/v1/warehouse-measurements`

**Замеры склада**

Operation ID: `getWarehouseMeasurements`

Метод возвращает отчёт о [замерах склада](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/warehouse-measurements)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Сервисный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Базовый | 6 ч | 1 запрос | 6 ч | 1 запрос |

**Parameters:**

- `dateFrom` (in query, string) — Начало отчётного периода. По умолчанию используется дата, когда были впервые получены данные для отчёта
- `dateTo` (in query, string) **(required)** — Конец отчётного периода
- `limit` (in query, integer) **(required)** — Количество замеров в ответе
- `offset` (in query, integer) — Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента

**Response 200:**

- `data` (object) **(required)** — Данные ответа
  - `reports` (array[object]) **(required)** — Замеры
  - `total` (integer) **(required)** — Количество замеров в отчёте. Без учёта `limit` и `offset`

**Response 400:**

- `title` (string) — Заголовок ошибки
- `status` (integer) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) — Заголовок ошибки
- `status` (integer) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---

### `GET /api/analytics/v1/deductions`

**Подмены и неверные вложения**

Operation ID: `getDeductions`

Метод возвращает отчёт об удержаниях за [подмены и неверные вложения](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/retentions)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Сервисный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Базовый | 1 ч | 4 запроса | 15 мин | 1 запрос |

**Parameters:**

- `dateFrom` (in query, string) — Начало отчётного периода. По умолчанию используются дата и время, когда были впервые получены данные для отчёта
- `dateTo` (in query, string) **(required)** — Конец отчётного периода
- `sort` (in query, enum: nmId, dtBonus, bonusSumm) — Сортировка: - `nmId` — по артикулу WB - `dtBonus` — по дате и времени удержания - `bonusSumm` — по сумме удержания
- `order` (in query, enum: desc, asc) — Порядок выдачи: - `desc` — по убыванию - `asc` — по возрастанию
- `limit` (in query, integer) **(required)** — Количество удержаний в ответе
- `offset` (in query, integer) — Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента

**Response 400:**

- `title` (string) — Заголовок ошибки
- `status` (integer) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) — Заголовок ошибки
- `status` (integer) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---

### `GET /api/v1/analytics/antifraud-details`

**Самовыкупы**

Метод возвращает отчёт об удержаниях за самовыкупы. Отчёт формируется каждую неделю по средам, до 7:00 по московскому времени, и содержит данные за одну неделю.

Удержание за самовыкуп — 30% от стоимости товаров.
Минимальная сумма всех удержаний — 100 000 ₽, если за неделю в ПВЗ привезли ваших товаров больше, чем на сумму 100 000 ₽.

Данные доступны с августа 2023.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интерва...

**Parameters:**

- `?` (in ?, )

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

### `GET /api/v1/analytics/goods-labeling`

**Маркировка товара**

Метод возвращает отчёт о штрафах за отсутствие обязательной маркировки товаров.

В отчёте представлены фотографии товаров, на которых маркировка отсутствует либо не считывается.

Можно получить данные максимум за 31 день. Данные доступны с марта 2024.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Сервисный ...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )

---

## Платное хранение

### `GET /api/v1/paid_storage`

**Создать отчёт**

Метод создаёт [задание на генерацию](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1status/get) отчёта о [платном хранении](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1download/get).

Можно получить отчёт максимум за 8 дней.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Перс...

**Parameters:**

- `dateFrom` (in query, string) **(required)** — Начало отчётного периода в формате RFC3339. Можно передать дату или дату со временем. Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59`   * `2019-0
- `dateTo` (in query, string) **(required)** — Конец отчётного периода в формате RFC3339. Можно передать дату или дату со временем. Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59`   * `2019-06

**Response 200:**

- `data` (object)
  - `taskId` (string) — ID задания на генерацию

---

### `GET /api/v1/paid_storage/tasks/{task_id}/status`

**Проверить статус**

Метод возвращает статус [задания на генерацию](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage/get) отчёта о [платном хранении](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1download/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 5 сек | 1 запрос | 5 сек | 5 запросов |
| Сервисный...

**Parameters:**

- `task_id` (in path, string) **(required)** — ID задания на генерацию

**Response 200:**

- `data` (object)
  - `id` (string) — ID задания
  - `status` (string) — Статус задания:   * `new` — новое   * `processing` —  обрабатывается   * `done` — отчёт готов   * `purged` — отчёт удалён   * `canceled` — отклонено

---

### `GET /api/v1/paid_storage/tasks/{task_id}/download`

**Получить отчёт**

Метод возвращает отчёт о [платном хранении](https://seller.wildberries.ru/analytics-reports/paid-storage/storage) по ID [задания на генерацию](/openapi/reports#tag/Platnoe-hranenie/paths/~1api~1v1~1paid_storage/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Сервисный | 1 мин | 1 запрос | 1 мин | 1 запрос ...

**Parameters:**

- `task_id` (in path, string) **(required)** — ID задания на генерацию

**Response 200:**

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `requestId` (string) — Уникальный ID запроса
- `title` (string) — Заголовок ошибки

---

## Продажи по регионам

### `GET /api/v1/analytics/region-sale`

**Получить отчёт**

Метод возвращает отчёт с [данными продаж, сгруппированных по регионам стран](https://seller.wildberries.ru/analytics-reports/region-sale).

Можно получить отчёт максимум за 31 день.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 10 сек | 1 запрос | 10 сек | 5 запросов |
| Сервисный | 10 сек | 1 запрос | 10 сек | 5 запросов |
| Базовый | 1 ч | 1 запро...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )

---

## Скрытые товары

### `GET /api/v1/analytics/banned-products/blocked`

**Заблокированные карточки**

Метод возвращает список [заблокированных карточек товаров продавца](https://seller.wildberries.ru/analytics-reports/banned-products) с причинами блокировки.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 10 сек | 1 запрос | 10 сек | 6 запросов |
| Сервисный | 10 сек | 1 запрос | 10 сек | 6 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `sort` (in query, enum: brand, nmId, title, vendorCode, reason) **(required)** — Сортировка - `brand` — по бренду - `nmId` — по артикулу WB - `title` — по наименованию товара - `vendorCode` — по артикулу продавца - `reason` — по пр
- `order` (in query, enum: desc, asc) **(required)** — Порядок выдачи - `desc` — от наибольшего числового значения к наименьшему, от последнего по алфавиту значения к первому - `asc` — от наименьшего число

**Response 200:**

- `report` (array[object]) — Отчёт

**Response 400:**

- `title` (string) — Заголовок ошибки
- `status` (number) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---

### `GET /api/v1/analytics/banned-products/shadowed`

**Скрытые из каталога**

Метод возвращает список [товаров продавца, скрытых из каталога](https://seller.wildberries.ru/analytics-reports/banned-products/shadowed).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 10 сек | 1 запрос | 10 сек | 6 запросов |
| Сервисный | 10 сек | 1 запрос | 10 сек | 6 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `sort` (in query, enum: brand, nmId, title, vendorCode, nmRating) **(required)** — Сортировка - `brand` — по бренду - `nmId` — по артикулу WB - `title` — по наименованию товара - `vendorCode` — по артикулу продавца - `nmRating` — по 
- `order` (in query, enum: desc, asc) **(required)** — Порядок выдачи - `desc` — от наибольшего числового значения к наименьшему, от последнего по алфавиту значения к первому - `asc` — от наименьшего число

**Response 200:**

- `report` (array[object]) — Отчёт

**Response 400:**

- `title` (string) — Заголовок ошибки
- `status` (number) — HTTP статус-код
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---


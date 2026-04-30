# Аналитика и данные

Узнать больше об аналитике и данных можно в [справочном центре](https://seller.wildberries.ru/instructions/ru/ru/subcategory/seller-analytics)

В разделе описаны методы получения:
  1. [Воронки продаж](/openapi/analytics#tag/Voronka-prodazh)
  2. [Поисковых запросов по вашим товарам](/openapi/analytics#tag/Poiskovye-zaprosy-po-vashim-tovaram)
  3. [Истории остатков](/openapi/analytics#tag/Istoriya-ostatkov)
  4. [Аналитики продавца в формате CSV](/openapi/analytics#tag/Analitika-prodavca-CSV)

## Аналитика продавца CSV

### `POST /api/v2/nm-report/downloads`

**Создать отчёт**

Метод создаёт задание на генерацию отчёта с расширенной аналитикой продавца. 

Вы можете создать CSV-версии отчётов по [воронке продаж](/openapi/analytics#tag/Voronka-prodazh) или [параметрам поиска](/openapi/analytics#tag/Poiskovye-zaprosy-po-vashim-tovaram) с группировкой по:
  * артикулам WB
  * предметам, брендам и ярлыкам

В отчётах по воронке продаж можно группировать данные по дням, неделям или месяцам.

Также можете создать CSV-версии отчётов по [текстам поисковых запросов](/openapi/anal...

**Request body:**

**Response 200:**

- `data` (string) **(required)** — Уведомление, что началась генерация отчёта

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) — Заголовок ошибки
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

**Response 429:**

---

### `GET /api/v2/nm-report/downloads`

**Получить список отчётов**

Метод возвращает список отчётов с расширенной аналитикой продавца. Ответ содержит ID [созданных отчётов](/openapi/analytics#tag/Analitika-prodavca-CSV/paths/~1api~1v2~1nm-report~1downloads/post) и статусы генерации.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 3 запроса | 20 сек | 3 запроса |
| Сервисный | 1 мин | 3 запроса | 20 сек | 3 зап...

**Parameters:**

- `filter[downloadIds]` (in query, array) — ID отчёта

**Response 200:**

- `data` (array[object]) **(required)**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) — Заголовок ошибки
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---

### `POST /api/v2/nm-report/downloads/retry`

**Сгенерировать отчёт повторно**

Метод создает повторное [задание на генерацию](/openapi/analytics#tag/Analitika-prodavca-CSV/paths/~1api~1v2~1nm-report~1downloads/post) отчёта с расширенной аналитикой продавца. Необходимо, если при генерации отчёта вы [получили статус](/openapi/analytics#tag/Analitika-prodavca-CSV/paths/~1api~1v2~1nm-report~1downloads/get) `FAILED`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | ---...

**Request body:**

- `downloadId` (string(uuid)) — ID отчёта

**Response 200:**

- `data` (string) **(required)** — Уведомление, что началась повторная генерация отчёта

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) — Заголовок ошибки
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---

### `GET /api/v2/nm-report/downloads/file/{downloadId}`

**Получить отчёт**

Метод возвращает отчёт с расширенной аналитикой продавца по ID [задания на генерацию](/openapi/analytics#tag/Analitika-prodavca-CSV/paths/~1api~1v2~1nm-report~1downloads/post).

Можно получить отчёт, который сгенерирован за последние 48 часов.
Отчёт будет загружен внутри архива ZIP в формате CSV.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин |...

**Parameters:**

- `downloadId` (in path, string) **(required)** — ID отчёта

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) — Заголовок ошибки
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB

---

## Воронка продаж

### `POST /api/analytics/v3/sales-funnel/products`

**Статистика карточек товаров за период**

Operation ID: `postSalesFunnelProducts`

Метод формирует отчёт о товарах, сравнивая ключевые показатели за текущий период с аналогичным прошлым.

Данные отчёта обновляются 1 раз в час.

В течение часа после события появляется большая часть данных:
  - о заказах
  - о переходах в карточку товара
  - о добавлениях товаров в корзину

Малая часть этих данных может появляться в течение нескольких дней.

Выкупы, отмены и возвраты отображаются в отчёте за тот день, когда товар был заказан. Например, если заказ был сделан 1 января, а покупател...

**Request body:**

- `selectedPeriod` (object) **(required)**
- `pastPeriod` (object)
- `nmIds` (array[integer]) — Артикулы WB, по которым нужно составить отчёт. Оставьте пустым, чтобы получить отчёт обо всех товарах
- `brandNames` (array[string]) — Список брендов для фильтрации
- `subjectIds` (array[integer]) — Список ID предметов для фильтрации
- `tagIds` (array[integer]) — Список ID ярлыков для фильтрации
- `skipDeletedNm` (boolean) — Скрыть удалённые товары
- `orderBy` (object)
  - `field` (enum) **(required)** — Values: `openCard, addToCart, orderCount, orderSum, buyoutCount, buyoutSum, cancelCount, cancelSum`. Поле для сортировки:   - `openCard` — Перешли в карточку   - `addToCart` — Положили в корзину   - `orderCount` — Заказали товаров, шт   - `orderSum` —
  - `mode` (enum) **(required)** — Values: `asc, desc`. Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию
- `limit` (integer(uint32)) — Количество карточек товара в ответе
- `offset` (integer(uint32)) — Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента

**Response 200:**

- `data` (object) **(required)**

---

### `POST /api/analytics/v3/sales-funnel/products/history`

**Статистика карточек товаров по дням**

Operation ID: `postSalesFunnelProductsHistory`

Метод возвращает статистику карточек товаров по дням или неделям.

Можно получить данные максимум за последнюю неделю.

Данные отчёта обновляются 1 раз в час.

В течение часа после события появляется большая часть данных:
  - о заказах
  - о переходах в карточку товара
  - о добавлениях товаров в корзину

Малая часть этих данных может появляться в течение нескольких дней.

Выкупы, отмены и возвраты отображаются в отчёте за тот день, когда товар был заказан. Например, если заказ был сделан 1 янва...

**Request body:**

- `selectedPeriod` (object) **(required)**
- `nmIds` (array[integer]) **(required)** — Артикулы WB, по которым нужно составить отчёт
- `skipDeletedNm` (boolean) — Скрыть удалённые товары
- `aggregationLevel` (enum) — Values: `day, week`

**Response 200:**

---

### `POST /api/analytics/v3/sales-funnel/grouped/history`

**Статистика групп карточек товаров по дням**

Operation ID: `postSalesFunnelGroupedHistory`

Метод возвращает статистику карточек товаров по дням или неделям.

Карточки товаров сгруппированы по предметам, брендам и ярлыкам.

Можно получить данные максимум за последнюю неделю.

Данные отчёта обновляются 1 раз в час.

В течение часа после события появляется большая часть данных:
  - о заказах
  - о переходах в карточку товара
  - о добавлениях товаров в корзину

Малая часть этих данных может появляться в течение нескольких дней.

Выкупы, отмены и возвраты отображаются в отчёте за тот день...

**Request body:**

- `selectedPeriod` (object) **(required)**
- `brandNames` (array[string]) — Список брендов для фильтрации
- `subjectIds` (array[integer]) — Список ID предметов для фильтрации
- `tagIds` (array[integer]) — Список ID ярлыков для фильтрации
- `skipDeletedNm` (boolean) — Скрыть удалённые товары
- `aggregationLevel` (enum) — Values: `day, week`

**Response 200:**

- `data` (object) **(required)**

---

## История остатков

### `POST /api/analytics/v1/stocks-report/wb-warehouses`

**Остатки на складах WB**

Operation ID: `postV1StocksReportWbWarehouses`

Метод доступен по [типам токенов](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API): Персональный, Сервисный 

Метод возвращает текущие остатки товаров на складах WB.

Данные обновляются 1 раз в 30 минут.

1 строка ответа — данные об 1 размере товара на 1 складе WB.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 3 запроса | 20 сек |...

**Request body:**

- `nmIds` (array[integer]) — Артикулы WB
- `chrtIds` (array[integer]) — ID размеров. Используется только для указанных в массиве `nmIds` артикулов
- `limit` (integer(uint32)) — Количество строк в ответе
- `offset` (integer(uint32)) — Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента

**Response 200:**

- `data` (object) **(required)**
  - `items` (array[object]) **(required)** — Остатки товаров на складах WB по размерам

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/stocks-report/products/groups`

**Данные по группам**

Метод формирует набор данных об остатках по группам товаров.

Группа товаров описывается кортежем `subjectID, brandName, tagID`.

Данные отчёта обновляются 1 раз в час.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 3 запроса | 20 сек | 3 запроса |
| Сервисный | 1 мин | 3 запроса | 20 сек | 3 запроса |
| Базовый | 1 ч | 2 запроса | 30 мин | 1...

**Request body:**

**Response 200:**

- `data` (object) **(required)**
  - `groups` (object) **(required)**
  - `currency` (object) **(required)**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/stocks-report/products/products`

**Данные по товарам**

Метод формирует набор данных об остатках по товарам.

Можно получить данные как по отдельным товарам, так и в рамках всего отчёта — если в запросе отсутствуют фильтры: `nmIDs`, `subjectID`, `brandName`, `tagID`.

Данные отчёта обновляются 1 раз в час.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 3 запроса | 20 сек | 3 запроса |

**Request body:**

**Response 200:**

- `data` (object) **(required)**
  - `items` (array[object]) **(required)** — Множество данных по товарам
  - `currency` (object) **(required)**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/stocks-report/products/sizes`

**Данные по размерам**

Метод формирует набор данных об остатках по размерам товара.

Возможны случаи:
1. Товар имеет размеры и `"includeOffice":true`, тогда в ответе будут данные об остатках по каждому из размеров с вложенной детализацией по складам.
2. Товар имеет размеры и `"includeOffice":false`, тогда в ответе будут данные об остатках по каждому из размеров без вложенной детализации по складам.
3. Товар не имеет размера и `"includeOffice":true`, тогда в ответе будет детализация по складам. Без данных об остатках п...

**Request body:**

- `nmID` (integer(int64)) **(required)** — Артикул WB
- `currentPeriod` (object) **(required)**
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 3 месяцев от текущей даты
  - `end` (string(date)) **(required)** — Дата окончания периода. Не ранее 3 месяцев от текущей даты
- `stockType` (enum) **(required)** — Values: `, wb, mp`
- `orderBy` (object) **(required)**
  - `field` (enum) **(required)** — Values: `ordersCount, ordersSum, avgOrders, buyoutCount, buyoutSum, buyoutPercent, stockCount, stockSum`
  - `mode` (enum) **(required)** — Values: `asc, desc`
- `includeOffice` (boolean) **(required)** — Включить детализацию по складам

**Response 200:**

- `data` (object) **(required)**
  - `offices` (array[object]) — Множество данных по складам
  - `sizes` (array[object]) — Множество данных по размерам товара
  - `currency` (object) **(required)**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/stocks-report/offices`

**Данные по складам**

Метод формирует набор данных об остатках по складам.

Данные по складам продавца приходят в агрегированном виде — по всем сразу, без детализации по конкретным складам — эти записи будут с `"regionName":"Маркетплейс"` и `"offices":[]`.

Данные отчёта обновляются 1 раз в час.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 3 запроса | 20 сек | 3...

**Request body:**

- `nmIDs` (array[integer]) — Список артикулов WB для фильтрации
- `subjectIDs` (array[integer]) — Список ID предметов для фильтрации
- `brandNames` (array[string]) — Список брендов для фильтрации
- `tagIDs` (array[integer]) — Список ID ярлыков для фильтрации
- `currentPeriod` (object) **(required)**
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 3 месяцев от текущей даты
  - `end` (string(date)) **(required)** — Дата окончания периода. Не ранее 3 месяцев от текущей даты
- `stockType` (enum) **(required)** — Values: `, wb, mp`
- `skipDeletedNm` (boolean) **(required)** — Скрыть удалённые товары

**Response 200:**

- `data` (object) **(required)**
  - `regions` (array[object]) — Множество данных по регионам отгрузки
  - `currency` (object) **(required)**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

## Поисковые запросы по вашим товарам

### `POST /api/v2/search-report/report`

**Основная страница**

Метод формирует набор данных для основной страницы отчёта по поисковым запросам с:
 - общей информацией
 - позициями товаров
 - данными по видимости и переходам в карточку
 - данными для таблицы по группам

Для получения дополнительных данных в таблице используйте отдельный запрос для:
 - [пагинации по группам](/openapi/analytics#tag/Poiskovye-zaprosy-po-vashim-tovaram/paths/~1api~1v2~1search-report~1table~1groups/post)
 - [получения по товарам в группе](/openapi/analytics#tag/Poiskovye-zaprosy-...

**Request body:**

- `currentPeriod` (object) **(required)**
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не ранее 365 суток от сегодня
- `pastPeriod` (object)
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не позднее даты перед датой начала `currentPeriod`. Не ранее 365 суток от сегодня
- `nmIds` (array[integer]) — Список артикулов WB для фильтрации
- `subjectIds` (array[integer]) — Список ID предметов для фильтрации
- `brandNames` (array[string]) — Список брендов для фильтрации
- `tagIds` (array[integer]) — Список ID ярлыков для фильтрации
- `positionCluster` (enum) **(required)** — Values: `all, firstHundred, secondHundred, below`
- `orderBy` (object) **(required)**
  - `field` (enum) **(required)** — Values: `avgPosition, openCard, addToCart, openToCart, orders, cartToOrder, visibility, minPrice`. Поле для сортировки:   - `avgPosition` — по средней позиции   - `addToCart` — по добавлениям в корзину   - `openCard` — по открытию карточки (переход 
  - `mode` (enum) **(required)** — Values: `asc, desc`. Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию
- `includeSubstitutedSKUs` (boolean) — Показать данные по прямым запросам с [подменным артикулом](https://seller.wildberries.ru/help-center/article/A-524)
- `includeSearchTexts` (boolean) — Показать данные по поисковым запросам без учёта подменного артикула
- `limit` (integer(uint32)) **(required)** — Количество групп товаров в ответе
- `offset` (integer(uint32)) **(required)** — После какого элемента выдавать данные

**Response 200:**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/search-report/table/groups`

**Пагинация по группам**

Метод формирует дополнительные данные к [основному отчёту](/openapi/analytics#tag/Poiskovye-zaprosy-po-vashim-tovaram/paths/~1api~1v2~1search-report~1report/post) с пагинацией по группам. Пагинация возможна только при наличии фильтра по бренду, предмету или ярлыку.

Дополнительный параметр выбора списка товаров в таблице:
 - `positionCluster` — средняя позиция в поиске

Параметры `includeSubstitutedSKUs` и `includeSearchTexts` не могут одновременно иметь значение `false`.

Данные отчёта обновляю...

**Request body:**

- `currentPeriod` (object) **(required)**
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не ранее 365 суток от сегодня
- `pastPeriod` (object)
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не позднее даты перед датой начала `currentPeriod`. Не ранее 365 суток от сегодня
- `nmIds` (array[integer]) — Список артикулов WB для фильтрации
- `subjectIds` (array[integer]) — Список ID предметов для фильтрации
- `brandNames` (array[string]) — Список брендов для фильтрации
- `tagIds` (array[integer]) — Список ID ярлыков для фильтрации
- `orderBy` (object) **(required)**
  - `field` (enum) **(required)** — Values: `avgPosition, openCard, addToCart, openToCart, orders, cartToOrder, visibility`. Поле для сортировки:   - `avgPosition` — по средней позиции   - `addToCart` — по добавлениям в корзину   - `openCard` — по открытию карточки (переход 
  - `mode` (enum) **(required)** — Values: `asc, desc`. Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию
- `positionCluster` (enum) **(required)** — Values: `all, firstHundred, secondHundred, below`
- `includeSubstitutedSKUs` (boolean) — Показать данные по прямым запросам с [подменным артикулом](https://seller.wildberries.ru/help-center/article/A-524)
- `includeSearchTexts` (boolean) — Показать данные по поисковым запросам без учёта подменного артикула
- `limit` (integer(uint32)) **(required)** — Количество групп товаров в ответе
- `offset` (integer(uint32)) **(required)** — После какого элемента выдавать данные

**Response 200:**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/search-report/table/details`

**Пагинация по товарам в группе**

Метод формирует дополнительные данные к [основному отчёту](/openapi/analytics#tag/Poiskovye-zaprosy-po-vashim-tovaram/paths/~1api~1v2~1search-report~1report/post) с пагинацией по товарам в группе. Пагинация возможна вне зависимости от наличия фильтров.

Фильтры для пагинации по товарам в группе или без фильтров:
 - кортеж `subjectId`,`brandName`,`tagId` — фильтр для группы
 - `nmIds` — фильтр по карточке товара

Дополнительный параметр выбора списка товаров:
 - `positionCluster` — средняя позици...

**Request body:**

- `currentPeriod` (object) **(required)**
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не ранее 365 суток от сегодня
- `pastPeriod` (object)
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не позднее даты перед датой начала `currentPeriod`. Не ранее 365 суток от сегодня
- `subjectId` (integer(int32)) — ID предмета
- `brandName` (string) — Название товара
- `tagId` (integer(int64)) — ID ярлыка
- `nmIds` (array[integer]) — Список артикулов WB
- `orderBy` (object) **(required)**
  - `field` (enum) **(required)** — Values: `avgPosition, openCard, addToCart, openToCart, orders, cartToOrder, visibility, minPrice`. Поле для сортировки:   - `avgPosition` — по средней позиции   - `addToCart` — по добавлениям в корзину   - `openCard` — по открытию карточки (переход 
  - `mode` (enum) **(required)** — Values: `asc, desc`. Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию
- `positionCluster` (enum) **(required)** — Values: `all, firstHundred, secondHundred, below`. Товары с какой средней позицией в поиске показывать в отчёте:   - `all` — все   - `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200   -
- `includeSubstitutedSKUs` (boolean) — Показать данные по прямым запросам с [подменным артикулом](https://seller.wildberries.ru/help-center/article/A-524)
- `includeSearchTexts` (boolean) — Показать данные по поисковым запросам без учёта подменного артикула
- `limit` (integer(uint32)) **(required)** — Количество товаров в ответе
- `offset` (integer(uint32)) **(required)** — После какого элемента выдавать данные

**Response 200:**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/search-report/product/search-texts`

**Поисковые запросы по товару**

Метод формирует топ поисковых запросов по товару.

Параметры выбора поисковых запросов:
 - `limit` — количество запросов, максимум 30. Для тарифов [Джема](https://seller.wildberries.ru/monetization/tariffs) **Продвинутый** и **Премиальный** максимум — 100.
 - `topOrderBy` — способ выбора топа запросов

Параметры `includeSubstitutedSKUs` и `includeSearchTexts` не могут одновременно иметь значение `false`.

Данные отчёта обновляются 1 раз в час.

[Лимит запросов](/openapi/api-information#tag/Vvede...

**Request body:**

- `currentPeriod` (object) **(required)**
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не ранее 365 суток от сегодня
- `pastPeriod` (object)
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не позднее даты перед датой начала `currentPeriod`. Не ранее 365 суток от сегодня
- `nmIds` (array[integer]) **(required)** — Список артикулов WB
- `topOrderBy` (enum) **(required)** — Values: `openCard, addToCart, openToCart, orders, cartToOrder`. Фильтрация по поисковым запросам, по которым больше всего:   - `openCard` — перешли в карточку   - `addToCart` — добавили в корзину   - `openToCart` —
- `includeSubstitutedSKUs` (boolean) — Показать данные по прямым запросам с [подменным артикулом](https://seller.wildberries.ru/help-center/article/A-524)
- `includeSearchTexts` (boolean) — Показать данные по поисковым запросам без учёта подменного артикула
- `orderBy` (object) **(required)**
  - `field` (enum) **(required)** — Values: `avgPosition, openCard, addToCart, openToCart, orders, cartToOrder, visibility`. Поле для сортировки:   - `avgPosition` — по средней позиции   - `addToCart` — по добавлениям в корзину   - `openCard` — по открытию карточки (переход 
  - `mode` (enum) **(required)** — Values: `asc, desc`. Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию
- `limit` (object) **(required)**

**Response 200:**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---

### `POST /api/v2/search-report/product/orders`

**Заказы и позиции по поисковым запросам товара**

Метод формирует данные для таблицы:
  - о заказах по каждому поисковому запросу для конкретного товара
  - о позициях товара в результатах поиска по каждому запросу

Данные указаны в рамках периода для [запрошенного товара](/openapi/analytics#tag/Poiskovye-zaprosy-po-vashim-tovaram/paths/~1api~1v2~1search-report~1product~1search-texts/post) и сгруппированы по дням. Максимальный период — 7 дней.

Данные отчёта обновляются 1 раз в час.

  Можно получить отчёт максимум за последние 365 дней с момен...

**Request body:**

- `period` (object) **(required)**
  - `start` (string(date)) **(required)** — Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня
  - `end` (string(date)) **(required)** — Дата окончания периода. Не ранее 365 суток от сегодня
- `nmId` (integer(uint64)) **(required)** — Артикул WB
- `searchTexts` (array[string]) **(required)** — Поисковые запросы. Для тарифов [Джема](https://seller.wildberries.ru/monetization/tariffs) **Продвинутый** и **Премиальный** максимум — 100

**Response 200:**

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

**Response 403:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — Уникальный ID запроса
- `origin` (string) **(required)** — ID внутреннего сервиса WB

---


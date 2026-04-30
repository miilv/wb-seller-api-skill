# Маркетинг и продвижение

Узнать больше о маркетинге и продвижении можно в [справочном центре](https://seller.wildberries.ru/instructions/category/59d92bd3-6ea0-40f2-b762-ca8835d7d42e?goBackOption=prevRoute&categoryId=479385c6-de01-4b4d-ad4e-ed941e65582e)

Методы маркетинга и продвижения позволяют:
  1. Получать информацию о кампаниях [продвижения](/openapi/promotion#tag/Kampanii) и [медиакампаниях](/openapi/promotion#tag/Media).
  2. [Создавать](/openapi/promotion#tag/Sozdanie-kampanij) и [управлять](/openapi/promotion#tag/Upravlenie-kampaniyami) кампаниями.
  3. Управлять [финансами](/openapi/promotion#tag/Finansy) кампаний.
  4. Выгружать [статистику](/openapi/promotion#tag/Statistika) кампаний продвижения и медиакампаний.
  5. Работать с [календарём акций](/openapi/promotion#tag/Kalendar-akcij).

Данные синхронизируются с базой раз в 3 минуты. Статусы кампаний меняются раз в минуту. Ставки кампаний меняются раз в 30 секунд.

## Календарь акций

### `GET /api/v1/calendar/promotions`

**Список акций**

Метод возвращает список [акций](/openapi/promotion#tag/Kalendar-akcij/paths/~1api~1v1~1calendar~1promotions~1details/get) в WB с датами и временем проведения.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Календарь акций:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 6 сек | 10 запросов | 600 мс | 5 запросов |
| Сервисный | 6 сек | 10 запросов | 600 мс | 5 запросов |
|...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )

---

### `GET /api/v1/calendar/promotions/details`

**Детальная информация об акциях**

Метод возвращает подробную информацию об [акции](/openapi/promotion#tag/Kalendar-akcij/paths/~1api~1v1~1calendar~1promotions~1details/get) по ID.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Календарь акций:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 6 сек | 10 запросов | 600 мс | 5 запросов |
| Сервисный | 6 сек | 10 запросов | 600 мс | 5 запросов |
| Базовый | 1 ...

**Parameters:**

- `?` (in ?, )

---

### `GET /api/v1/calendar/promotions/nomenclatures`

**Список товаров для участия в акции**

Метод формирует список товаров, подходящих для участия в [акции](/openapi/promotion#tag/Kalendar-akcij/paths/~1api~1v1~1calendar~1promotions~1details/get). Эти товары можно добавить в акцию с помощью [отдельного метода](/openapi/promotion#tag/Kalendar-akcij/paths/~1api~1v1~1calendar~1promotions~1upload/post).

  Данный метод неприменим для автоакций.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Календарь акций:

| Пе...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )

---

### `POST /api/v1/calendar/promotions/upload`

**Добавить товар в акцию**

Метод создаёт задание на загрузку товара в [акцию](/openapi/promotion#tag/Kalendar-akcij/paths/~1api~1v1~1calendar~1promotions~1details/get).

Состояние загрузки можно проверить с помощью [отдельных методов](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1history~1tasks/get).

  Данный метод неприменим для автоакций.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Календарь акций:

| Тип | Период | Лимит ...

---

## Кампании

### `GET /adv/v1/promotion/count`

**Списки кампаний**

Метод возвращает списки всех [рекламных кампаний](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get) продавца с их ID. Кампании сгруппированы по типу и статусу, у каждой указана дата последнего изменения.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Сервисный | 1 сек | 5 запросов | 200...

**Response 200:**

- `adverts` (array[object]) — Данные по кампаниям
- `all` (integer) — Общее количество кампаний всех статусов и типов

---

### `GET /api/advert/v2/adverts`

**Информация о кампаниях**

Метод возвращает информацию о рекламных кампаниях с единой или ручной ставкой по их статусам, типам оплаты и ID.

 
[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `ids` (in query, string) — ID кампаний, максимум 50
- `statuses` (in query, string) — Статусы кампаний: - `-1` — удалена, процесс удаления будет завершён в течение 10 минут - `4` — готова к запуску - `7` — завершена - `8` — отменена - `
- `payment_type` (in query, enum: cpm, cpc) — Тип оплаты: - `cpm` — за показы - `cpc` — за клик

**Response 200:**

- `adverts` (array[object]) **(required)** — Кампании

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

## Медиа

### `GET /adv/v1/count`

**Количество медиакампаний**

Метод возвращает количество [медиакампаний](/openapi/promotion#tag/Media/paths/~1adv~1v1~1advert/get) продавца с группировкой по статусам.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Сервисный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Response 200:**

- `all` (integer) — Общее количество медиакампаний всех статусов и типов
- `adverts` (object)
  - `type` (integer) — Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам
  - `status` (integer) — Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с возможностью вернуть на модерацию)   - `4` — готова к запуску   - 
  - `count` (integer) — Количество медиакампаний

---

### `GET /adv/v1/adverts`

**Список медиакампаний**

Метод возвращает список всех [медиакампаний](/openapi/promotion#tag/Media/paths/~1adv~1v1~1advert/get) продавца по их типам и статусам.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Сервисный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `status` (in query, integer) — Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с возможностью вернуть на модерацию)   - `4` — готова к запуску   - 
- `type` (in query, integer) — Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам
- `limit` (in query, integer) — Количество кампаний в ответе
- `offset` (in query, integer) — Смещение относительно первой медиакампании
- `order` (in query, string) — Порядок вывода ответа: - `create` — по времени создания медиакампании - `id` — по ID медиакампании
- `direction` (in query, string) — Порядок сортировки: - `desc` — от большего к меньшему - `asc` — от меньшего к большему

**Response 200:**

---

### `GET /adv/v1/advert`

**Информация о медиакампании**

Метод возвращает информацию о кампании [WB Медиа](https://cmp.wildberries.ru/cmpf/list). Вместо карточек товаров в медиакампаниях продвигаются рекламные баннеры продавца на сайте и в приложении WB.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Сервисный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Б...

**Parameters:**

- `id` (in query, integer) **(required)** — ID медиакампании

**Response 200:**

- `advertId` (integer) — ID медиакампании
- `name` (string) — Название медиакампании
- `brand` (string) — Название бренда
- `type` (integer) — Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам
- `status` (integer) — Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с возможностью вернуть на модерацию)   - `4` — готова к запуску   - 
- `createTime` (string(date-time)) — Время создания медиакампании
- `extended` (object)
  - `reason` (string) — Комментарий модератора
  - `expenses` (integer) — Затраты
  - `from` (string(date-time)) — Дата и время начала показа медиакампании
  - `to` (string(date-time)) — Дата и время окончания показа медиакампании
  - `updated_at` (string(date-time)) — Дата и время изменения кампании
  - `price` (integer) — Стоимость размещения по дням для типа `1`
  - `budget` (integer) — Остаток бюджета для типа `2`
  - `operation` (integer) — Источник списания:   - `1` — баланс   - `2` — счёт
  - `contract_id` (integer) — ID контракта, для продавцов на контракте
- `items` (array[object]) — Информация о баннере.  Наличие в ответе тех или иных полей зависит от конфигурации медиакампании.

---

## Поисковые кластеры

### `POST /adv/v0/normquery/get-bids`

**Список ставок поисковых кластеров**

Метод возвращает список поисковых кластеров со ставками по:
  - ID кампаний
  - артикулам WB

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Request body:**

- `items` (array[object]) **(required)**
  - `advert_id` (integer) **(required)** — ID кампании
  - `nm_id` (integer) **(required)** — Артикул WB

**Response 200:**

- `bids` (array[object]) **(required)**
  - `advert_id` (integer) **(required)** — ID кампании
  - `nm_id` (integer) **(required)** — Артикул WB
  - `norm_query` (string) **(required)** — Поисковый кластер
  - `bid` (integer) **(required)** — Текущая ставка за тысячу показов, ₽

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `POST /adv/v0/normquery/bids`

**Установить ставки для поисковых кластеров**

Метод устанавливает ставки на поисковые кластеры.

Можно использовать только для кампаний с:
  - ручной ставкой
  - моделью оплаты `cpm` — за показы

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 2 запроса | 500 мс | 4 запроса |
| Сервисный | 1 сек | 2 запроса | 500 мс | 4 запроса |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Request body:**

- `bids` (array[object]) **(required)**
  - `advert_id` (integer) **(required)** — ID кампании
  - `nm_id` (integer) **(required)** — Артикул WB
  - `norm_query` (string) **(required)** — Поисковый кластер
  - `bid` (integer) **(required)** — Ставка за тысячу показов, ₽

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `DELETE /adv/v0/normquery/bids`

**Удалить ставки поисковых кластеров**

Метод удаляет ставки с поисковых кластеров.

Можно использовать только для кампаний с:
  - ручной ставкой
  - моделью оплаты `cpm` — за показы

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Request body:**

- `bids` (array[object]) **(required)**
  - `advert_id` (integer) **(required)** — ID кампании
  - `nm_id` (integer) **(required)** — Артикул WB
  - `norm_query` (string) **(required)** — Поисковый кластер
  - `bid` (integer) **(required)** — Ставка за тысячу показов, ₽

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `POST /adv/v0/normquery/get-minus`

**Список минус-фраз кампаний**

Метод возвращает список минус-фраз по:
  - ID кампаний
  - артикулам WB

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Request body:**

- `items` (array[object]) **(required)**
  - `advert_id` (integer) **(required)** — ID кампании
  - `nm_id` (integer) **(required)** — Артикул WB

**Response 200:**

- `items` (array[object])
  - `advert_id` (integer) — ID кампании
  - `nm_id` (integer) — Артикул WB
  - `norm_queries` (array[string]) — Список минус-фраз

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `POST /adv/v0/normquery/set-minus`

**Установка и удаление минус-фраз**

Метод устанавливает и удаляет минус-фразы в кампаниях c единой и ручной ставкой.

  Отправка пустого массива удаляет все минус-фразы

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Request body:**

- `advert_id` (integer) **(required)** — ID кампании
- `nm_id` (integer) **(required)** — Артикул WB
- `norm_queries` (array[string]) **(required)**

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `POST /adv/v0/normquery/list`

**Списки активных и неактивных поисковых кластеров**

Метод возвращает списки активных и неактивных поисковых кластеров, по которым было не меньше 100 показов.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 10 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Request body:**

- `items` (array[object]) **(required)**
  - `advertId` (integer(int64)) **(required)** — ID кампании
  - `nmId` (integer(int64)) **(required)** — Артикул WB

**Response 200:**

- `items` (array[object]) **(required)**
  - `advertId` (integer(int64)) — ID кампании
  - `nmId` (integer(int64)) — Артикул WB
  - `normQueries` (object)

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

## Создание кампаний

### `POST /api/advert/v1/bids/min`

**Минимальные ставки для карточек товаров**

Метод возвращает минимальные ставки для карточек товаров в копейках по типу оплаты и местам размещения.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 20 запросов | 3 сек | 5 запросов |
| Сервисный | 1 мин | 20 запросов | 3 сек | 5 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Request body:**

- `advert_id` (integer(int64)) **(required)** — ID кампании
- `nm_ids` (array[integer]) **(required)** — Список артикулов WB
- `payment_type` (enum) **(required)** — Values: `cpm, cpc`. Тип оплаты:       - `cpm` — за показы       - `cpc` — за клик
- `placement_types` (array[string]) **(required)** — Места размещения:   - `search` — поиск   - `recommendation` — рекомендации   - `combined` — поиск и рекомендации

**Response 200:**

- `bids` (array[object]) **(required)** — Список карточек товаров со ставками

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `POST /adv/v2/seacat/save-ad`

**Создать кампанию**

Метод создаёт кампанию:
  - с ручной ставкой для продвижения товаров в поиске и/или рекомендациях
  - с единой ставкой для продвижения товаров одновременно в поиске и рекомендациях

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 5 запросов | 12 сек | 5 запросов |
| Сервисный | 1 мин | 5 запросов | 12 сек | 5 запросов |
| Базовый | 1 ч | 5 запр...

**Request body:**

- `name` (string) — Название кампании
- `nms` (array[integer]) — Карточки товаров для кампании. Доступные карточки товаров можно получить с помощью метода [Карточки товаров для кампаний](./promotion#tag/Sozdanie-kam
- `bid_type` (enum) — Values: `manual, unified`. Тип ставки:   - `manual` — ручная   - `unified` — единая
- `payment_type` (enum) — Values: `cpm, cpc`. Тип оплаты: - `cpm` — за показы - `cpc` — за клик. При создании с этим типом оплаты в кампании автоматически устанавливается минимальная ставка
- `placement_types` (array[string]) — Места размещения:   - `search` — в поиске   - `recommendations` — в рекомендациях  Укажите только для кампании с ручной ставкой

**Response 200:**

**Response 400:**

---

### `GET /adv/v1/supplier/subjects`

**Предметы для кампаний**

Метод возвращает список [предметов](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1all/get), которые можно добавить в рекламную [кампанию](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 12 сек | 1 запрос | 12 сек | 5 запросов |
| С...

**Parameters:**

- `payment_type` (in query, string) — Тип оплаты: - `cpm` — за показы - `cpc` — за клик

**Response 200:**

---

### `POST /adv/v2/supplier/nms`

**Карточки товаров для кампаний**

Метод возвращает список [карточек товаров](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1v2~1get~1cards~1list/post), которые можно добавить в рекламную [кампанию](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get). Для получения карточек необходимы ID [предметов](/openapi/promotion#tag/Sozdanie-kampanij/paths/~1adv~1v1~1supplier~1subjects/get), также доступных для добавления в кампанию.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaproso...

**Request body:**

**Response 200:**

---

## Статистика

### `POST /adv/v0/normquery/stats`

**Статистика поисковых кластеров**

Метод формирует статистику по поисковым кластерам за указанный период.

Можно использовать для кампаний с моделями оплаты `cpm` — за показы и `cpc` — за клики.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 10 запросов | 6 сек | 20 запросов |
| Сервисный | 1 мин | 10 запросов | 6 сек | 20 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 з...

**Request body:**

- `from` (string(date)) **(required)** — Дата начала периода
- `to` (string(date)) **(required)** — Дата окончания периода
- `items` (array[object]) **(required)**

**Response 200:**

- `stats` (array[object]) **(required)**
  - `advert_id` (integer) **(required)** — ID кампании
  - `nm_id` (integer) **(required)** — Артикул WB
  - `stats` (array[object])

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `GET /adv/v3/fullstats`

**Статистика кампаний**

Метод формирует статистику для кампаний независимо от типа.

Максимальный период в запросе — 31 день.

Для кампаний в статусах `7`, `9` и `11`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 3 запроса | 20 сек | 1 запрос |
| Сервисный | 1 мин | 3 запроса | 20 сек | 1 запрос |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `ids` (in query, string) **(required)** — ID кампаний, максимум 50 значений
- `beginDate` (in query, string) **(required)** — Дата начала интервала
- `endDate` (in query, string) **(required)** — Дата окончания интервала

**Response 200:**

_(array of objects:)_
- `advertId` (integer) **(required)** — ID кампании
- `atbs` (integer) **(required)** — Количество добавлений товаров в корзину
- `boosterStats` (object) — Статистика по бустеру
- `canceled` (integer) **(required)** — Отмены, шт.
- `clicks` (integer) **(required)** — Количество кликов
- `cpc` (number(double)) **(required)** — Средняя стоимость клика, ₽
- `cr` (number(double)) **(required)** — CR (conversion rate) — отношение количества заказов к общему количеству кликов
- `ctr` (number(double)) **(required)** — CTR (click-through rate) — отношение числа кликов к количеству показов в процентах
- `days` (object) **(required)** — Статистика с разбивкой по дням
- `orders` (integer) **(required)** — Количество заказов
- `shks` (integer) **(required)** — Количество заказанных товаров, шт.
- `sum` (number(double)) **(required)** — Затраты, ₽
- `sum_price` (number(double)) **(required)** — Сумма заказов, ₽
- `views` (integer) **(required)** — Количество просмотров

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `POST /adv/v1/stats`

**Статистика медиакампаний**

Метод формирует статистику кампаний сервиса [WB Медиа](https://cmp.wildberries.ru/cmpf/statistics). Статистику можно группировать по датам и/или интервалам.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Сервисный | 1 сек | 10 запросов | 100 мс | 10 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос ...

**Request body:**

**Response 200:**

**Response 400:**

- `error` (string)

---

### `POST /adv/v1/normquery/stats`

**Статистика по поисковым кластерам с детализацией по дням**

Метод формирует статистику по поисковым кластерам за указанный период с детализацией по дням.
Можно использовать для кампаний с моделями оплаты `cpm` — за показы и `cpc` — за клики.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 10 запросов | 6 сек | 20 запросов |
| Сервисный | 1 мин | 10 запросов | 6 сек | 20 запросов |
| Базовый | 1 ч | 2 з...

**Request body:**

- `from` (string(date)) **(required)** — Дата начала периода
- `to` (string(date)) **(required)** — Дата окончания периода периода
- `items` (array[object]) **(required)**

**Response 200:**

- `items` (array[object]) **(required)**
  - `advertId` (integer(int64)) **(required)** — ID кампании
  - `nmId` (integer(int64)) **(required)** — Артикул WB
  - `dailyStats` (array[object]) — Статистика с детализацией по дням

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

## Управление кампаниями

### `GET /adv/v0/delete`

**Удаление кампании**

Метод удаляет [кампании](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get) в статусе `4` — готова к запуску.

После удаления кампания некоторое время будет находиться в статусе `-1` — кампания в процессе удаления. Полное удаление кампании занимает от 3 до 10 минут.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов ...

**Parameters:**

- `id` (in query, integer) **(required)** — ID кампании

**Response 400:**

- `error` (string)

---

### `POST /adv/v0/rename`

**Переименование кампании**

Метод меняет название [кампании](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get). Это можно сделать в любой момент существования кампании.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 зап...

**Request body:**

- `advertId` (integer) **(required)** — ID кампании, в которой меняется название
- `name` (string) **(required)** — Новое название (максимум 100 символов)

---

### `GET /adv/v0/start`

**Запуск кампании**

Метод запускает [кампании](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get) в статусах `4` — готово к запуску — или `11` — пауза.
Чтобы запустить кампанию, проверьте ее бюджет. Если бюджета недостаточно, [пополните его](/openapi/promotion#tag/Finansy/paths/~1adv~1v1~1budget~1deposit/post).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персонал...

**Parameters:**

- `id` (in query, integer) **(required)** — ID кампании

**Response 400:**

- `error` (string)

---

### `GET /adv/v0/pause`

**Пауза кампании**

Метод ставит [кампании](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get) в статусе `9` — активна — на паузу.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Parameters:**

- `id` (in query, integer) **(required)** — ID кампании

**Response 400:**

- `error` (string)

---

### `GET /adv/v0/stop`

**Завершение кампании**

Метод завершает [кампании](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get) в статусах:
  - `4` — готово к запуску
  - `9` — активна
  - `11` — пауза

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Сервисный | 1 сек | 5 запросов | 200 мс | 5 запросов |
| Базовый | 1 ч | 5 запросов | 12 ...

**Parameters:**

- `id` (in query, integer) **(required)** — ID кампании

**Response 400:**

- `error` (string)

---

### `PUT /adv/v0/auction/placements`

**Изменение мест размещения в кампаниях с ручной ставкой**

Метод меняет места размещения в кампаниях с ручной ставкой и моделью оплаты за показы — `cpm`.

Для кампаний в статусах `4`, `9` и `11`.

 
[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 1 запрос | 1 сек | 1 запрос |
| Сервисный | 1 сек | 1 запрос | 1 сек | 1 запрос |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |

**Request body:**

- `placements` (array[object]) **(required)** — Места размещения в кампаниях

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `PATCH /api/advert/v1/bids`

**Изменение ставок в кампаниях**

Метод меняет ставки карточек товаров по артикулам WB в кампаниях:
  - с единой ставкой
  - с ручной ставкой
  - с моделью оплаты `cpc` — за клики

Для кампаний в статусах `4`, `9` и `11`.

В запросе укажите место размещения в параметре `placement`:
  - `combined` — в поиске и рекомендациях для кампаний с единой ставкой
  - `search `или `recommendations` — в поиске или рекомендациях для кампаний с ручной ставкой

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один акка...

**Request body:**

- `bids` (array[object]) **(required)** — Ставки в кампаниях

**Response 200:**

- `bids` (array[object]) **(required)** — Результат отработки запроса

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `PATCH /adv/v0/auction/nms`

**Изменение списка карточек товаров в кампаниях**

Метод добавляет и удаляет карточки товаров в кампаниях.

Для кампаний в статусах `4`, `9` и `11`.

Для добавляемых товаров устанавливается текущая минимальная ставка.

 
[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 1 запрос | 1 сек | 1 запрос |
| Сервисный | 1 сек | 1 запрос | 1 сек | 1 запрос |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запро...

**Request body:**

- `nms` (array[object]) **(required)** — Карточки товаров в кампаниях

**Response 200:**

- `nms` (array[object]) **(required)** — Результат отработки запроса

**Response 400:**

- `detail` (string) **(required)** — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `request_id` (string) **(required)** — Уникальный ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `GET /api/advert/v0/bids/recommendations`

**Рекомендуемые ставки для карточек товаров и поисковых кластеров**

Метод возвращает рекомендуемые ставки для карточек товаров и поисковых кластеров кампании.
Только для кампаний с типом оплаты `cpm` — за показы.

 
[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 5 запросов | 12 сек | 5 запросов |
| Сервисный | 1 мин | 5 запросов | 12 сек | 5 запросов |
| Базовый | 1 ч | 20 запросов | 3 мин | 1 запрос |

**Parameters:**

- `nmId` (in query, integer) **(required)** — Артикул WB
- `advertId` (in query, integer) **(required)** — ID кампании

**Response 200:**

- `advertId` (integer(int64)) — ID кампании
- `base` (object)
  - `competitiveBid` (object)
  - `leadersBid` (object)
  - `top2` (object)
- `nmId` (integer(int64)) — Артикул WB
- `normQueries` (array[object]) — Рекомендуемые ставки для поисковых кластеров
  - `normQuery` (string) — Поисковый кластер
  - `reachMax` (object)
  - `reachMedium` (object)
  - `reachMin` (object)

---

## Финансы

### `GET /adv/v1/balance`

**Баланс**

Метод возвращает информацию о:
  - счёте кабинета Продвижения WB. Его пополняет продавец.
  - балансе — максимальной сумме для оплаты кампании по взаиморасчету: удержании средств из будущих продаж. Баланс пополнить нельзя, он рассчитывается автоматически на основе отчётов по продвижению.
  - бонусных начислениях WB.

Информацию о бюджете кампаний можно получить в [отдельном методе](/openapi/promotion#tag/Finansy/paths/~1adv~1v1~1budget/get).

[Лимит запросов](/openapi/api-information#tag/Vvedeni...

**Response 200:**

- `balance` (integer) — Счёт, ₽
- `net` (integer) — Баланс, ₽
- `bonus` (integer) — Бонусы, ₽
- `cashbacks` (array[object]) — Промо-бонусы

**Response 400:**

---

### `GET /adv/v1/budget`

**Бюджет кампании**

Метод возвращает информацию о бюджете [кампании](/openapi/promotion#tag/Kampanii/paths/~1api~1advert~1v2~1adverts/get) — максимальной сумме затрат на кампанию. Бюджет кампании можно [пополнить](/openapi/promotion#tag/Finansy/paths/~1adv~1v1~1budget~1deposit/post).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 4 запроса | 250 мс | 4 запроса |...

**Parameters:**

- `id` (in query, integer) **(required)** — ID кампании

**Response 200:**

- `cash` (integer) — Поле не используется. Значение всегда 0.
- `netting` (integer) — Поле не используется. Значение всегда 0.
- `total` (integer) — Бюджет кампании, ₽

---

### `POST /adv/v1/budget/deposit`

**Пополнение бюджета кампании**

Метод пополняет [бюджет](/openapi/promotion#tag/Finansy/paths/~1adv~1v1~1budget/get) кампании. 

Чтобы запустить кампанию после пополнения бюджета, используйте метод [Запуск кампании](/openapi/promotion#tag/Upravlenie-kampaniyami/paths/~1adv~1v0~1start/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 1 запрос | 1 сек | 5 запросов |
| Серв...

**Parameters:**

- `id` (in query, integer) **(required)** — ID кампании

**Request body:**

- `sum` (integer) — Общая сумма пополнения бюджета
- `cashback_sum` (integer) — Сумма пополнения бюджета промо-бонусами.  Пополнить можно только определённый процент от общей суммы, указанный в поле `percent` ответа метода получен
- `cashback_percent` (integer) — Процент от суммы пополнения, который можно пополнить промо-бонусами. Нужно указать значение поля percent из ответа метода получения [баланса](./promot
- `type` (integer) — Тип источника пополнения: - `0` — Счёт - `1` — Баланс - `3` — Бонусы
- `return` (boolean) — Флаг возврата ответа (`true` — в ответе вернется обновлённый размер бюджета кампании, `false` или не указать параметр вообще — не вернётся.)

**Response 200:**

**Response 400:**

- `error` (string)

---

### `GET /adv/v1/upd`

**Получение истории затрат**

Метод формирует список фактических затрат на рекламные кампании за заданный период.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 1 запрос | 1 сек | 5 запросов |
| Сервисный | 1 сек | 1 запрос | 1 сек | 5 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `from` (in query, string) **(required)** — Начало интервала
- `to` (in query, string) **(required)** — Конец интервала.   (Минимальный интервал 1 день, максимальный 31)

**Response 200:**

---

### `GET /adv/v1/payments`

**Получение истории пополнений счёта**

Метод возвращает историю пополнений счёта **WB Продвижение** за заданный период.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 1 запрос | 1 сек | 5 запросов |
| Сервисный | 1 сек | 1 запрос | 1 сек | 5 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `from` (in query, string) — Начало интервала
- `to` (in query, string) — Конец интервала.   (Минимальный интервал 1 день, максимальный 31)

**Response 200:**

**Response 400:**

---


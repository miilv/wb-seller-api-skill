# Общение с покупателями

Узнать больше об общении с покупателями можно в [справочном центре](https://seller.wildberries.ru/instructions/category/f7f6c465-dd12-422d-80a0-a6d9562115d5?goBackOption=prevRoute&categoryId=30817062-14cc-4a82-bc78-3600c2b0685b)

С помощью методов общения с покупателями вы можете работать с:
  1. [Вопросами](/openapi/user-communication#tag/Voprosy) и [отзывами](/openapi/user-communication#tag/Otzyvy) покупателей
  2. [Закреплёнными отзывами](/openapi/user-communication#tag/Zakreplyonnye-otzyvy)
  3. [Чатами с покупателями](/openapi/user-communication#tag/Chat-s-pokupatelyami)
  4. [Заявками покупателей на возврат](/openapi/user-communication#tag/Vozvraty-pokupatelyami)

  
    Узнать, как использовать методы в бизнес-кейсах, можно в [инструкции](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-0b26-7620-8d0b-e3050b7cd01d/obshchenie-s-pokupateliami) по работе с разделом Общение с покупателями

## Возвраты покупателями

### `GET /api/v1/claims`

**Заявки покупателей на возврат**

Метод возвращает заявки покупателей на возврат товаров за последние 14 дней. Вы можете [отвечать на эти заявки](/openapi/user-communication#tag/Vozvraty-pokupatelyami/paths/~1api~1v1~1claim/patch).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 20 запросов | 3 сек | 10 запросов |
| Сервисный | 1 мин | 20 запросов | 3 сек | 10 запросов |
| Баз...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )

---

### `PATCH /api/v1/claim`

**Ответ на заявку покупателя**

Метод отправляет ответ на [заявку](/openapi/user-communication#tag/Vozvraty-pokupatelyami/paths/~1api~1v1~1claims/get) покупателя на возврат товаров.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 20 запросов | 3 сек | 10 запросов |
| Сервисный | 1 мин | 20 запросов | 3 сек | 10 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

---

## Вопросы

### `GET /api/v1/new-feedbacks-questions`

**Непросмотренные отзывы и вопросы**

Метод проверяет наличие непросмотренных [вопросов](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) и [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) от покупателей. Если у продавца есть непросмотренные вопросы или отзывы, возвращает `true`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- ...

**Response 200:**

- `data` (object)
  - `hasNewQuestions` (boolean) — Есть ли непросмотренные вопросы:    - `true` — да    - `false` — нет
  - `hasNewFeedbacks` (boolean) — Есть ли непросмотренные отзывы:  - `true` — да  - `false` — нет
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/questions/count-unanswered`

**Неотвеченные вопросы**

Метод возвращает общее количество неотвеченных [вопросов](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) и количество неотвеченных вопросов за сегодня.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек | 3 запроса | 333 мс |...

**Response 200:**

- `data` (object)
  - `countUnanswered` (integer) — Количество неотвеченных вопросов
  - `countUnansweredToday` (integer) — Количество неотвеченных вопросов за сегодня
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/questions/count`

**Количество вопросов**

Метод возвращает количество отвеченных или неотвеченных [вопросов](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) за заданный период.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Ба...

**Parameters:**

- `dateFrom` (in query, integer) — Дата начала периода в формате Unix timestamp
- `dateTo` (in query, integer) — Дата конца периода в формате Unix timestamp
- `isAnswered` (in query, boolean) — Есть ли ответ на вопрос:   - `true` — да   - `false` — нет

**Response 200:**

- `data` (integer) — Количество вопросов
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 400:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/questions`

**Список вопросов**

Метод возвращает список вопросов по заданным фильтрам. Вы можете:
  - получить данные отвеченных и неотвеченных вопросов
  - сортировать вопросы по дате
  - настроить пагинацию и количество вопросов в ответе

  Можно получить максимум 10 000 вопросов в одном ответе

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональн...

**Parameters:**

- `isAnswered` (in query, boolean) **(required)** — Есть ли ответ на вопрос:   - `true` — да   - `false` — нет
- `nmId` (in query, integer) — Артикул WB
- `take` (in query, integer) **(required)** — Количество запрашиваемых вопросов (максимально допустимое значение для параметра - 10 000, при этом сумма значений параметров `take` и `skip` не должн
- `skip` (in query, integer) **(required)** — Количество вопросов для пропуска (максимально допустимое значение для параметра - 10 000, при этом сумма значений параметров `take` и `skip` не должна
- `order` (in query, string) — Сортировка вопросов по дате (`dateAsc`/`dateDesc`)
- `dateFrom` (in query, integer) — Дата начала периода в формате Unix timestamp
- `dateTo` (in query, integer) — Дата конца периода в формате Unix timestamp

**Response 200:**

- `data` (object)
  - `countUnanswered` (integer) — Количество неотвеченных вопросов
  - `countArchive` (integer) — Количество отвеченных вопросов
  - `questions` (array[object]) — Вопросы
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 400:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `PATCH /api/v1/questions`

**Работа с вопросами**

В зависимости от тела запроса, метод позволяет:
  - отметить [вопрос](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) как просмотренный
  - отклонить вопрос
  - ответить на вопрос или отредактировать ответ

  Отредактировать ответ на вопрос можно 1 раз в течение 60 дней после отправки ответа

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всп...

**Request body:**

**Response 200:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 400:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 404:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/question`

**Получить вопрос по ID**

Метод возвращает данные [вопроса](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/get) по его ID. Далее вы можете [работать с этим вопросом](/openapi/user-communication#tag/Voprosy/paths/~1api~1v1~1questions/patch).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс...

**Parameters:**

- `id` (in query, string) **(required)** — ID вопроса

**Response 200:**

- `data` (object)
  - `id` (string) — ID вопроса
  - `text` (string) — Текст вопроса
  - `createdDate` (string(date-time)) — Дата и время создания вопроса
  - `state` (string) — Статус вопроса:   - `none` - вопрос отклонён продавцом (такой вопрос не отображается на портале покупателей)   - `wbRu` - ответ предоставлен, вопрос о
  - `answer` (object) — Ответ
  - `productDetails` (object) — Product information
  - `wasViewed` (boolean) — Просмотрен ли вопрос
  - `isWarned` (boolean) — Признак подозрительного вопроса.  Если `true`, то вопрос опубликован, но на портале продавцов вы увидите баннер **Сообщение подозрительное**
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 422:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

## Закреплённые отзывы

### `GET /api/feedbacks/v1/pins`

**Список закреплённых и откреплённых отзывов**

Метод предоставляет список закреплённых и откреплённых отзывов.

Откреплёнными считаются только отзывы, которые были откреплены автоматически по причинам, указанным в ответе в поле `unpinnedCause`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек |...

**Parameters:**

- `state` (in query, enum: pinned, unpinned) — Закреплён ли отзыв:   - `pinned` — да   - `unpinned` — нет
- `pinOn` (in query, enum: nm, imt) — Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-132
- `imtId` (in query, integer) — ID для [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#obuedinenie-i-razuedin
- `nmId` (in query, integer) — Артикул WB
- `feedbackId` (in query, integer) — ID отзыва
- `dateFrom` (in query, string) — Дата закрепления первого отзыва в списке
- `dateTo` (in query, string) — Дата закрепления последнего отзыва в списке
- `next` (in query, integer) — ID последней операции закрепления (пагинатор)
- `limit` (in query, integer) — Количество отзывов на одной странице (пагинация)

**Response 200:**

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `requestId` (string) **(required)** — ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `POST /api/feedbacks/v1/pins`

**Закрепить отзывы**

Метод позволяет закрепить отзывы в карточке товара или в группе [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#obuedinenie-i-razuedinenie-kartochek-tovarov) карточек. 

Чтобы получить ID отзывов, используйте метод [Список закреплённых и откреплённых отзывов](/openapi/user-communication#tag/Zakreplyonnye-otzyvy/paths/~1api~1feedbacks~1v1~1pins/get).

Метод доступен по [подписке Джем](https://seller.wildberries.ru/monetizati...

**Request body:**

_(array of objects:)_
- `pinMethod` (enum) **(required)** — Values: `tariff, subscription`. Метод закрепления:   - `subscription` — подписка Джем   - `tariff` — тарифная опция
- `pinOn` (enum) **(required)** — Values: `nm, imt`. Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-132
- `feedbackId` (string) **(required)** — ID отзыва

**Response 200:**

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `requestId` (string) **(required)** — ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

**Response 403:**

- `detail` (string) — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `requestId` (string) **(required)** — ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `DELETE /api/feedbacks/v1/pins`

**Открепить отзывы**

Метод позволяет открепить отзывы в карточке товара или в группе [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#obuedinenie-i-razuedinenie-kartochek-tovarov) карточек.

Чтобы получить `pinId` — ID операций закрепления, используйте метод [Список закреплённых и откреплённых отзывов](/openapi/user-communication#tag/Zakreplyonnye-otzyvy/paths/~1api~1feedbacks~1v1~1pins/get).

[Лимит запросов](/openapi/api-information#tag/Vveden...

**Request body:**

**Response 200:**

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `requestId` (string) **(required)** — ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `GET /api/feedbacks/v1/pins/count`

**Количество закреплённых и откреплённых отзывов**

Метод возвращает количество закреплённых и откреплённых отзывов за заданный период.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Parameters:**

- `state` (in query, enum: pinned, unpinned) — Закреплён ли отзыв:   - `pinned` — да   - `unpinned` — нет
- `pinOn` (in query, enum: nm, imt) — Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-132
- `imtId` (in query, integer) — ID для [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#obuedinenie-i-razuedin
- `nmId` (in query, integer) — Артикул WB
- `feedbackId` (in query, integer) — ID отзыва
- `dateFrom` (in query, string) — Дата закрепления первого отзыва в списке
- `dateTo` (in query, string) — Дата закрепления последнего отзыва в списке

**Response 200:**

**Response 400:**

- `detail` (string) — Детали ошибки
- `origin` (string) **(required)** — ID внутреннего сервиса WB
- `requestId` (string) **(required)** — ID запроса
- `status` (integer) **(required)** — HTTP статус-код
- `title` (string) **(required)** — Заголовок ошибки

---

### `GET /api/feedbacks/v1/pins/limits`

**Лимиты закреплённых отзывов**

Метод возвращает лимиты закреплённых отзывов по тарифу и подписке.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос |

**Response 200:**

---

## Отзывы

### `GET /api/v1/feedbacks/count-unanswered`

**Необработанные отзывы**

Метод возвращает:
  - количество необработанных [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) за сегодня и за всё время

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Базовы...

**Response 200:**

- `data` (object)
  - `countUnanswered` (integer) — Количество необработанных отзывов
  - `countUnansweredToday` (integer) — Количество необработанных отзывов за сегодня
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/feedbacks/count`

**Количество отзывов**

Метод возвращает количество обработанных или необработанных [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) за заданный период.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| ...

**Parameters:**

- `dateFrom` (in query, integer) — Дата начала периода в формате Unix timestamp
- `dateTo` (in query, integer) — Дата конца периода в формате Unix timestamp
- `isAnswered` (in query, boolean) — Обработан ли отзыв:   - `true` — да   - `false` — нет

**Response 200:**

- `data` (integer) — Количество отзывов
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 400:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/feedbacks`

**Список отзывов**

Метод возвращает список отзывов по заданным фильтрам. Вы можете:
  - получить данные обработанных и необработанных отзывов
  - сортировать отзывы по дате
  - настроить пагинацию и количество отзывов в ответе

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный...

**Parameters:**

- `isAnswered` (in query, boolean) **(required)** — Обработан ли отзыв:   - `true` — да   - `false` — нет
- `nmId` (in query, integer) — Артикул WB
- `take` (in query, integer) **(required)** — Количество отзывов (max. 5 000)
- `skip` (in query, integer) **(required)** — Количество отзывов для пропуска (max. 199990)
- `order` (in query, enum: dateAsc, dateDesc) — Сортировка отзывов по дате (dateAsc/dateDesc)
- `dateFrom` (in query, integer) — Дата начала периода в формате Unix timestamp
- `dateTo` (in query, integer) — Дата конца периода в формате Unix timestamp

**Response 200:**

- `data` (object)
  - `countUnanswered` (integer) — Количество необработанных отзывов
  - `countArchive` (integer) — Количество обработанных отзывов
  - `feedbacks` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 400:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `POST /api/v1/feedbacks/answer`

**Ответить на отзыв**

Метод позволяет ответить на [отзыв](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) покупателя.

  ID отзыва не валидируется. Если в запросе вы передали некорректный ID, вы не получите ошибку.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| С...

**Request body:**

- `id` (string) **(required)** — ID отзыва
- `text` (string) **(required)** — Текст ответа

**Response 400:**

- `title` (string) — Заголовок ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB
- `detail` (string) — Детали ошибки

---

### `PATCH /api/v1/feedbacks/answer`

**Отредактировать ответ на отзыв**

Метод позволяет отредактировать уже отправленный [ответ на отзыв](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks~1answer/post) покупателя.

Отредактировать ответ можно только один раз в течение 60 дней c момента отправки.

  ID отзыва не валидируется. Если в запросе вы передали некорректный ID, вы не получите ошибку.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Л...

**Request body:**

- `id` (string) **(required)** — ID отзыва
- `text` (string) **(required)** — Текст ответа

---

### `POST /api/v1/feedbacks/order/return`

**Возврат товара по ID отзыва**

Метод запрашивает возврат товара, по которому оставлен [отзыв](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get).

Возврат доступен для отзывов с полем `"isAbleReturnProductOrders": true`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисн...

**Request body:**

- `feedbackId` (string) — ID отзыва

**Response 200:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 400:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 422:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/feedback`

**Получить отзыв по ID**

Метод возвращает данные [отзыва](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get) по его ID.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Сервисный | 1 сек | 3 запроса | 333 мс | 6 запросов |
| Базовый | 1 ч | 5 запросов | 12 мин | 1 запрос...

**Parameters:**

- `id` (in query, string) **(required)** — ID отзыва

**Response 200:**

- `data` (object)
  - `id` (string) — ID отзыва
  - `text` (string) — Текст отзыва
  - `pros` (string) — Достоинства товара
  - `cons` (string) — Недостатки товара
  - `matchingSize` (string) — Соответствие заявленного размера реальному.  Возможные значения: - ` ` - для безразмерных товаров - `ок` - соответствует размеру - `smaller` - маломер
  - `productValuation` (integer) — Оценка товара
  - `createdDate` (string(date-time)) — Дата и время создания отзыва
  - `answer` (object) — Структура ответа
  - `state` (string) — Статус отзыва:   - `none` - не обработан (новый)   - `wbRu` - обработан
  - `productDetails` (object) — Product information
  - `photoLinks` (array[object]) — Массив структур фотографий
  - `userName` (string) — Имя автора отзыва
  - `orderStatus` (string) — Статус заказа.  Возможные значения: - `buyout` — выкуплен - `rejected` — отказались - `returned` — возврат - `notSpecified` — статус не присвоен
  - `video` (object) — Структура видео
  - `wasViewed` (boolean) — Просмотрен ли отзыв
  - `isAbleSupplierFeedbackValuation` (boolean) — Доступна ли продавцу возможность оставить жалобу на отзыв:   - `true`— да   - `false` — нет
  - `supplierFeedbackValuation` (integer) — Ключ причины жалобы на отзыв
  - `isAbleSupplierProductValuation` (boolean) — Доступна ли продавцу возможность сообщить о проблеме с товаром  (`true` - доступна, `false` - не доступна)
  - `supplierProductValuation` (integer) — Ключ проблемы с товаром
  - `isAbleReturnProductOrders` (boolean) — Опция возврата товара:   - `true` — доступна   - `false` — недоступна
  - `returnProductOrdersDate` (string) — Дата и время, когда на запрос возврата был получен ответ со статус-кодом 200.
  - `bables` (array[string]) — Список тегов покупателя
  - `lastOrderShkId` (integer) — Штрихкод единицы товара
  - `lastOrderCreatedAt` (string) — Дата покупки
  - `color` (string) — Цвет товара
  - `subjectId` (integer) — ID предмета
  - `subjectName` (string) — Название предмета
  - `parentFeedbackId` (string) — ID начального отзыва (`null`, если этот отзыв начальный)
  - `childFeedbackId` (string) — ID дополненного отзыва (`null`, если этот отзыв дополненный)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 422:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

### `GET /api/v1/feedbacks/archive`

**Список архивных отзывов**

Метод возвращает список архивных [отзывов](/openapi/user-communication#tag/Otzyvy/paths/~1api~1v1~1feedbacks/get).

Отзыв становится архивным, если:
  - на отзыв получен ответ
  - на отзыв не получен ответ в течение 30 дней
  - в отзыве нет текста и фото

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Вопросы и отзывы:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек ...

**Parameters:**

- `nmId` (in query, integer) — Артикул WB
- `take` (in query, integer) **(required)** — Количество отзывов (max. 5 000)
- `skip` (in query, integer) **(required)** — Количество отзывов для пропуска
- `order` (in query, enum: dateAsc, dateDesc) — Сортировка отзывов по дате (dateAsc/dateDesc)

**Response 200:**

- `data` (object)
  - `feedbacks` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки

**Response 400:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

**Response 403:**

- `data` (object)
- `error` (boolean) — Есть ли ошибка
- `errorText` (string) — Описание ошибки
- `additionalErrors` (array[string]) — Дополнительные ошибки
- `requestId` (string)

---

## Чат с покупателями

### `GET /api/v1/seller/chats`

**Список чатов**

Метод возвращает список всех чатов продавца. По этим данным можно получить [события чатов](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1events/get) или [отправить сообщение покупателю](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1message/post).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональ...

**Response 200:**

- `result` (array[object])
  - `chatID` (string) — ID чата
  - `replySign` (string) — Подпись чата. Требуется при [отправке сообщения](./user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1message/post)
  - `clientName` (string) — Имя покупателя
  - `goodCard` (object)
  - `lastMessage` (object) — Последнее сообщение в чате
- `errors` (array[string]) — Ошибки, если есть

---

### `GET /api/v1/seller/events`

**События чатов**

Метод возвращает список событий всех [чатов с покупателями](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1chats/get).

Чтобы получить все события:
  1. Сделайте первый запрос без параметра `next`.
  2. Повторяйте запрос со значением параметра `next` из ответа на предыдущий запрос, пока `totalEvents` не станет равным `0`. Это будет означать, что вы получили все события.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавц...

**Parameters:**

- `next` (in query, integer) — Пагинатор. С какого момента получить следующий пакет данных. Формат Unix timestamp **с миллисекундами**

**Response 200:**

- `result` (object)
  - `next` (integer(Unix timestamp)) — Пагинатор. Значение поля необходимо указать в запросе для получения следующего пакета данных
  - `newestEventTime` (string(date-time)) — Время новейшего события в ответе
  - `oldestEventTime` (string(date-time)) — Время старейшего события в ответе
  - `totalEvents` (integer) — Количество событий
  - `events` (array[object])
- `errors` (array[string]) — Ошибки, если есть

**Response 400:**

- `status` (number) — HTTP статус-код
- `title` (string) — Заголовок ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `error` (string) — Текст ошибки

---

### `POST /api/v1/seller/message`

**Отправить сообщение**

Метод отправляет сообщения в [чат с покупателем](/openapi/user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1chats/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 10 сек | 10 запросов | 1 сек | 10 запросов |
| Сервисный | 10 сек | 10 запросов | 1 сек | 10 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Response 200:**

- `errors` (array[string]) — Ошибки загрузки файлов, если есть
- `result` (object)
  - `addTime` (integer(Unix Timestamp в миллисекундах)) — Дата и время создания чата
  - `chatID` (string) — ID чата
  - `sign` (string) — Подпись чата

---

### `GET /api/v1/seller/download/{id}`

**Получить файл из сообщения**

Метод возвращает файл или изображение из сообщения по его ID.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 10 сек | 10 запросов | 1 сек | 10 запросов |
| Сервисный | 10 сек | 10 запросов | 1 сек | 10 запросов |
| Базовый | 1 ч | 10 запросов | 6 мин | 1 запрос |

**Parameters:**

- `id` (in path, string) **(required)** — ID файла, см. значение поля `downloadID` в методе [События чатов](./user-communication#tag/Chat-s-pokupatelyami/paths/~1api~1v1~1seller~1events/get)

**Response 202:**

- `moderationState` (string) **(required)** — Статус модерации
- `retrySeconds` (integer) **(required)** — Секунд до следующей попытки запроса файла

**Response 400:**

- `status` (number) — HTTP статус-код
- `title` (string) — Заголовок ошибки
- `origin` (string) — ID внутреннего сервиса WB
- `detail` (string) — Детали ошибки
- `requestId` (string) — Уникальный ID запроса
- `error` (string) — Текст ошибки

---


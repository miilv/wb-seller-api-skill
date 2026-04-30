# Общее

В этом разделе:
  - [общая информация о WB API](/openapi/api-information#tag/Vvedenie)
  - как [начать работу с WB API](/openapi/api-information#tag/Vvedenie/Kak-nachat-rabotu-s-API)
  - как [авторизоваться](/openapi/api-information#tag/Avtorizaciya) и [создавать токены](/openapi/api-information#tag/Avtorizaciya/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token)
  - основные [статус-коды ответов](/openapi/api-information#tag/Vvedenie/Status-kody-HTTP)
  - [лимиты запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov)
  - как обратиться в [поддержку](/openapi/api-information#tag/Vvedenie/Podderzhka)

С помощью методов этого раздела вы можете:
  - проверить [подключение к WB API](/openapi/api-information#tag/Proverka-podklyucheniya-k-WB-API/paths/~1ping/get)
  - получить [новости портала продавцов](/openapi/api-information#tag/API-novostej/paths/~1api~1communications~1v2~1news/get)
  - получить [информацию о продавце](/openapi/api-information#tag/Informaciya-o-prodavce/paths/~1api~1v1~1seller-info/get)
  - [управлять пользователями продавца](/openapi/api-information#tag/Upravlenie-polzovatelyami-prodavca)

## API новостей

### `GET /api/communications/v2/news`

**Получение новостей портала продавцов**

Метод позволяет получать новости портала продавцов. 
 Для получения успешного ответа необходимо указать
один из параметров `from` или `fromID`. 
 За один запрос можно получить не более 100 новостей.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Сервисный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Базовый ...

**Parameters:**

- `from` (in query, string) — Дата, от которой необходимо выдать новости
- `fromID` (in query, integer) — ID новости, начиная с которой — включая её — нужно получить список новостей

**Response 200:**

- `data` (array[object]) — Новости

---

## Информация о продавце

### `GET /api/v1/seller-info`

**Получить информацию о продавце**

Информацию о продавце можно получить с [токеном](/openapi/api-information#tag/Avtorizaciya/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token) любой категории

Метод позволяет получать наименование продавца и ID его профиля.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Сервисный | 1 мин | 1 запрос | 1 мин |...

**Response 200:**

- `name` (string) — Наименование продавца
- `sid` (string(UUID)) — Уникальный ID продавца на Wildberries, [находящийся в публичном поле токена](./api-information#tag/Avtorizaciya/Kak-ustroen-token)
- `tin` (string) — ИНН
- `tradeMark` (string) — Торговое наименование продавца

---

### `GET /api/common/v1/rating`

**Получить рейтинг продавца**

Operation ID: `getCommonV1Rating`

Для доступа к методу используйте [токен](/openapi/api-information#tag/Avtorizaciya/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token) для категории Вопросы и отзывы

Метод доступен по Сервисному [токену](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API)

Метод возвращает пользовательский рейтинг продавца и количество отзывов.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Вспле...

**Response 200:**

- `feedbackCount` (integer) — Количество отзывов
- `valuation` (number(float)) — Рейтинг продавца

---

### `GET /api/common/v1/subscriptions`

**Получить информацию о подписке Джем**

Operation ID: `getCommonV1Subscriptions`

Информацию о подписке Джем можно получить с [токеном](/openapi/api-information#tag/Avtorizaciya/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token) любой категории

Метод доступен по Сервисному [токену](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API)

Метод возвращает информацию о подписке [Джем](https://seller.wildberries.ru/monetization/jam):
  - Если продавец никогда не подключал подписку Джем, возвращается пустой ответ `200`.
  - Если продавец активирова...

**Response 200:**

- `state` (enum) **(required)** — Values: `active, inactive`. Статус подписки:   - `active` — активна   - `inactive` — истекла или отменена
- `activationSource` (enum) **(required)** — Values: `constructor, jam`. Источник подключения подписки:   - `constructor` — покупка через раздел **Конструктор тарифов**   - `jam` — покупка через раздел **Подписка «Джем»**
- `level` (enum) **(required)** — Values: `standard, advanced, premium`. Уровень подписки:   - `standard`   - `advanced`   - `premium`
- `since` (string(date-time)) **(required)** — Дата и время первой активации подписки. Не меняется при продлении или повторной активации
- `till` (string(date-time)) **(required)** — Дата и время окончания подписки

---

## Проверка подключения к WB API

### `GET /ping`

**Проверка подключения**

Метод проверяет:
  1. Успешно ли запрос доходит до WB API
  2. Валидность токена авторизации и URL запроса
  3. Совпадают ли категория токена и сервис

  Метод не предназначен для проверки доступности сервисов WB

У каждого сервиса есть свой вариант метода в зависимости от домена:

| Категория | URL запроса |
|---------------|-----------------------|
| Контент | `https://content-api.wildberries.ru/ping`
`https://content-api-sandbox.wildberries.ru/ping` |
| Аналитика | `https://seller-analytics-a...

**Response 200:**

- `TS` (string) — Timestamp запроса
- `Status` (enum) — Values: `OK`. Статус

---

## Управление пользователями продавца

### `POST /api/v1/invite`

**Создать приглашение для нового пользователя**

Метод доступен по Персональному [токену](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API)

Метод создаёт приглашение для нового пользователя с настройкой доступов к разделам профиля продавца.

Как выдаются права доступа:
- Если `access` пустой (`[]`) или не указан — по умолчанию выдаются все доступы, кроме доступов к витрине (`showcase`) и **Джем** (`changeJam`)
- Если в `access` указана часть разделов профиля, то кроме тех доступов, что указаны в запросе, т...

**Request body:**

- `access` (object)
- `invite` (object) **(required)**
  - `phoneNumber` (string) **(required)** — Номер телефона пользователя для приглашения. Поддерживаются номера телефонов из стран:• Азербайджан • Армения • Барбадос • Беларусь • Бразилия • Гонко
  - `position` (string) — Должность пользователя

**Response 200:**

- `inviteID` (string(uuid)) **(required)** — ID приглашения
- `expiredAt` (string(date-time)) **(required)** — Дата и время окончания срока действия приглашения
- `isSuccess` (boolean) **(required)** — - `true` — приглашение создано успешно - `false` — повторите запрос
- `inviteUrl` (string(uri)) **(required)** — URL приглашения, по которому должен перейти пользователь

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — ID запроса
- `origin` (string) **(required)** — Название внутреннего сервиса
- `status` (number) **(required)** — HTTP статус-код

---

### `GET /api/v1/users`

**Получить список активных или приглашённых пользователей продавца**

Метод доступен по Персональному [токену](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API)

Метод возвращает список активных или приглашённых пользователей профиля продавца.

Чтобы выбрать список, укажите значение параметра `isInviteOnly`:
  - `isInviteOnly=true` — список приглашённых пользователей, которые ещё не активировали доступ
  - `isInviteOnly=false` или не указан — список активных пользователей

По каждому пользователю можно получить:
  - роль пользо...

**Parameters:**

- `limit` (in query, integer) — Количество активных или приглашённых пользователей в ответе
- `offset` (in query, integer) — Сколько элементов пропустить. Например, для значения 10 ответ начнется с 11 элемента
- `isInviteOnly` (in query, boolean) — - `true` — список приглашённых пользователей, которые ещё не активировали доступ - `false` или не указан — список активных пользователей профиля прода

**Response 200:**

- `total` (integer) **(required)** — Общее количество активных или приглашённых пользователей
- `countInResponse` (integer) **(required)** — Количество активных или приглашённых пользователей на текущей странице
- `users` (array[object]) **(required)** — Информация о пользователях

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — ID запроса
- `origin` (string) **(required)** — Название внутреннего сервиса
- `status` (number) **(required)** — HTTP статус-код

---

### `PUT /api/v1/users/access`

**Изменить права доступа пользователей**

Метод доступен по Персональному [токену](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API)

Метод меняет права доступа одному или нескольким пользователям.

Обновляются только права доступа, переданные в параметрах запроса. Остальные поля остаются без изменений.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 сек | 1 запрос | 1 сек | 5 зап...

**Request body:**

- `usersAccesses` (array[object]) **(required)** — Настройки доступа для пользователя
  - `userId` (integer) — ID пользователя
  - `access` (object)

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — ID запроса
- `origin` (string) **(required)** — Название внутреннего сервиса
- `status` (number) **(required)** — HTTP статус-код

---

### `DELETE /api/v1/user`

**Удалить пользователя**

Метод доступен по Персональному [токену](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API)

Метод удаляет пользователя из [списка сотрудников продавца](/openapi/api-information#tag/Upravlenie-polzovatelyami-prodavca/paths/~1api~1v1~1users/get). Этому пользователю будет закрыт доступ в профиль продавца.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- |...

**Parameters:**

- `deletedUserID` (in query, integer) **(required)** — ID пользователя, которому будет закрыт доступ

**Response 400:**

- `title` (string) **(required)** — Заголовок ошибки
- `detail` (string) **(required)** — Детали ошибки
- `requestId` (string) **(required)** — ID запроса
- `origin` (string) **(required)** — Название внутреннего сервиса
- `status` (number) **(required)** — HTTP статус-код

---


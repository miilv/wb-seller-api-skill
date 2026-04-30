# Работа с товарами

С помощью методов этого раздела вы можете:
  - [создавать](/openapi/work-with-products#tag/Sozdanie-kartochek-tovarov) и [редактировать](/openapi/work-with-products#tag/Kartochki-tovarov) карточки товаров
  - получать [категории, предметы, характеристики и бренды товаров](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki)
  - загружать [медиафайлы](/openapi/work-with-products#tag/Mediafajly) в карточки товаров
  - настраивать [ярлыки](/openapi/work-with-products#tag/Yarlyki) для поиска товаров
  - устанавливать [цены и скидки](/openapi/work-with-products#tag/Ceny-i-skidki)
  - управлять [остатками товаров](/openapi/work-with-products#tag/Ostatki-na-skladah-prodavca) и [складами](/openapi/work-with-products#tag/Sklady-prodavca), если вы работаете по модели продаж со склада продавца

  
    Узнать, как использовать методы в бизнес-кейсах, можно в [инструкции](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami) по работе с товарами

## Карточки товаров

### `POST /content/v2/get/cards/list`

**Список карточек товаров**

Метод доступен по [токену](/openapi/api-information#tag/Avtorizaciya/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token) с категорией Контент или Продвижение

Метод возвращает список созданных карточек товаров.

  В ответе метода не будет карточек, находящихся в корзине. Получить такие карточки можно через [отдельный метод](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1v2~1get~1cards~1trash/post)

Чтобы получить **больше 100** карточек товаров, используйте пагинацию:
  1. Сде...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Request body:**

- `settings` (object) — Настройки
  - `sort` (object) — Параметр сортировки
    - `ascending` (boolean) — Сортировать по полю `updatedAt`:   - `false` — по убыванию   -  `true` — по возрастанию
  - `filter` (object) — Параметры фильтрации
    - `withPhoto` (integer) — Фильтр по фото:   * `0` — только карточки без фото   * `1` — только карточки с фото   * `-1` — все карточки товара
    - `textSearch` (string) — Поиск по артикулу продавца, артикулу WB, баркоду
    - `tagIDs` (array[integer]) — Поиск по ID ярлыков
    - `allowedCategoriesOnly` (boolean) — Фильтр по категории:   - `true` — только разрешённые   - `false` — все    Не используется в песочнице
    - `objectIDs` (array[integer]) — Поиск по id предметов
    - `brands` (array[string]) — Поиск по брендам
    - `imtID` (integer) — Поиск по [ID для объединённых карточек товаров](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovar
  - `cursor` (object) — Курсор
    - `limit` (integer) — Сколько карточек товаров выдать в ответе
    - `updatedAt` (string) — Дата и время изменения
    - `nmID` (integer) — Артикул WB, с которого надо запрашивать следующий список карточек товаров

**Response 200:**

- `cards` (array[object]) — Список карточек товаров
- `cursor` (object) — Пагинатор
  - `updatedAt` (string) — Дата и время, с которых надо запрашивать следующий список карточек товаров
  - `nmID` (integer) — Артикул WB, с которого надо запрашивать следующий список карточек товаров
  - `total` (integer) — Количество возвращённых карточек товаров

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/cards/error/list`

**Список несозданных карточек товаров с ошибками**

Метод возвращает список карточек товаров ([черновиков](https://seller.wildberries.ru/new-goods/error-cards)), при создании или редактировании которых произошли ошибки, с описанием этих ошибок.

Данные в ответе возвращаются пакетами `batch`. Один пакет содержит:
  - все ошибки по одному массиву `variants` одного запроса при [создании](/openapi/work-with-products#tag/Sozdanie-kartochek-tovarov/paths/~1content~1v2~1cards~1upload/post) карточек товаров
  - все ошибки одного запроса при [создании с п...

**Parameters:**

- `locale` (in query, string) — Язык названий предметов:   - `ru` — русский   - `en` — английский   - `zh` — китайский

**Request body:**

- `cursor` (object)
  - `limit` (number(int)) — Количество пакетов в ответе
  - `updatedAt` (string(date-time)) — Дата и время формирования последнего пакета в ответе на предыдущий запрос
  - `batchUUID` (string(UUID)) — ID последнего пакета в ответе на предыдущий запрос
- `order` (object)
  - `ascending` (boolean) — - `false` — сортировка по убыванию - `true` — сортировка по возрастанию

**Response 200:**

- `data` (object) **(required)**
  - `items` (array[object]) **(required)** — Пакеты данных
  - `cursor` (object) **(required)**
- `error` (boolean) **(required)** — Флаг ошибки
- `errorText` (string) **(required)** — Описание ошибки
- `additionalErrors` (object) **(required)** — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/cards/update`

**Редактирование карточек товаров**

Метод обновляет данные карточек товаров. Также используйте его, чтобы добавлять новые размеры.

  Карточка товара перезаписывается при обновлении. Поэтому в запросе нужно передать в том числе те параметры карточки, которые вы не собираетесь обновлять. Их значения можно получить в [списке карточек товаров](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1v2~1get~1cards~1list/post) и [списке карточек товаров в корзине](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1con...

**Request body:**

**Response 200:**

- `data` (object) — Данные ответа
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 413:**

- `title` (string) — Заголовок ошибки
- `detail` (string) — Детали ошибки
- `code` (string) — Внутренний код ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB
- `status` (number) — HTTP статус-код
- `statusText` (string) — Расшифровка HTTP статус-кода

---

### `POST /content/v2/cards/moveNm`

**Объединение и разъединение карточек товаров**

Метод [объединяет и разъединяет](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#obuedinenie-i-razuedinenie-kartochek-tovarov) карточки товаров. Карточки товаров являются объединёнными, если у них одинаковый `imtID`.

Для объединения карточек товаров сделайте запрос **с указанием** `imtID`. Можно объединять не более 30 карточек товаров.

Для разъединения карточек товаров сделайте запрос **без указания** `imtID`. Для разъединенных карточек...

**Request body:**

**Response 200:**

- `data` (object) — Данные ответа
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

**Response 403:**

- `data` (object) — Данные ответа
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 413:**

---

### `POST /content/v2/cards/delete/trash`

**Перенос карточек товаров в корзину**

Метод переносит [карточки товаров в корзину](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1v2~1get~1cards~1trash/post). При этом карточки товаров не удаляются, их можно [восстановить](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1v2~1cards~1recover/post).

  После переноса в корзину карточке товара присваивается новый imtID — ID для [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#ob...

**Request body:**

- `nmIDs` (array[integer]) — Артикулы WB

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/cards/recover`

**Восстановление карточек товаров из корзины**

Метод восстанавливает [карточки товаров из корзины](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1v2~1get~1cards~1trash/post).

  Карточка товара сохраняет тот же imtID — ID для [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#obuedinenie-i-razuedinenie-kartochek-tovarov) карточек товаров — что был присвоен ей при [перемещении в корзину](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1...

**Request body:**

- `nmIDs` (array[integer]) — Артикулы WB

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/get/cards/trash`

**Список карточек товаров в корзине**

Метод доступен по [токену](/openapi/api-information#tag/Avtorizaciya/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token) с категорией Контент или Продвижение

Метод возвращает список карточек товаров в корзине.

Чтобы получить **больше 100** карточек товаров, используйте пагинацию.
  1. Сделайте первый запрос: 

      
        {
          "settings": {
            "sort": {
              "ascending": true
            },
            "cursor": {
              "limit": 100
            }
          }
...

**Parameters:**

- `locale` (in query, enum: ru, en, zh) — Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Request body:**

- `settings` (object) — Настройки
  - `sort` (object) — Параметр сортировки
    - `ascending` (boolean) — Сортировать по `trashedAt`:   - `false` — по убыванию   - `true` — по возрастанию
  - `cursor` (object) — Пагинатор
    - `limit` (integer) — Сколько карточек товаров выдать в ответе
    - `trashedAt` (string) — Дата и время помещения в корзину
    - `nmID` (integer) — Артикул WB, с которого надо запрашивать следующий список карточек товаров
  - `filter` (object) — Параметры фильтрации
    - `textSearch` (string) — Поиск по артикулу продавца, артикулу WB, баркоду

**Response 200:**

- `cards` (array[object]) — Массив карточек товаров
- `cursor` (object) — Пагинатор
  - `trashedAt` (string) — Дата и время, с которых надо запрашивать следующий список карточек товаров
  - `nmID` (integer) — Артикул WB, с которого надо запрашивать следующий список карточек товаров
  - `total` (integer) — Количество возвращённых карточек товаров

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

## Категории, предметы и характеристики

### `GET /content/v2/object/parent/all`

**Родительские категории товаров**

Метод возвращает названия и ID всех родительских категорий для [создания карточек товаров](/openapi/work-with-products#tag/Sozdanie-kartochek-tovarov): например, `Электроника`, `Бытовая химия`, `Рукоделие`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек...

**Parameters:**

- `locale` (in query, string) — Язык поля ответа `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг наличия ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/object/all`

**Список предметов**

Метод возвращает список названий [родительских категорий предметов](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1parent~1all/get) и их предметов с ID. Например, у категории `Игрушки` будут предметы `Калейдоскопы`, `Куклы`, `Мячики`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 ...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице
- `name` (in query, string) — Поиск по названию предмета (Носки), поиск работает по подстроке, искать можно на любом из поддерживаемых языков
- `limit` (in query, integer) — Количество предметов, максимум 1000
- `offset` (in query, integer) — Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента
- `parentID` (in query, integer) — ID родительской категории предмета

**Response 200:**

- `data` (array[object]) — Предметы
- `error` (boolean) — Флаг наличия ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/object/charcs/{subjectId}`

**Характеристики предмета**

Метод возвращает параметры характеристик предмета: названия, типы данных, единицы измерения и так далее. В запросе необходимо указать ID [предмета](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1all/get).

  Для получения значений характеристик [Цвет](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1directory~1colors/get), [Пол](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1con...

**Parameters:**

- `subjectId` (in path, integer) **(required)** — ID предмета
- `locale` (in query, string) — Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (array[object]) — Данные
- `error` (boolean) — Флаг наличия ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/directory/colors`

**Цвет**

Метод возвращает возможные значения [характеристики](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get) предмета `Цвет`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек товаров](/...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/directory/kinds`

**Пол**

Метод возвращает возможные значения [характеристики](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get) предмета `Пол`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек товаров](/o...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (array[string]) — Массив значений для хар-ки Пол
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/directory/countries`

**Страна производства**

Метод возвращает возможные значения [характеристики](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get) предмета `Страна производства`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карт...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/directory/seasons`

**Сезон**

Метод возвращает возможные значения [характеристики](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get) предмета `Сезон`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек товаров](...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (array[string]) — Массив значений для хар-ки Сезон
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/directory/vat`

**Ставка НДС**

Метод возвращает возможные значения [характеристики](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get) предмета `Ставка НДС`.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек това...

**Parameters:**

- `locale` (in query, string) — Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (array[string])
- `error` (boolean) — Флаг наличия ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /content/v2/directory/tnved`

**ТНВЭД-код**

Метод возвращает список ТНВЭД-кодов по ID [предмета](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1all/get) и фрагменту ТНВЭД-кода.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек товаров](/openapi/work-...

**Parameters:**

- `subjectID` (in query, integer) **(required)** — ID предмета
- `search` (in query, integer) — Поиск по ТНВЭД-коду. Работает только в паре с `subjectID`
- `locale` (in query, string) — Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не используется в песочнице

**Response 200:**

- `data` (array[object]) — Данные
- `error` (boolean) — Флаг наличия ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `GET /api/content/v1/brands`

**Бренды**

Метод возвращает список брендов по ID предмета.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 сек | 1 запрос | 1 сек | 5 запросов |
| Сервисный | 1 сек | 1 запрос | 1 сек | 5 запросов |
| Базовый | 1 ч | 1 запрос | 1 ч | 1 запрос |

**Parameters:**

- `subjectId` (in query, integer) **(required)** — ID предмета
- `next` (in query, integer) — Параметр пагинации. Используйте значение `next` из ответа, чтобы получить следующий пакет данных

**Response 200:**

- `brands` (array[object]) **(required)**
- `next` (integer) — Параметр пагинации. Укажите это значение в запросе, чтобы получить следующий пакет данных. Если поле отсутствует, вы получили все данные
- `total` (integer) **(required)** — Общее количество брендов предмета

---

## Медиафайлы

### `POST /content/v3/media/file`

**Загрузить медиафайл**

Метод загружает и добавляет один медиафайл к карточке товара.

Требования к изображениям:
  * максимум изображений для одной карточки товара — 30
  * минимальное разрешение — 700x900 px
  * максимальный размер — 32 Мб
  * минимальное качество — 65%
  * форматы — JPG, PNG, BMP, GIF (статичные), WebP

Требования к видео:
  * максимум одно видео для одной карточки товара
  * максимальный размер — 50 Мб
  * форматы — MOV, MP4

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) н...

**Parameters:**

- `X-Nm-Id` (in header, string) **(required)** — Артикул WB
- `X-Photo-Number` (in header, integer) **(required)** — Номер медиафайла на загрузку, начинается с `1`. При загрузке видео всегда указывайте `1`.  Чтобы добавить изображение к уже загруженным, номер медиафа

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

- `additionalErrors` (object) — Дополнительные ошибки
- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `additionalErrors` (object) — Дополнительные ошибки
- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `POST /content/v3/media/save`

**Загрузить медиафайлы по ссылкам**

Метод загружает набор медиафайлов в карточку товара через указание ссылок в запросе.

  Новые медиафайлы полностью заменяют старые. Чтобы добавить новые медиафайлы, укажите в запросе ссылки одновременно на новые и старые медиафайлы.

Требования к ссылкам:
  * ссылка должна вести прямо на файл. Убедитесь, что ссылка не ведёт на страницу предпросмотра или авторизации, например. Если по ссылке открывается текстовая страница TXT или HTML, ссылка считается некорректной
  * для доступа к файлу по ссыл...

**Request body:**

- `nmId` (integer) — Артикул WB
- `data` (array[string]) — Ссылки на изображения в том порядке, в котором они будут в карточке товара, и на видео, на любой позиции массива

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

- `additionalErrors` (object) — Дополнительные ошибки
- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `additionalErrors` (object) — Дополнительные ошибки
- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 409:**

- `additionalErrors` (object) — Дополнительные ошибки
- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 422:**

- `additionalErrors` (object) — Дополнительные ошибки
- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

## Остатки на складах продавца

### `PUT /api/v3/stocks/{warehouseId}`

**Обновить остатки товаров**

Метод обновляет количество остатков товаров продавца [в списке](/openapi/work-with-products#tag/Ostatki-na-skladah-prodavca/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/post).

  Названия параметров запроса не валидируются. При отправке некорректных названий вы получите успешный ответ (204), но остатки не обновятся.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов остатков на складах продавца:

| Период | Лимит | Интервал | Всплеск ...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `stocks` (array[object]) **(required)** — Массив ID размеров товаров и их остатков

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

---

### `DELETE /api/v3/stocks/{warehouseId}`

**Удалить остатки товаров**

Метод удаляет запись об остатках товаров продавца из [списка остатков](/openapi/work-with-products#tag/Ostatki-na-skladah-prodavca/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/post).

  Действие необратимо. Удаленный остаток будет необходимо загрузить повторно для возобновления продаж.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов остатков на складах продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `chrtIds` (array[integer]) **(required)** — Массив ID размеров товаров

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 404:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `POST /api/v3/stocks/{warehouseId}`

**Получить остатки товаров**

Метод возвращает данные об остатках товаров на [складах продавца](/openapi/work-with-products#tag/Sklady-prodavca).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов остатков на складах продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )

**Request body:**

- `chrtIds` (array[integer]) **(required)** — Массив ID размеров товаров

**Response 200:**

- `stocks` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

## Склады продавца

### `GET /api/v3/offices`

**Получить список складов WB**

Метод возвращает список всех складов WB для привязки к складам продавца. Предназначен для определения складов WB, чтобы сдавать готовые заказы по модели [FBS](/openapi/orders-fbs#tag/Zakazy-FBS) (Fulfillment by Seller).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов складов продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 ...

**Response 200:**

_(array of objects:)_
- `address` (string) — Адрес
- `name` (string) — Название
- `city` (string) — Город
- `id` (integer(int64)) — ID
- `longitude` (number(float64)) — Долгота
- `latitude` (number(float64)) — Широта
- `cargoType` (enum) — Values: `1, 2, 3`. Тип товара, который принимает склад:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+
- `deliveryType` (enum) — Values: `1, 2, 3, 5, 6`. Тип доставки, который принимает склад:   - `1` — доставка на склад WB (FBS)   - `2` — доставка силами продавца (DBS)   - `3` — доставка курьером WB (D
- `federalDistrict` (string) — Федеральный округ склада WB. Если `null`, склад находится за пределами РФ или федеральный округ не указан
- `selected` (boolean) — Признак того, что склад уже выбран продавцом

---

### `GET /api/v3/warehouses`

**Получить список складов продавца**

Метод возвращает список всех складов продавца. Может использоваться для получения [остатков товаров](/openapi/work-with-products#tag/Ostatki-na-skladah-prodavca/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/post).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов складов продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывает...

**Response 200:**

_(array of objects:)_
- `name` (string) — Название склада продавца
- `officeId` (integer(int64)) — ID склада WB
- `id` (integer(int64)) — ID склада продавца
- `cargoType` (enum) — Values: `1, 2, 3`. Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   - `3` — крупногабаритный товар (КГТ+)
- `deliveryType` (enum) — Values: `1, 2, 3, 5, 6`. Тип доставки, который принимает склад:   - `1` — доставка на склад WB (FBS)   - `2` — доставка силами продавца (DBS)   - `3` — доставка курьером WB (D
- `isDeleting` (boolean) — Склад удаляется:   - `false` — нет   - `true` — да  После удаления склад пропадёт из списка
- `isProcessing` (boolean) — Данные склада обновляются:   - `false` — нет   - `true` — да, обновление и удаление остатков недоступно  Обновление данных может занимать несколько ми

---

### `POST /api/v3/warehouses`

**Создать склад продавца**

Метод создаёт склад продавца для работы с [остатками товаров](/openapi/work-with-products#tag/Ostatki-na-skladah-prodavca/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/post). Нужно привязать к складу продавца [склад WB](/openapi/work-with-products#tag/Sklady-prodavca/paths/~1api~1v3~1offices/get) для работы по модели [FBS](/openapi/orders-fbs#tag/Zakazy-FBS) (Fulfillment by Seller).

  Нельзя привязывать склад WB, который уже используется

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limi...

**Request body:**

- `name` (string) **(required)** — Имя склада продавца
- `officeId` (integer) **(required)** — ID склада WB

**Response 201:**

- `id` (integer) — ID склада продавца

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/warehouses/{warehouseId}`

**Обновить склад продавца**

Метод обновляет данные склада продавца в [списке складов](/openapi/work-with-products#tag/Sklady-prodavca/paths/~1api~1v3~1warehouses/get). Данные о привязанном [складе WB](/openapi/work-with-products#tag/Sklady-prodavca/paths/~1api~1v3~1offices/get) можно изменить один раз в сутки.

  Нельзя привязывать склад WB, который уже используется

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов складов продавца:

| Период | Лимит | Интерв...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `name` (string) **(required)** — Имя склада продавца
- `officeId` (integer) **(required)** — ID склада WB

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

**Response 409:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `DELETE /api/v3/warehouses/{warehouseId}`

**Удалить склад продавца**

Метод удаляет склад продавца из [списка складов](/openapi/work-with-products#tag/Sklady-prodavca/paths/~1api~1v3~1warehouses/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов складов продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |

Один запрос с кодом ответа 409 учитывается как 10 запросов

**Parameters:**

- `?` (in ?, )

---

### `GET /api/v3/dbw/warehouses/{warehouseId}/contacts`

**Список контактов**

Метод возвращает список контактов, привязанных к [складу продавца](/openapi/work-with-products#tag/Sklady-prodavca/paths/~1api~1v3~1warehouses/get).

Только для складов с типом доставки `3` — доставка курьером WB (DBW).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для следующих методов DBW:

    получение и обновление списка контактов
    получение и удаление метаданных
    методы сборочных заданий
 

| Период | Лимит | Интервал | Всплеск |
| ...

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `contacts` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

### `PUT /api/v3/dbw/warehouses/{warehouseId}/contacts`

**Обновить список контактов**

Метод обновляет список контактов [склада продавца](/openapi/work-with-products#tag/Sklady-prodavca/paths/~1api~1v3~1warehouses/get).

  Список контактов перезаписывается при обновлении. Поэтому в запросе нужно передать все параметры списка контактов, в том числе те, которые вы не собираетесь обновлять.

Только для складов с типом доставки `3` — курьером WB (DBW).

К складу можно добавить максимум 5 контактов. Чтобы удалить контакты, отправьте пустой массив `contacts`.

[Лимит запросов](/openapi/...

**Parameters:**

- `?` (in ?, )

**Request body:**

- `contacts` (array[object])

**Response 400:**

- `code` (string) — Код ошибки
- `message` (string) — Описание ошибки
- `data` (object) — Дополнительные данные ошибки

---

## Создание карточек товаров

### `GET /content/v2/cards/limits`

**Лимиты карточек товаров**

Возвращает бесплатные и платные лимиты продавца на [создание карточек товаров](/openapi/work-with-products#tag/Sozdanie-kartochek-tovarov/paths/~1content~1v2~1cards~1upload/post).

Формула для получения количества карточек, которые можно создать:

> (`freeLimits` + `paidLimits`) - количество созданных карточек

Созданными считаются карточки, которые можно получить через методы [список карточек товаров](/openapi/work-with-products#tag/Kartochki-tovarov/paths/~1content~1v2~1get~1cards~1list/post) ...

**Response 200:**

- `data` (object)
  - `freeLimits` (integer) — Количество бесплатных лимитов
  - `paidLimits` (integer) — Количество оплаченных лимитов
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/barcodes`

**Генерация баркодов**

Метод генерирует массив уникальных баркодов для создания размера в [карточке товара](/openapi/work-with-products#tag/Sozdanie-kartochek-tovarov/paths/~1content~1v2~1cards~1upload/post). Можно использовать, если у вас нет собственных баркодов.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключен...

**Request body:**

- `count` (integer) — Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов для генерации - `5 000`

**Response 200:**

- `data` (array[string]) — Массив сгенерированных баркодов
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/cards/upload`

**Создание карточек товаров**

Метод создаёт карточки товаров c указанием описаний и характеристик товаров.

  Есть две формы запроса: для создания отдельных и объединённых карточек товаров

Габариты товаров можно указать только в `сантиметрах`, вес товара с упаковкой — в `килограммах`.

Создание карточки товара происходит асинхронно. Синхронизация новой карточки с сервисами может занимать до 30 минут. В течение этого времени невозможно добавить остатки на склады и настроить цены. 

Одним запросом можно создать максимум 100 о...

**Request body:**

**Response 200:**

- `data` (object) — Данные ответа
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 413:**

- `title` (string) — Заголовок ошибки
- `detail` (string) — Детали ошибки
- `code` (string) — Внутренний код ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB
- `status` (number) — HTTP статус-код
- `statusText` (string) — Расшифровка HTTP статус-кода

---

### `POST /content/v2/cards/upload/add`

**Создание карточек товаров с присоединением**

Метод создаёт карточки товаров, присоединяя их к существующим отдельным карточкам и группам [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/rabota-s-tovarami#obuedinenie-i-razuedinenie-kartochek-tovarov) карточек. В одной группе объединённых карточек товаров может быть не более 30 карточек, соответственно, создать с присоединением можно не более 29 карточек товаров за один запрос.

Габариты товаров можно указать только в `сантиметрах`, вес т...

**Request body:**

- `imtID` (integer) — `imtID` отдельной карточки товара или группы [объединённых](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-1320-71bb-9dac-8ba07e7177ce/ra
- `cardsToAdd` (array[object]) — Добавляемые карточки товаров

**Response 200:**

- `data` (object) — Данные ответа
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 413:**

- `title` (string) — Заголовок ошибки
- `detail` (string) — Детали ошибки
- `code` (string) — Внутренний код ошибки
- `requestId` (string) — Уникальный ID запроса
- `origin` (string) — ID внутреннего сервиса WB
- `status` (number) — HTTP статус-код
- `statusText` (string) — Расшифровка HTTP статус-кода

---

## Цены и скидки

### `POST /api/v2/upload/task`

**Установить цены и скидки**

Метод устанавливает цены и скидки для товаров.

Чтобы установить цены для размеров товара, используйте [отдельный метод](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1size/post).

  Получить информацию о процессе установки цен и скидок можно с помощью методов [состояния](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1history~1tasks/get) и [детализации](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1history~1goods~1task/get) обработан...

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 409:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 422:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `POST /api/v2/upload/task/size`

**Установить цены для размеров**

Метод устанавливает цены отдельно для размеров товаров.

Работает только для товаров из категорий, где можно устанавливать цены отдельно для разных размеров. Для [таких товаров](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1list~1goods~1size~1nm/get) `"editableSizePrice":true`.

Чтобы установить цены и скидки для самих товаров, используйте [отдельный метод](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task/post).

  Получить информацию о процессе устано...

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 409:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 422:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `POST /api/v2/upload/task/club-discount`

**Установить скидки WB Клуба**

Устанавливает скидки для товаров в рамках подписки [WB Клуб](https://seller.wildberries.ru/help-center/article/A-337).

  Получить информацию о процессе установки цен и скидок можно с помощью методов [состояния](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1history~1tasks/get) и [детализации](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1history~1goods~1task/get) обработанной загрузки.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на о...

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 409:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 422:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `GET /api/v2/history/tasks`

**Состояние обработанной загрузки**

Метод возвращает информацию об обработанной загрузке цен и скидок.

  Обработанная загрузка — это загрузка цен и скидок для [товаров](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task/post), цен для [размеров товаров](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1size/post) и скидок [WB Клуба](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1club-discount/post).

[Лимит запросов](/openapi/api-information#tag/Vve...

**Parameters:**

- `?` (in ?, )

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `GET /api/v2/history/goods/task`

**Детализация обработанной загрузки**

Метод возвращает информацию о товарах и об ошибках в товарах в обработанной загрузке.

  Обработанная загрузка — это загрузка цен и скидок для [товаров](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task/post), цен для [размеров товаров](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1size/post) и скидок [WB Клуба](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1club-discount/post).

[Лимит запросов](/openapi/api-...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `GET /api/v2/buffer/tasks`

**Состояние необработанной загрузки**

Метод возвращает информацию про загрузку скидок в обработке.

  Необработанная загрузка — это загрузка скидок в [календаре акций](/openapi/promotion#tag/Kalendar-akcij). Такие скидки применятся к товарам только в момент старта акции.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Цены и скидки:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 6 сек | 10 запросов | 600 мс |...

**Parameters:**

- `?` (in ?, )

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `GET /api/v2/buffer/goods/task`

**Детализация необработанной загрузки**

Метод возвращает информацию о товарах и ошибках в товарах из загрузки в обработке.

  Необработанная загрузка — это загрузка скидок в [календаре акций](/openapi/promotion#tag/Kalendar-akcij). Такие скидки применятся к товарам только в момент старта акции.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Цены и скидки:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 6 сек | ...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `GET /api/v2/list/goods/filter`

**Получить товары с ценами**

Метод возвращает информацию о товарах: цены, валюту, общие скидки и скидки [WB Клуба](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1club-discount/post).

В одном запросе можно указать только один артикул.

Чтобы получить информацию обо всех товарах продавца, не указывая артикулы, установите `limit=1000`, в параметре `offset` установите смещение по количеству записей. Количество нужно рассчитать по формуле: `offset` плюс `limit` из предыдущего запроса. Повторяйте за...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `POST /api/v2/list/goods/filter`

**Получить товары с ценами по артикулам**

Метод возвращает информацию о товарах по их артикулам: цены, валюту, общие скидки и скидки [WB Клуба](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1club-discount/post).

В одном запросе можно указать более одного артикула.

Используйте отдельные методы, чтобы получить информацию:
  - обо [всех товарах продавца, не указывая артикулы](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1list~1goods~1filter/get)
  - о [размерах товара](/openapi/work-with-pro...

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `GET /api/v2/list/goods/size/nm`

**Получить размеры товара с ценами**

Метод возвращает информацию обо всех размерах одного товара: цены, валюту, общие скидки и скидки для [WB Клуба](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1upload~1task~1club-discount/post).

Работает только для товаров из категорий, где можно устанавливать цены отдельно для разных размеров. Для таких товаров `"editableSizePrice":true`.

Чтобы получить информацию о самом товаре, используйте [отдельный метод](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1list~1...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )
- `?` (in ?, )

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

### `GET /api/v2/quarantine/goods`

**Получить товары в карантине**

Метод возвращает информацию о товарах в карантине.

Если новая цена товара со скидкой будет минимум в 3 раза меньше старой, товар попадёт в [карантин](https://seller.wildberries.ru/instructions/ru/ru/material/price-quarantine) и будет продаваться по старой цене. Ошибка об этом будет в ответах методов [состояний загрузок](/openapi/work-with-products#tag/Ceny-i-skidki/paths/~1api~1v2~1history~1tasks/get).

Вы можете изменить цену или скидку с помощью API либо вывести товар из карантина в [личном к...

**Parameters:**

- `?` (in ?, )
- `?` (in ?, )

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

**Response 422:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки

---

## Ярлыки

### `GET /content/v2/tags`

**Список ярлыков**

Метод возвращает список и характеристики всех ярлыков продавца для группировки и фильтрации товаров.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек товаров](/openapi/work-with-products#tag/Sozdanie-kartochek-tovarov/paths/~1content~1v2~1cards~1upload/po...

**Response 200:**

- `data` (object)
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Описание ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/tag`

**Создание ярлыка**

Метод добавляет один ярлык продавца. Можно создать максимум 15 ярлыков для одного продавца. Максимальная длина ярлыка — 15 символов.

Созданный ярлык можно получить в общем [списке](/openapi/work-with-products#tag/Yarlyki/paths/~1content~1v2~1tags/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов ...

**Request body:**

- `color` (string) — Цвет ярлыка.  Доступные цвета:   - `D1CFD7` — серый   - `FEE0E0` — красный   - `ECDAFF` — фиолетовый   - `E4EAFF` — синий   - `DEF1DD` — зеленый   - `
- `name` (string) — Имя ярлыка

**Response 200:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `PATCH /content/v2/tag/{id}`

**Изменение ярлыка**

Метод заменяет данные ярлыка: имя и цвет.

Новые данные можно получить в общем [списке](/openapi/work-with-products#tag/Yarlyki/paths/~1content~1v2~1tags/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек товаров](/openapi/work-with-products#tag/Sozda...

**Parameters:**

- `id` (in path, integer) **(required)** — Числовой ID ярлыка

**Request body:**

- `color` (string) — Цвет ярлыка
- `name` (string) — Имя ярлыка

**Response 200:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `DELETE /content/v2/tag/{id}`

**Удаление ярлыка**

Метод удаляет ярлык из [списка ярлыков](/openapi/work-with-products#tag/Yarlyki/paths/~1content~1v2~1tags/get) продавца.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запросов |

Исключение — методы:

    [создания карточек товаров](/openapi/work-with-products#tag/Sozdanie-kartochek-tovarov/paths/~1content~1...

**Parameters:**

- `id` (in path, integer) **(required)** — Числовой ID ярлыка

**Response 200:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (object) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---

### `POST /content/v2/tag/nomenclature/link`

**Управление ярлыками в карточке товара**

Метод добавляет или снимает ярлык с карточки товара. К карточке можно добавить максимум 15 ярлыков.

При удалении ярлыка из карточки товара он не удаляется из [списка ярлыков](/openapi/work-with-products#tag/Yarlyki/paths/~1content~1v2~1tags/get) продавца.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца для всех методов категории Контент:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 100 запросов | 600 мс | 5 запрос...

**Request body:**

- `nmID` (integer) — Артикул WB
- `tagsIDs` (array[integer]) — Массив числовых ID ярлыков.  Что бы снять ярлыки с карточки товара, необходимо передать пустой массив.  Чтобы добавить ярлыки к уже имеющимся в карточ

**Response 200:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 400:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

**Response 403:**

- `data` (object) — Данные ошибки
- `error` (boolean) — Флаг ошибки
- `errorText` (string) — Текст ошибки
- `additionalErrors` (string) — Дополнительные ошибки

---


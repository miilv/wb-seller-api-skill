# Тарифы

Узнать больше о комиссиях и тарифах можно в [справочном центре](https://seller.wildberries.ru/instructions/category/a04560b5-256d-48cb-8f09-60e283b5d493)

В разделе описаны методы получения:
  1. [Комиссий](/openapi/wb-tariffs#tag/Komissii)
  2. [Тарифов на остаток](/openapi/wb-tariffs#tag/Tarify-na-ostatok)
  3. [Тарифов на возврат товаров продавцу](/openapi/wb-tariffs#tag/Stoimost-vozvrata-prodavcu)

## Комиссии

### `GET /api/v1/tariffs/commission`

**Комиссия по категориям товаров**

Метод возвращает данные о [комиссии](https://seller.wildberries.ru/dynamic-product-categories/commission) WB по [родительским категориям товаров](/openapi/work-with-products#tag/Kategorii-predmety-i-harakteristiki/paths/~1content~1v2~1object~1parent~1all/get) согласно модели продаж.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 ...

**Parameters:**

- `?` (in ?, )

**Response 200:**

---

## Стоимость возврата продавцу

### `GET /api/v1/tariffs/return`

**Тарифы на возврат**

Метод возвращает [тарифы](https://seller.wildberries.ru/dynamic-product-categories/return-cost):
  - на перевозку товаров со склада WB или из пункта приёма до продавца
  - на обратную перевозку возвратов, которые не забрал продавец

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 60 запросов | 1 сек | 5 запросов |
| Сервисный | 1 мин | 60 запро...

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `response` (object)
  - `data` (object)

---

## Тарифы на остаток

### `GET /api/v1/tariffs/box`

**Тарифы для коробов**

Для остатков товаров, которые поставляются на склад в коробах, метод возвращает [тарифы](https://seller.wildberries.ru/dynamic-product-categories) на:
  - доставку со склада или пункта приёма до покупателя
  - доставку от покупателя до пункта приёма
  - хранение на складе WB

  Тарифы для коробов совпадают с тарифами для Суперсейфа

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | ...

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `response` (object)
  - `data` (object)

---

### `GET /api/v1/tariffs/pallet`

**Тарифы для монопаллет**

Для товаров, которые поставляются на склад WB на монопаллетах, метод возвращает [стоимость](https://seller.wildberries.ru/dynamic-product-categories):
  - доставки со склада до покупателя
  - доставки от покупателя до склада
  - хранения на складе WB

  Тарифы для монопаллет совпадают с тарифами для Поштучных паллет

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Пе...

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `response` (object)
  - `data` (object)

---

## Тарифы на поставку

### `GET /api/tariffs/v1/acceptance/coefficients`

**Тарифы на поставку**

Метод возвращает тарифы на поставку для конкретных складов на ближайшие 14 дней.

  Приёмка для поставки доступна только при сочетании: 
 coefficient — 0 или 1 
 и allowUnload — true

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 6 запросов | 10 сек | 6 запросов |
| Сервисный | 1 мин | 6 запросов | 10 сек | 6 запросов |
| Базовый | 1 ч | 1 за...

**Parameters:**

- `warehouseIDs` (in query, string) — ID складов. По умолчанию возвращаются данные по всем складам

**Response 200:**

_(array of objects:)_
- `date` (string) — Дата начала действия коэффициента
- `coefficient` (number) — Коэффициент приёмки:   - `-1` — приёмка недоступна, вне зависимости от значения поля `allowUnload`   - `0` — бесплатная приёмка   - от `1` — множитель
- `warehouseID` (integer) — ID склада. По нему можно получить [информацию о складе](./orders-fbw#tag/Informaciya-dlya-formirovaniya-postavok/paths/~1api~1v1~1warehouses/get)
- `warehouseName` (string) — Название склада
- `allowUnload` (boolean) — Доступность приёмки для поставок данного типа, смотри значение поля `boxTypeID`:   - `true` — приёмка доступна  - `false` — приёмка не доступна
- `boxTypeID` (integer) — ID типа поставки:   - `2` — Короба   - `5` — Монопаллеты   - `6` — Суперсейф  Для типа поставки **QR-поставка с коробами** поле не возвращается
- `storageCoef` (string) — Коэффициент хранения
- `deliveryCoef` (string) — Коэффициент логистики
- `deliveryBaseLiter` (string) — Стоимость логистики первого литра
- `deliveryAdditionalLiter` (string) — Стоимость логистики каждого следующего литра
- `storageBaseLiter` (string) — Стоимость хранения:   - для паллет — стоимость за одну паллету   - для коробов — стоимость хранения за первый литр
- `storageAdditionalLiter` (string) — Стоимость хранения каждого последующего литра:   - для паллет — всегда будет `null`, т.к. стоимость хранения за единицу паллеты определяется в `Storag
- `isSortingCenter` (boolean) — Тип склада:   - `true` — сортировочный центр (СЦ)  - `false` — обычный

**Response 400:**

- `status` (integer) — HTTP статус-код
- `title` (string) — ID ошибки
- `detail` (string) — Описание ошибки
- `requestId` (string) — ID запроса
- `origin` (string) — Сервис, вернувший ошибку

---


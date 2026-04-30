# Документы и бухгалтерия

Узнать больше о документах и бухгалтерии можно в [справочном центре](https://seller.wildberries.ru/instructions/category/ba929b64-1f89-4426-82d7-ce998ee552bd?goBackOption=prevRoute&categoryId=3c971375-9939-45e8-ab82-376019be8942)

Просмотр [баланса](/openapi/financial-reports-and-accounting#tag/Balans), [финансовых отчётов](/openapi/financial-reports-and-accounting#tag/Finansovye-otchyoty) и [документов](/openapi/financial-reports-and-accounting#tag/Dokumenty) продавца.

## Баланс

### `GET /api/v1/account/balance`

**Получить баланс продавца**

Метод возвращает данные виджета баланса на [главной странице](https://seller.wildberries.ru) портала продавцов.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Сервисный | 1 мин | 1 запрос | 1 мин | 1 запрос |
| Базовый | 24 ч | 1 запрос | 24 ч | 1 запрос |

**Response 200:**

- `currency` (string) — Валюта
- `current` (number) — Текущий баланс продавца
- `for_withdraw` (number) — Сумма, доступная к выводу

---

## Документы

### `GET /api/v1/documents/categories`

**Категории документов**

Метод возвращает категории документов для получения [списка документов продавца](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1list/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 10 сек | 1 запрос | 10 сек | 5 запросов |
| Сервисный | 10 сек | 1 запрос | 10 сек | 5 запросов |
| Базовый | 24 ч | 1 запрос | 2...

**Parameters:**

- `?` (in ?, )

**Response 200:**

- `data` (object)
  - `categories` (array[object]) — Категории документов

---

### `GET /api/v1/documents/list`

**Список документов**

Метод возвращает список документов продавца. Вы можете получить [один](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1download/get) или [несколько](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1download~1all/post) документов из полученного списка.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |...

**Parameters:**

- `?` (in ?, )
- `beginTime` (in query, string) — Начало периода. Только вместе с `endTime`
- `endTime` (in query, string) — Конец периода. Только вместе с `beginTime`
- `sort` (in query, enum: date, category) — Сортировка:   - `date` — по дате создания документа   - `category` — по категории (только при `locale=ru`)  Только вместе с `order`
- `order` (in query, enum: desc, asc) — Сортировка:   - `desc` — по убыванию   - `asc` — по возрастанию  Только вместе с `sort`
- `category` (in query, string) — ID [категории документов](./financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1categories/get) из поля `name`
- `serviceName` (in query, string) — Уникальный ID документа
- `limit` (in query, integer) — Максимальное количество строк ответа
- `offset` (in query, integer) — После какой строки выдавать данные

**Response 200:**

- `data` (object)
  - `documents` (array[object]) — Категории документов

---

### `GET /api/v1/documents/download`

**Получить документ**

Метод загружает один документ из [списка документов продавца](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1list/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 10 сек | 1 запрос | 10 сек | 5 запросов |
| Сервисный | 10 сек | 1 запрос | 10 сек | 5 запросов |
| Базовый | 24 ч | 1 запрос | 24 ч | 1 запрос |

**Parameters:**

- `serviceName` (in query, string) **(required)** — Уникальный ID документа
- `extension` (in query, string) **(required)** — Формат документа

**Response 200:**

- `data` (object)
  - `fileName` (string) — Название документа
  - `extension` (string) — Формат документа
  - `document` (string) — Документ в кодировке base64

---

### `POST /api/v1/documents/download/all`

**Получить документы**

Метод загружает несколько документов из [списка документов продавца](/openapi/financial-reports-and-accounting#tag/Dokumenty/paths/~1api~1v1~1documents~1list/get).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 5 мин | 1 запрос | 5 мин | 5 запросов |
| Сервисный | 5 мин | 1 запрос | 5 мин | 5 запросов |
| Базовый | 24 ч | 1 запрос | 24 ч | 1 запрос |

**Request body:**

- `params` (array[object])

**Response 200:**

- `data` (object)
  - `fileName` (string) — Название документа
  - `extension` (string) — Формат документа
  - `document` (string) — Документ в кодировке base64

---

## Финансовые отчёты

### `POST /api/finance/v1/sales-reports/list`

**Список отчётов реализации**

Operation ID: `postV1SalesReportsList`

Метод доступен по [типам токенов](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API): Персональный, Сервисный 

Метод возвращает список отчётов релизации по формату [таблицы отчётов](https://seller.wildberries.ru/suppliers-mutual-settlements).

Данные доступны с 1 января 2025 года.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 1 зап...

**Request body:**

- `dateFrom` (string) **(required)** — Начальная дата отчёта. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд. Дата передаётся в формат
- `dateTo` (string) **(required)** — Конечная дата отчёта. Дата в формате [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339). Можно передать дату или дату со временем. Время можно у
- `limit` (integer) — Количество отчётов в ответе
- `offset` (integer) — Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента
- `period` (enum) — Values: `daily, weekly`. Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные

**Response 200:**

_(array of objects:)_
- `reportId` (integer(int64)) **(required)** — ID отчёта
- `sellerFinanceName` (string) **(required)** — Наименование продавца
- `dateFrom` (string(date)) **(required)** — Дата начала отчётного периода
- `dateTo` (string(date)) **(required)** — Дата конца отчётного периода
- `createDate` (string(date)) **(required)** — Дата формирования отчёта
- `currency` (string) **(required)** — Валюта отчёта
- `reportType` (enum) **(required)** — Values: `1, 2, 3`. Тип отчёта:   - `1` — основной   - `2` — по выкупам   - `3` — по выкупам для Грузии
- `retailAmountSum` (string) **(required)** — Продажа
- `forPaySum` (string) **(required)** — К перечислению за товар
- `avgSalePercent` (number) **(required)** — Согласованная скидка, %
- `deliveryServiceSum` (string) **(required)** — Стоимость логистики
- `paidStorageSum` (string) **(required)** — Стоимость хранения
- `paidAcceptanceSum` (string) **(required)** — Стоимость операций при приёмке
- `deductionSum` (string) **(required)** — Прочие удержания и выплаты
- `penaltySum` (string) **(required)** — Общая сумма штрафов
- `additionalPaymentSum` (string) **(required)** — Корректировка Вознаграждения Вайлдберриз (ВВ)
- `cashbackAmountSum` (string) **(required)** — Сумма, удержанная за начисленные баллы программы лояльности
- `cashbackDiscountSum` (string) **(required)** — Компенсация скидки по программе лояльности
- `cashbackCommissionChangeSum` (string) **(required)** — Стоимость участия в программе лояльности
- `paymentSchedule` (string) **(required)** — Разовое изменение срока перечисления денежных средств
- `bankPaymentSum` (string) **(required)** — Итого к оплате

---

### `POST /api/finance/v1/sales-reports/detailed/{reportId}`

**Детализации к отчётам реализации по ID отчётов**

Operation ID: `postV1SalesReportsDetailedReportId`

Метод доступен по [типам токенов](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API): Персональный, Сервисный 

Метод возвращает детализации к [отчётам реализации](https://seller.wildberries.ru/suppliers-mutual-settlements) по ID отчётов.

Данные доступны с 1 января 2025 года.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 1 запрос |...

**Parameters:**

- `reportId` (in path, integer) **(required)** — ID отчёта. Для ежедневных отчётов вместо стандартной десериализации рекомендуем использовать нестандартные библиотеки с поддержкой [BigInt](https://ww

**Request body:**

- `limit` (integer) — Количество строк в ответе
- `rrdId` (integer) — ID строки ответа. Необходим для получения отчёта частями. Начинайте загрузку отчёта с `"rrdid":0`. В последующих запросах передавайте значение `rrdId`
- `fields` (array[string]) — Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все поля

**Response 200:**

_(array of objects:)_
- `reportId` (integer(int64)) **(required)** — ID отчёта
- `dateFrom` (string(date)) **(required)** — Дата начала отчётного периода
- `dateTo` (string(date)) **(required)** — Дата конца отчётного периода
- `createDate` (string(date)) **(required)** — Дата формирования отчёта
- `currency` (string) **(required)** — Валюта отчёта
- `reportType` (enum) **(required)** — Values: `1, 2, 3`. Тип отчёта:   - `1` — основной   - `2` — по выкупам   - `3` — по выкупам для Грузии
- `rrdId` (integer) **(required)** — ID строки
- `giId` (integer) **(required)** — ID поставки
- `dlvPrc` (number) **(required)** — Фиксированный коэффициент склада по поставке
- `fixTariffDateFrom` (string(date)) **(required)** — Дата начала действия фиксации
- `fixTariffDateTo` (string(date)) **(required)** — Дата конца действия фиксации
- `subjectName` (string) **(required)** — Предмет
- `nmId` (integer) **(required)** — Артикул WB
- `brandName` (string) **(required)** — Бренд
- `vendorCode` (string) **(required)** — Артикул продавца
- `title` (string) **(required)** — Название товара
- `techSize` (string) **(required)** — Размер
- `sku` (string) **(required)** — Баркод
- `docTypeName` (string) **(required)** — Тип документа
- `quantity` (integer) **(required)** — Количество
- `retailPrice` (string) **(required)** — Цена розничная
- `retailAmount` (string) **(required)** — Вайлдберриз реализовал Товар (Пр)
- `salePercent` (integer) **(required)** — Согласованный продуктовый дисконт, %
- `commissionPercent` (number) **(required)** — Размер кВВ, %
- `officeName` (string) **(required)** — Склад
- `sellerOperName` (string) **(required)** — Обоснование для оплаты
- `orderDt` (string(date-time)) **(required)** — Дата и время заказа
- `saleDt` (string(date-time)) **(required)** — Дата и время продажи
- `rrDate` (string(date)) **(required)** — Дата операции
- `shkId` (integer) **(required)** — Штрихкод
- `retailPriceWithDisc` (string) **(required)** — Цена розничная с учётом согласованной скидки
- `deliveryAmount` (integer) **(required)** — Количество доставок
- `returnAmount` (integer) **(required)** — Количество возврата
- `deliveryService` (string) **(required)** — Услуги по доставке товара покупателю
- `giBoxTypeName` (string) **(required)** — Тип коробов
- `productDiscountForReport` (number) **(required)** — Итоговая согласованная скидка, %
- `sellerPromo` (string) **(required)** — Промокод, %
- `spp` (number) **(required)** — Платформенные скидки, %
- `kvwBase` (number) **(required)** — Размер кВВ без НДС, % базовый
- `kvw` (number) **(required)** — Итоговый кВВ без НДС, %
- `supRatingUp` (number) **(required)** — Размер снижения кВВ из-за рейтинга, %
- `isKgvpV2` (number) **(required)** — Размер снижения кВВ из-за акции, %
- `ppvzSalesCommission` (string) **(required)** — Вознаграждение с продаж до вычета услуг поверенного, без НДС
- `forPay` (string) **(required)** — К перечислению продавцу за реализованный товар
- `ppvzReward` (string) **(required)** — Возмещение за выдачу и возврат товаров на ПВЗ
- `acquiringFee` (string) **(required)** — Компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов
- `acquiringPercent` (number) **(required)** — Размер компенсации платёжных услуг/Комиссии за интеграцию платёжных сервисов, %
- `paymentProcessing` (string) **(required)** — Тип платежа: компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов
- `acquiringBank` (string) **(required)** — Наименование банка-эквайера
- `vw` (string) **(required)** — Вознаграждение Вайлдберриз (ВВ), без НДС
- `vwNds` (string) **(required)** — НДС с вознаграждения Вайлдберриз
- `ppvzOfficeName` (string) **(required)** — Наименование офиса доставки
- `ppvzOfficeId` (integer) **(required)** — ID офиса доставки
- `ppvzSupplierName` (string) **(required)** — Партнёр
- `ppvzSupplierInn` (string) **(required)** — ИНН партнёра
- `declarationNumber` (string) **(required)** — Номер таможенной декларации
- `bonusTypeName` (string) — Виды логистики, штрафов и корректировок ВВ
- `stickerId` (string) **(required)** — Стикер МП
- `country` (string) **(required)** — Страна продажи
- `srvDbs` (boolean) **(required)** — Признак услуги платной доставки
- `penalty` (string) **(required)** — Общая сумма штрафов
- `additionalPayment` (string) **(required)** — Корректировка Вознаграждения Вайлдберриз (ВВ)
- `rebillLogisticCost` (string) **(required)** — Возмещение издержек по перевозке/по складским операциям с товаром
- `rebillLogisticOrg` (string) — Организатор перевозки
- `paidStorage` (string) **(required)** — Хранение
- `deduction` (string) **(required)** — Удержания
- `paidAcceptance` (string) **(required)** — Операции на приёмке
- `orderId` (integer) **(required)** — ID сборочного задания
- `kiz` (string) — Код маркировки [Честного знака](https://честныйзнак.рф/)
- `isB2b` (boolean) **(required)** — Признак B2B-продажи
- `trbxId` (string) **(required)** — ID короба для обработки товара
- `installmentCofinancingAmount` (string) **(required)** — Скидка по программе софинансирования
- `wibesDiscountPercent` (number) **(required)** — Скидка Wibes, %
- `cashbackAmount` (string) **(required)** — Сумма, удержанная за начисленные баллы программы лояльности
- `cashbackDiscount` (string) **(required)** — Компенсация скидки по программе лояльности
- `cashbackCommissionChange` (string) **(required)** — Стоимость участия в программе лояльности
- `paymentSchedule` (string) **(required)** — Разовое изменение срока перечисления денежных средств
- `deliveryMethod` (string) **(required)** — Способ продажи и тип товара
- `sellerPromoId` (integer) **(required)** — ID собственной акции продавца с дополнительной скидкой
- `sellerPromoDiscount` (number) **(required)** — Размер дополнительной скидки по собственной акции продавца, %
- `loyaltyId` (integer) **(required)** — ID скидки лояльности от продавца
- `loyaltyDiscount` (number) **(required)** — Размер скидки лояльности от продавца, %
- `uuidPromocode` (string) **(required)** — ID промокода
- `salePricePromocodeDiscountPrc` (number) **(required)** — Скидка за промокод, %
- `articleSubstitution` (string) **(required)** — ID подменного артикула
- `salePriceAffiliatedDiscountPrc` (number) **(required)** — Скидка по подменному артикулу, %
- `agencyVat` (number) — Удержание Агентского НДС, %. Только для продавцов из Кыргызстана
- `salePriceWholesaleDiscountPrc` (number) **(required)** — Оптовая скидка для бизнеса, %
- `orderUid` (string) **(required)** — ID корзины заказа — транзакции. Заказы в одной корзине покупателя будут иметь одинаковый `orderUid`
- `srid` (string) **(required)** — ID заказа. В ответах методов сборочных заданий [FBS](./orders-fbs#tag/Sborochnye-zadaniya-FBS), [DBW](./orders-dbw#tag/Sborochnye-zadaniya-DBW), [DBS]

---

### `POST /api/finance/v1/sales-reports/detailed`

**Детализации к отчётам реализации за период**

Operation ID: `postV1SalesReportsDetailed`

Метод возвращает детализации к [отчётам реализации](https://seller.wildberries.ru/suppliers-mutual-settlements) за указанный период.

Данные доступны с 29 января 2024 года.

  Вы можете выгрузить данные в [Google Таблицы](https://dev.wildberries.ru/knowledge-base/articles/019d49a4-650c-7b04-9596-ba441936f9d3)

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 1 запрос | 1 ...

**Request body:**

- `dateFrom` (string) **(required)** — Начальная дата отчёта. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд. Дата передаётся в формат
- `dateTo` (string) **(required)** — Конечная дата отчёта. Дата в формате [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339). Можно передать дату или дату со временем. Время можно у
- `limit` (integer) — Количество строк в ответе
- `rrdId` (integer) — ID строки ответа. Необходим для получения отчёта частями. Начинайте загрузку отчёта с `"rrdid":0`. В последующих запросах передавайте значение `rrdId`
- `period` (enum) — Values: `daily, weekly`. Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные
- `fields` (array[string]) — Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все поля

**Response 200:**

_(array of objects:)_
- `reportId` (integer(int64)) **(required)** — ID отчёта
- `dateFrom` (string(date)) **(required)** — Дата начала отчётного периода
- `dateTo` (string(date)) **(required)** — Дата конца отчётного периода
- `createDate` (string(date)) **(required)** — Дата формирования отчёта
- `currency` (string) **(required)** — Валюта отчёта
- `reportType` (enum) **(required)** — Values: `1, 2, 3`. Тип отчёта:   - `1` — основной   - `2` — по выкупам   - `3` — по выкупам для Грузии
- `rrdId` (integer) **(required)** — ID строки
- `giId` (integer) **(required)** — ID поставки
- `dlvPrc` (number) **(required)** — Фиксированный коэффициент склада по поставке
- `fixTariffDateFrom` (string(date)) **(required)** — Дата начала действия фиксации
- `fixTariffDateTo` (string(date)) **(required)** — Дата конца действия фиксации
- `subjectName` (string) **(required)** — Предмет
- `nmId` (integer) **(required)** — Артикул WB
- `brandName` (string) **(required)** — Бренд
- `vendorCode` (string) **(required)** — Артикул продавца
- `title` (string) **(required)** — Название товара
- `techSize` (string) **(required)** — Размер
- `sku` (string) **(required)** — Баркод
- `docTypeName` (string) **(required)** — Тип документа
- `quantity` (integer) **(required)** — Количество
- `retailPrice` (string) **(required)** — Цена розничная
- `retailAmount` (string) **(required)** — Вайлдберриз реализовал Товар (Пр)
- `salePercent` (integer) **(required)** — Согласованный продуктовый дисконт, %
- `commissionPercent` (number) **(required)** — Размер кВВ, %
- `officeName` (string) **(required)** — Склад
- `sellerOperName` (string) **(required)** — Обоснование для оплаты
- `orderDt` (string(date-time)) **(required)** — Дата и время заказа
- `saleDt` (string(date-time)) **(required)** — Дата и время продажи
- `rrDate` (string(date)) **(required)** — Дата операции
- `shkId` (integer) **(required)** — Штрихкод
- `retailPriceWithDisc` (string) **(required)** — Цена розничная с учётом согласованной скидки
- `deliveryAmount` (integer) **(required)** — Количество доставок
- `returnAmount` (integer) **(required)** — Количество возврата
- `deliveryService` (string) **(required)** — Услуги по доставке товара покупателю
- `giBoxTypeName` (string) **(required)** — Тип коробов
- `productDiscountForReport` (number) **(required)** — Итоговая согласованная скидка, %
- `sellerPromo` (string) **(required)** — Промокод, %
- `spp` (number) **(required)** — Платформенные скидки, %
- `kvwBase` (number) **(required)** — Размер кВВ без НДС, % базовый
- `kvw` (number) **(required)** — Итоговый кВВ без НДС, %
- `supRatingUp` (number) **(required)** — Размер снижения кВВ из-за рейтинга, %
- `isKgvpV2` (number) **(required)** — Размер снижения кВВ из-за акции, %
- `ppvzSalesCommission` (string) **(required)** — Вознаграждение с продаж до вычета услуг поверенного, без НДС
- `forPay` (string) **(required)** — К перечислению продавцу за реализованный товар
- `ppvzReward` (string) **(required)** — Возмещение за выдачу и возврат товаров на ПВЗ
- `acquiringFee` (string) **(required)** — Компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов
- `acquiringPercent` (number) **(required)** — Размер компенсации платёжных услуг/Комиссии за интеграцию платёжных сервисов, %
- `paymentProcessing` (string) **(required)** — Тип платежа: компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов
- `acquiringBank` (string) **(required)** — Наименование банка-эквайера
- `vw` (string) **(required)** — Вознаграждение Вайлдберриз (ВВ), без НДС
- `vwNds` (string) **(required)** — НДС с вознаграждения Вайлдберриз
- `ppvzOfficeName` (string) **(required)** — Наименование офиса доставки
- `ppvzOfficeId` (integer) **(required)** — ID офиса доставки
- `ppvzSupplierName` (string) **(required)** — Партнёр
- `ppvzSupplierInn` (string) **(required)** — ИНН партнёра
- `declarationNumber` (string) **(required)** — Номер таможенной декларации
- `bonusTypeName` (string) — Виды логистики, штрафов и корректировок ВВ
- `stickerId` (string) **(required)** — Стикер МП
- `country` (string) **(required)** — Страна продажи
- `srvDbs` (boolean) **(required)** — Признак услуги платной доставки
- `penalty` (string) **(required)** — Общая сумма штрафов
- `additionalPayment` (string) **(required)** — Корректировка Вознаграждения Вайлдберриз (ВВ)
- `rebillLogisticCost` (string) **(required)** — Возмещение издержек по перевозке/по складским операциям с товаром
- `rebillLogisticOrg` (string) — Организатор перевозки
- `paidStorage` (string) **(required)** — Хранение
- `deduction` (string) **(required)** — Удержания
- `paidAcceptance` (string) **(required)** — Операции на приёмке
- `orderId` (integer) **(required)** — ID сборочного задания
- `kiz` (string) — Код маркировки [Честного знака](https://честныйзнак.рф/)
- `isB2b` (boolean) **(required)** — Признак B2B-продажи
- `trbxId` (string) **(required)** — ID короба для обработки товара
- `installmentCofinancingAmount` (string) **(required)** — Скидка по программе софинансирования
- `wibesDiscountPercent` (number) **(required)** — Скидка Wibes, %
- `cashbackAmount` (string) **(required)** — Сумма, удержанная за начисленные баллы программы лояльности
- `cashbackDiscount` (string) **(required)** — Компенсация скидки по программе лояльности
- `cashbackCommissionChange` (string) **(required)** — Стоимость участия в программе лояльности
- `paymentSchedule` (string) **(required)** — Разовое изменение срока перечисления денежных средств
- `deliveryMethod` (string) **(required)** — Способ продажи и тип товара
- `sellerPromoId` (integer) **(required)** — ID собственной акции продавца с дополнительной скидкой
- `sellerPromoDiscount` (number) **(required)** — Размер дополнительной скидки по собственной акции продавца, %
- `loyaltyId` (integer) **(required)** — ID скидки лояльности от продавца
- `loyaltyDiscount` (number) **(required)** — Размер скидки лояльности от продавца, %
- `uuidPromocode` (string) **(required)** — ID промокода
- `salePricePromocodeDiscountPrc` (number) **(required)** — Скидка за промокод, %
- `articleSubstitution` (string) **(required)** — ID подменного артикула
- `salePriceAffiliatedDiscountPrc` (number) **(required)** — Скидка по подменному артикулу, %
- `agencyVat` (number) — Удержание Агентского НДС, %. Только для продавцов из Кыргызстана
- `salePriceWholesaleDiscountPrc` (number) **(required)** — Оптовая скидка для бизнеса, %
- `orderUid` (string) **(required)** — ID корзины заказа — транзакции. Заказы в одной корзине покупателя будут иметь одинаковый `orderUid`
- `srid` (string) **(required)** — ID заказа. В ответах методов сборочных заданий [FBS](./orders-fbs#tag/Sborochnye-zadaniya-FBS), [DBW](./orders-dbw#tag/Sborochnye-zadaniya-DBW), [DBS]

---

### `GET /api/v5/supplier/reportDetailByPeriod`

**Отчёт о продажах по реализации**

Данный метод устарел. Он будет удалён [15 июля](https://dev.wildberries.ru/release-notes?id=498).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Сервисный | 1 мин | 1 запрос | 1 мин | 10 запросов |
| Базовый | 24 ч | 2 запроса | 12 ч | 1 запрос |

**Parameters:**

- `dateFrom` (in query, string) **(required)** — Начальная дата отчёта.  Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд.
- `dateTo` (in query, string) **(required)** — Конечная дата отчёта
- `limit` (in query, integer) — Количество строк в ответе
- `rrdid` (in query, integer) — Уникальный ID строки отчёта. Необходим для получения отчёта частями.  Загрузку отчёта нужно начинать с `rrdid = 0` и при последующих вызовах API перед
- `period` (in query, enum: weekly, daily) — Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные

**Response 200:**

_(array of objects:)_
- `realizationreport_id` (integer) — Номер отчёта
- `date_from` (string(date)) — Дата начала отчётного периода
- `date_to` (string(date)) — Дата конца отчётного периода
- `create_dt` (string(date)) — Дата формирования отчёта
- `currency_name` (string) — Валюта отчёта
- `suppliercontract_code` (object) — Договор
- `rrd_id` (integer) — Номер строки
- `gi_id` (integer) — Номер поставки
- `dlv_prc` (number) — Фиксированный коэффициент склада по поставке
- `fix_tariff_date_from` (string(date)) — Дата начала действия фиксации
- `fix_tariff_date_to` (string(date)) — Дата конца действия фиксации
- `subject_name` (string) — Предмет
- `nm_id` (integer) — Артикул WB
- `brand_name` (string) — Бренд
- `sa_name` (string) — Артикул продавца
- `ts_name` (string) — Размер
- `barcode` (string) — Баркод
- `doc_type_name` (string) — Тип документа
- `quantity` (integer) — Количество
- `retail_price` (number) — Цена розничная
- `retail_amount` (number) — Вайлдберриз реализовал Товар (Пр)
- `sale_percent` (integer) — Согласованный продуктовый дисконт, %
- `commission_percent` (number) — Размер кВВ, %
- `office_name` (string) — Склад
- `supplier_oper_name` (string) — Обоснование для оплаты
- `order_dt` (string(date-time)) — Дата заказа.  Присылается с явным указанием часового пояса
- `sale_dt` (string(date-time)) — Дата продажи.  Присылается с явным указанием часового пояса
- `rr_dt` (string(date)) — Дата операции
- `shk_id` (integer) — Штрихкод
- `retail_price_withdisc_rub` (number) — Цена розничная с учётом согласованной скидки
- `delivery_amount` (integer) — Количество доставок
- `return_amount` (integer) — Количество возврата
- `delivery_rub` (number) — Услуги по доставке товара покупателю
- `gi_box_type_name` (string) — Тип коробов
- `product_discount_for_report` (number) — Итоговая согласованная скидка, %
- `supplier_promo` (number) — Промокод, %
- `ppvz_spp_prc` (number) — Скидка постоянного Покупателя (СПП), %
- `ppvz_kvw_prc_base` (number) — Размер кВВ без НДС, % базовый
- `ppvz_kvw_prc` (number) — Итоговый кВВ без НДС, %
- `sup_rating_prc_up` (number) — Размер снижения кВВ из-за рейтинга, %
- `is_kgvp_v2` (number) — Размер снижения кВВ из-за акции, %
- `ppvz_sales_commission` (number) — Вознаграждение с продаж до вычета услуг поверенного, без НДС
- `ppvz_for_pay` (number) — К перечислению продавцу за реализованный товар
- `ppvz_reward` (number) — Возмещение за выдачу и возврат товаров на ПВЗ
- `acquiring_fee` (number) — Компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов
- `acquiring_percent` (number) — Размер компенсации платёжных услуг/Комиссии за интеграцию платёжных сервисов, %
- `payment_processing` (string) — Тип платежа: компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов
- `acquiring_bank` (string) — Наименование банка-эквайера
- `ppvz_vw` (number) — Вознаграждение Вайлдберриз (ВВ), без НДС
- `ppvz_vw_nds` (number) — НДС с вознаграждения Вайлдберриз
- `ppvz_office_name` (string) — Наименование офиса доставки
- `ppvz_office_id` (integer) — Номер офиса доставки
- `ppvz_supplier_id` (integer) — Номер партнёра
- `ppvz_supplier_name` (string) — Партнёр
- `ppvz_inn` (string) — ИНН партнёра
- `declaration_number` (string) — Номер таможенной декларации
- `bonus_type_name` (string) — Виды логистики, штрафов и корректировок ВВ.  Поле будет в ответе при наличии значения
- `sticker_id` (string) — Цифровое значение стикера, который клеится на товар в процессе сборки заказа по схеме "Маркетплейс"
- `site_country` (string) — Страна продажи
- `srv_dbs` (boolean) — Признак услуги платной доставки
- `penalty` (number) — Общая сумма штрафов
- `additional_payment` (number) — Корректировка Вознаграждения Вайлдберриз (ВВ)
- `rebill_logistic_cost` (number) — Возмещение издержек по перевозке/по складским операциям с товаром
- `rebill_logistic_org` (string) — Организатор перевозки.  Поле будет в ответе при наличии значения
- `storage_fee` (number) — Хранение
- `deduction` (number) — Удержания
- `acceptance` (number) — Операции на приёмке
- `assembly_id` (integer) — Номер сборочного задания
- `kiz` (string) — Код маркировки [Честного знака](https://честныйзнак.рф/).  Поле будет в ответе при наличии значения
- `srid` (string) — Уникальный ID заказа.  Примечание для использующих API Marketplace: `srid` равен `rid` в ответах методов сборочных заданий.
- `report_type` (enum) — Values: `1, 2, 3`. Тип отчёта:   - `1` — основной   - `2` — по выкупам   - `3` — по выкупам для Грузии
- `is_legal_entity` (boolean) — Признак B2B-продажи
- `trbx_id` (string) — Номер короба для обработки товара
- `installment_cofinancing_amount` (number) — Скидка по программе софинансирования
- `wibes_wb_discount_percent` (number) — Скидка Wibes, %
- `cashback_amount` (number) — Сумма, удержанная за начисленные баллы программы лояльности
- `cashback_discount` (number) — Компенсация скидки по программе лояльности
- `cashback_commission_change` (number(decimal)) — Стоимость участия в программе лояльности
- `order_uid` (string) — ID транзакции. Заказы в одной корзине покупателя будут иметь одинаковый `order_uid`
- `payment_schedule` (number(decimal)) — Разовое изменение срока перечисления денежных средств
- `delivery_method` (string) — Способ продажи и тип товара
- `seller_promo_id` (integer) — ID собственной акции продавца с дополнительной скидкой
- `seller_promo_discount` (number) — Размер дополнительной скидки по собственной акции продавца, %
- `loyalty_id` (integer) — ID скидки лояльности от продавца
- `loyalty_discount` (number) — Размер скидки лояльности от продавца, %
- `uuid_promocode` (string) — ID промокода
- `sale_price_promocode_discount_prc` (number) — Скидка за промокод, %
- `article_substitution` (string) — ID подменного артикула
- `sale_price_affiliated_discount_prc` (number) — Скидка по подменному артикулу, %
- `agency_vat` (number) — Удержание Агентского НДС, %. Только для продавцов из Кыргызстана.  Поле будет в ответе при наличии значения
- `sale_price_wholesale_discount_prc` (number) — Оптовая скидка для бизнеса, %

---

### `POST /api/finance/v1/acquiring/list`

**Список отчётов об издержках на приём платежей**

Operation ID: `postV1AcquiringList`

Метод доступен по [типам токенов](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API): Персональный, Сервисный 

Метод возвращает список отчётов об издержках на приём платежей по формату [таблицы отчётов](https://seller.wildberries.ru/suppliers-mutual-settlements/reports-implementations/acquiring-reports).

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | ---...

**Request body:**

- `dateFrom` (string) **(required)** — Начальная дата отчёта. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд. Дата передаётся в формат
- `dateTo` (string) **(required)** — Конечная дата отчёта. Дата в формате [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339). Можно передать дату или дату со временем. Время можно у
- `limit` (integer) — Количество отчётов в ответе
- `offset` (integer) — Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента

**Response 200:**

_(array of objects:)_
- `reportId` (integer(int64)) **(required)** — ID отчёта
- `sellerFinanceName` (string) **(required)** — Наименование продавца
- `dateFrom` (string(date)) **(required)** — Дата начала отчётного периода
- `dateTo` (string(date)) **(required)** — Дата конца отчётного периода
- `createDate` (string(date)) **(required)** — Дата формирования отчёта
- `currency` (string) **(required)** — Валюта отчёта
- `acquiringFeeSum` (string) **(required)** — Сумма издержек по эквайрингу
- `acquiringFeeVatSum` (string) **(required)** — В том числе НДС

---

### `POST /api/finance/v1/acquiring/detailed/{reportId}`

**Детализации к отчётам об издержках на приём платежей по ID отчётов**

Operation ID: `postV1AcquiringDetailedReportId`

Метод доступен по [типам токенов](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API): Персональный, Сервисный 

Метод возвращает детализации к [отчётам об издержках на приём платежей](https://seller.wildberries.ru/suppliers-mutual-settlements/reports-implementations/acquiring-reports) по ID отчётов.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | ---...

**Parameters:**

- `reportId` (in path, integer) **(required)** — ID отчёта

**Request body:**

- `limit` (integer) — Количество строк в ответе
- `rrdId` (integer) — ID строки ответа. Необходим для получения отчёта частями. Начинайте загрузку отчёта с `"rrdid":0`. В последующих запросах передавайте значение `rrdId`
- `fields` (array[string]) — Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все поля

**Response 200:**

_(array of objects:)_
- `rrdId` (integer) **(required)** — ID строки
- `reportId` (integer(int64)) **(required)** — ID отчёта
- `acqDate` (string) **(required)** — Дата операции
- `acquiringBank` (string) **(required)** — Наименование банка-эквайера
- `tin` (string) **(required)** — ИНН
- `taxRegistrationReasonCode` (string) **(required)** — КПП
- `saleDate` (string) **(required)** — Дата продажи
- `srid` (string) **(required)** — ID заказа. В ответах методов сборочных заданий [FBS](./orders-fbs#tag/Sborochnye-zadaniya-FBS), [DBW](./orders-dbw#tag/Sborochnye-zadaniya-DBW), [DBS]
- `docTypeName` (string) **(required)** — Тип документа
- `nmId` (integer) **(required)** — Артикул WB
- `retailAmount` (string) **(required)** — Вайлдберриз реализовал Товар (Пр)
- `acquiringFee` (string) **(required)** — Размер комиссии за эквайринг, в том числе НДС
- `acquiringFeeVat` (string) **(required)** — Сумма НДС
- `invoiceNumber` (string) **(required)** — Номер счёта-фактуры
- `invoiceDate` (string) **(required)** — Дата счёта-фактуры
- `shkId` (integer) **(required)** — Штрихкод
- `currency` (string) **(required)** — Валюта отчёта

---

### `POST /api/finance/v1/acquiring/detailed`

**Детализации к отчётам об издержках на приём платежей за период**

Operation ID: `postV1AcquiringDetailed`

Метод доступен по [типам токенов](/openapi/api-information#tag/Avtorizaciya/Pravila-ispolzovaniya-tokenov-dostupa-k-API): Персональный, Сервисный 

Метод возвращает детализации к [отчётам об издержках на приём платежей](https://seller.wildberries.ru/suppliers-mutual-settlements/reports-implementations/acquiring-reports) за указанный период.

[Лимит запросов](/openapi/api-information#tag/Vvedenie/Limity-zaprosov) на один аккаунт продавца:

| Период | Лимит | Интервал | Всплеск |
| --- | --- | ---...

**Request body:**

- `dateFrom` (string) **(required)** — Начальная дата отчёта. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд. Дата передаётся в формат
- `dateTo` (string) **(required)** — Конечная дата отчёта. Дата в формате [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339). Можно передать дату или дату со временем. Время можно у
- `limit` (integer) — Количество строк в ответе
- `rrdId` (integer) — ID строки ответа. Необходим для получения отчёта частями. Начинайте загрузку отчёта с `"rrdid":0`. В последующих запросах передавайте значение `rrdId`
- `fields` (array[string]) — Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все поля

**Response 200:**

_(array of objects:)_
- `rrdId` (integer) **(required)** — ID строки
- `reportId` (integer(int64)) **(required)** — ID отчёта
- `acqDate` (string) **(required)** — Дата операции
- `acquiringBank` (string) **(required)** — Наименование банка-эквайера
- `tin` (string) **(required)** — ИНН
- `taxRegistrationReasonCode` (string) **(required)** — КПП
- `saleDate` (string) **(required)** — Дата продажи
- `srid` (string) **(required)** — ID заказа. В ответах методов сборочных заданий [FBS](./orders-fbs#tag/Sborochnye-zadaniya-FBS), [DBW](./orders-dbw#tag/Sborochnye-zadaniya-DBW), [DBS]
- `docTypeName` (string) **(required)** — Тип документа
- `nmId` (integer) **(required)** — Артикул WB
- `retailAmount` (string) **(required)** — Вайлдберриз реализовал Товар (Пр)
- `acquiringFee` (string) **(required)** — Размер комиссии за эквайринг, в том числе НДС
- `acquiringFeeVat` (string) **(required)** — Сумма НДС
- `invoiceNumber` (string) **(required)** — Номер счёта-фактуры
- `invoiceDate` (string) **(required)** — Дата счёта-фактуры
- `shkId` (integer) **(required)** — Штрихкод
- `currency` (string) **(required)** — Валюта отчёта

---


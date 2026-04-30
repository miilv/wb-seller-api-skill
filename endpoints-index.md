# Wildberries API — Endpoints Index

All endpoints below are pulled from the official Wildberries OpenAPI specs at https://dev.wildberries.ru/openapi/

Authentication: `Authorization: <token>` header on every request.


## Общее (01-general.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| API новостей | `GET /api/communications/v2/news` | Получение новостей портала продавцов | `` |
| Информация о продавце | `GET /api/common/v1/rating` | Получить рейтинг продавца | `getCommonV1Rating` |
| Информация о продавце | `GET /api/common/v1/subscriptions` | Получить информацию о подписке Джем | `getCommonV1Subscriptions` |
| Информация о продавце | `GET /api/v1/seller-info` | Получить информацию о продавце | `` |
| Проверка подключения к WB API | `GET /ping` | Проверка подключения | `` |
| Управление пользователями продавца | `DELETE /api/v1/user` | Удалить пользователя | `` |
| Управление пользователями продавца | `GET /api/v1/users` | Получить список активных или приглашённых пользователей продавца | `` |
| Управление пользователями продавца | `POST /api/v1/invite` | Создать приглашение для нового пользователя | `` |
| Управление пользователями продавца | `PUT /api/v1/users/access` | Изменить права доступа пользователей | `` |

## Работа с товарами (02-products.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Карточки товаров | `POST /content/v2/cards/delete/trash` | Перенос карточек товаров в корзину | `` |
| Карточки товаров | `POST /content/v2/cards/error/list` | Список несозданных карточек товаров с ошибками | `` |
| Карточки товаров | `POST /content/v2/cards/moveNm` | Объединение и разъединение карточек товаров | `` |
| Карточки товаров | `POST /content/v2/cards/recover` | Восстановление карточек товаров из корзины | `` |
| Карточки товаров | `POST /content/v2/cards/update` | Редактирование карточек товаров | `` |
| Карточки товаров | `POST /content/v2/get/cards/list` | Список карточек товаров | `` |
| Карточки товаров | `POST /content/v2/get/cards/trash` | Список карточек товаров в корзине | `` |
| Категории, предметы и характеристики | `GET /api/content/v1/brands` | Бренды | `` |
| Категории, предметы и характеристики | `GET /content/v2/directory/colors` | Цвет | `` |
| Категории, предметы и характеристики | `GET /content/v2/directory/countries` | Страна производства | `` |
| Категории, предметы и характеристики | `GET /content/v2/directory/kinds` | Пол | `` |
| Категории, предметы и характеристики | `GET /content/v2/directory/seasons` | Сезон | `` |
| Категории, предметы и характеристики | `GET /content/v2/directory/tnved` | ТНВЭД-код | `` |
| Категории, предметы и характеристики | `GET /content/v2/directory/vat` | Ставка НДС | `` |
| Категории, предметы и характеристики | `GET /content/v2/object/all` | Список предметов | `` |
| Категории, предметы и характеристики | `GET /content/v2/object/charcs/{subjectId}` | Характеристики предмета | `` |
| Категории, предметы и характеристики | `GET /content/v2/object/parent/all` | Родительские категории товаров | `` |
| Медиафайлы | `POST /content/v3/media/file` | Загрузить медиафайл | `` |
| Медиафайлы | `POST /content/v3/media/save` | Загрузить медиафайлы по ссылкам | `` |
| Остатки на складах продавца | `DELETE /api/v3/stocks/{warehouseId}` | Удалить остатки товаров | `` |
| Остатки на складах продавца | `POST /api/v3/stocks/{warehouseId}` | Получить остатки товаров | `` |
| Остатки на складах продавца | `PUT /api/v3/stocks/{warehouseId}` | Обновить остатки товаров | `` |
| Склады продавца | `DELETE /api/v3/warehouses/{warehouseId}` | Удалить склад продавца | `` |
| Склады продавца | `GET /api/v3/dbw/warehouses/{warehouseId}/contacts` | Список контактов | `` |
| Склады продавца | `GET /api/v3/offices` | Получить список складов WB | `` |
| Склады продавца | `GET /api/v3/warehouses` | Получить список складов продавца | `` |
| Склады продавца | `POST /api/v3/warehouses` | Создать склад продавца | `` |
| Склады продавца | `PUT /api/v3/dbw/warehouses/{warehouseId}/contacts` | Обновить список контактов | `` |
| Склады продавца | `PUT /api/v3/warehouses/{warehouseId}` | Обновить склад продавца | `` |
| Создание карточек товаров | `GET /content/v2/cards/limits` | Лимиты карточек товаров | `` |
| Создание карточек товаров | `POST /content/v2/barcodes` | Генерация баркодов | `` |
| Создание карточек товаров | `POST /content/v2/cards/upload` | Создание карточек товаров | `` |
| Создание карточек товаров | `POST /content/v2/cards/upload/add` | Создание карточек товаров с присоединением | `` |
| Цены и скидки | `GET /api/v2/buffer/goods/task` | Детализация необработанной загрузки | `` |
| Цены и скидки | `GET /api/v2/buffer/tasks` | Состояние необработанной загрузки | `` |
| Цены и скидки | `GET /api/v2/history/goods/task` | Детализация обработанной загрузки | `` |
| Цены и скидки | `GET /api/v2/history/tasks` | Состояние обработанной загрузки | `` |
| Цены и скидки | `GET /api/v2/list/goods/filter` | Получить товары с ценами | `` |
| Цены и скидки | `GET /api/v2/list/goods/size/nm` | Получить размеры товара с ценами | `` |
| Цены и скидки | `GET /api/v2/quarantine/goods` | Получить товары в карантине | `` |
| Цены и скидки | `POST /api/v2/list/goods/filter` | Получить товары с ценами по артикулам | `` |
| Цены и скидки | `POST /api/v2/upload/task` | Установить цены и скидки | `` |
| Цены и скидки | `POST /api/v2/upload/task/club-discount` | Установить скидки WB Клуба | `` |
| Цены и скидки | `POST /api/v2/upload/task/size` | Установить цены для размеров | `` |
| Ярлыки | `DELETE /content/v2/tag/{id}` | Удаление ярлыка | `` |
| Ярлыки | `GET /content/v2/tags` | Список ярлыков | `` |
| Ярлыки | `PATCH /content/v2/tag/{id}` | Изменение ярлыка | `` |
| Ярлыки | `POST /content/v2/tag` | Создание ярлыка | `` |
| Ярлыки | `POST /content/v2/tag/nomenclature/link` | Управление ярлыками в карточке товара | `` |

## Заказы FBS (03-orders-fbs.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Метаданные FBS | `DELETE /api/v3/orders/{orderId}/meta` | Удалить метаданные сборочного задания | `` |
| Метаданные FBS | `POST /api/marketplace/v3/orders/meta` | Получить метаданные сборочных заданий | `` |
| Метаданные FBS | `PUT /api/marketplace/v3/orders/{orderId}/meta/customs-declaration` | Закрепить за сборочным заданием номер ГТД | `` |
| Метаданные FBS | `PUT /api/v3/orders/{orderId}/meta/expiration` | Закрепить за сборочным заданием срок годности товара | `` |
| Метаданные FBS | `PUT /api/v3/orders/{orderId}/meta/gtin` | Закрепить за сборочным заданием GTIN | `` |
| Метаданные FBS | `PUT /api/v3/orders/{orderId}/meta/imei` | Закрепить за сборочным заданием IMEI | `` |
| Метаданные FBS | `PUT /api/v3/orders/{orderId}/meta/sgtin` | Закрепить за сборочным заданием код маркировки Честного знака | `` |
| Метаданные FBS | `PUT /api/v3/orders/{orderId}/meta/uin` | Закрепить за сборочным заданием УИН | `` |
| Поставки FBS | `DELETE /api/v3/supplies/{supplyId}` | Удалить поставку | `` |
| Поставки FBS | `DELETE /api/v3/supplies/{supplyId}/trbx` | Удалить грузоместа из поставки | `` |
| Поставки FBS | `GET /api/marketplace/v3/supplies/{supplyId}/order-ids` | Получить ID сборочных заданий поставки | `` |
| Поставки FBS | `GET /api/v3/supplies` | Получить список поставок | `` |
| Поставки FBS | `GET /api/v3/supplies/{supplyId}` | Получить информацию о поставке | `` |
| Поставки FBS | `GET /api/v3/supplies/{supplyId}/barcode` | Получить QR-код поставки | `` |
| Поставки FBS | `GET /api/v3/supplies/{supplyId}/trbx` | Получить список грузомест поставки | `` |
| Поставки FBS | `PATCH /api/marketplace/v3/supplies/{supplyId}/orders` | Добавить сборочные задания к поставке | `` |
| Поставки FBS | `PATCH /api/v3/supplies/{supplyId}/deliver` | Передать поставку в доставку | `` |
| Поставки FBS | `POST /api/v3/supplies` | Создать новую поставку | `` |
| Поставки FBS | `POST /api/v3/supplies/{supplyId}/trbx` | Добавить грузоместа к поставке | `` |
| Поставки FBS | `POST /api/v3/supplies/{supplyId}/trbx/stickers` | Получить стикеры грузомест поставки | `` |
| Пропуска FBS | `DELETE /api/v3/passes/{passId}` | Удалить пропуск | `` |
| Пропуска FBS | `GET /api/v3/passes` | Получить список пропусков | `` |
| Пропуска FBS | `GET /api/v3/passes/offices` | Получить список складов, для которых требуется пропуск | `` |
| Пропуска FBS | `POST /api/v3/passes` | Создать пропуск | `` |
| Пропуска FBS | `PUT /api/v3/passes/{passId}` | Обновить пропуск | `` |
| Сборочные задания FBS | `GET /api/marketplace/v3/fbs/orders/archive` | Получить список архивных сборочных заданий | `` |
| Сборочные задания FBS | `GET /api/v3/orders` | Получить информацию о сборочных заданиях | `` |
| Сборочные задания FBS | `GET /api/v3/orders/new` | Получить список новых сборочных заданий | `` |
| Сборочные задания FBS | `GET /api/v3/supplies/orders/reshipment` | Получить все сборочные задания для повторной отгрузки | `` |
| Сборочные задания FBS | `PATCH /api/v3/orders/{orderId}/cancel` | Отменить сборочное задание | `` |
| Сборочные задания FBS | `POST /api/v3/orders/client` | Заказы с информацией по клиенту | `` |
| Сборочные задания FBS | `POST /api/v3/orders/status` | Получить статусы сборочных заданий | `` |
| Сборочные задания FBS | `POST /api/v3/orders/status/history` | История статусов для сборочных заданий трансграничных поставок | `` |
| Сборочные задания FBS | `POST /api/v3/orders/stickers` | Получить стикеры сборочных заданий | `` |
| Сборочные задания FBS | `POST /api/v3/orders/stickers/cross-border` | Получить стикеры сборочных заданий трансграничных поставок | `` |

## Заказы DBW (04-orders-dbw.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Метаданные DBW | `DELETE /api/v3/dbw/orders/{orderId}/meta` | Удалить метаданные сборочного задания | `` |
| Метаданные DBW | `GET /api/v3/dbw/orders/{orderId}/meta` | Получить метаданные сборочного задания | `` |
| Метаданные DBW | `POST /api/marketplace/v3/dbw/orders/meta/details` | Получить метаданные сборочных заданий | `` |
| Метаданные DBW | `PUT /api/v3/dbw/orders/{orderId}/meta/gtin` | Закрепить за сборочным заданием GTIN | `` |
| Метаданные DBW | `PUT /api/v3/dbw/orders/{orderId}/meta/imei` | Закрепить за сборочным заданием IMEI | `` |
| Метаданные DBW | `PUT /api/v3/dbw/orders/{orderId}/meta/sgtin` | Закрепить за сборочным заданием код маркировки Честного знака | `` |
| Метаданные DBW | `PUT /api/v3/dbw/orders/{orderId}/meta/uin` | Закрепить за сборочным заданием УИН (уникальный идентификационный номер) | `` |
| Сборочные задания DBW | `GET /api/v3/dbw/orders` | Получить информацию о завершенных сборочных заданиях | `` |
| Сборочные задания DBW | `GET /api/v3/dbw/orders/new` | Получить список новых сборочных заданий | `` |
| Сборочные задания DBW | `PATCH /api/v3/dbw/orders/{orderId}/assemble` | Перевести в доставку | `` |
| Сборочные задания DBW | `PATCH /api/v3/dbw/orders/{orderId}/cancel` | Отменить сборочное задание | `` |
| Сборочные задания DBW | `PATCH /api/v3/dbw/orders/{orderId}/confirm` | Перевести на сборку | `` |
| Сборочные задания DBW | `POST /api/marketplace/v3/dbw/orders/client` | Информация о покупателе | `` |
| Сборочные задания DBW | `POST /api/v3/dbw/orders/courier` | Информация о курьере | `` |
| Сборочные задания DBW | `POST /api/v3/dbw/orders/delivery-date` | Дата и время доставки | `` |
| Сборочные задания DBW | `POST /api/v3/dbw/orders/status` | Получить статусы сборочных заданий | `` |
| Сборочные задания DBW | `POST /api/v3/dbw/orders/stickers` | Получить стикеры сборочных заданий | `` |

## Заказы DBS (05-orders-dbs.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/customs-declaration` | Закрепить за сборочными заданиями номер ГТД | `` |
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/delete` | Удалить метаданные сборочных заданий | `` |
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/details` | Получить метаданные сборочных заданий | `` |
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/gtin` | Закрепить GTIN за сборочными заданиями | `` |
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/imei` | Закрепить IMEI за сборочными заданиями | `` |
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/info` | Получить метаданные сборочных заданий | `` |
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/sgtin` | Закрепить коды маркировки Честного знака за сборочными заданиями | `` |
| Метаданные DBS | `POST /api/marketplace/v3/dbs/orders/meta/uin` | Закрепить УИН за сборочными заданиями | `` |
| Сборочные задания DBS | `GET /api/v3/dbs/orders` | Получить информацию о завершенных сборочных заданиях | `` |
| Сборочные задания DBS | `GET /api/v3/dbs/orders/new` | Получить список новых сборочных заданий | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/b2b/info` | Информация о покупателе B2B | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/status/cancel` | Отменить сборочные задания | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/status/confirm` | Перевести сборочные задания на сборку | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/status/deliver` | Перевести сборочные задания в доставку | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/status/info` | Получить статусы сборочных заданий | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/status/receive` | Сообщить о получении заказов | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/status/reject` | Сообщить об отказе от заказов | `` |
| Сборочные задания DBS | `POST /api/marketplace/v3/dbs/orders/stickers` | Получить стикеры для сборочных заданий с доставкой в ПВЗ | `` |
| Сборочные задания DBS | `POST /api/v3/dbs/groups/info` | Получить информацию о платной доставке | `` |
| Сборочные задания DBS | `POST /api/v3/dbs/orders/client` | Информация о покупателе | `` |
| Сборочные задания DBS | `POST /api/v3/dbs/orders/delivery-date` | Дата и время доставки | `` |

## Заказы Самовывоз (06-in-store-pickup.yaml)

**Server(s):** `https://marketplace-api.wildberries.ru`


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Метаданные Самовывоз | `DELETE /api/v3/click-collect/orders/{orderId}/meta` | Удалить метаданные сборочного задания | `` |
| Метаданные Самовывоз | `GET /api/v3/click-collect/orders/{orderId}/meta` | Получить метаданные сборочного задания | `` |
| Метаданные Самовывоз | `POST /api/marketplace/v3/click-collect/orders/meta/delete` | Удалить метаданные сборочных заданий | `` |
| Метаданные Самовывоз | `POST /api/marketplace/v3/click-collect/orders/meta/gtin` | Закрепить GTIN за сборочными заданиями | `` |
| Метаданные Самовывоз | `POST /api/marketplace/v3/click-collect/orders/meta/imei` | Закрепить IMEI за сборочными заданиями | `` |
| Метаданные Самовывоз | `POST /api/marketplace/v3/click-collect/orders/meta/info` | Получить метаданные сборочных заданий | `` |
| Метаданные Самовывоз | `POST /api/marketplace/v3/click-collect/orders/meta/sgtin` | Закрепить коды маркировки Честного знака за сборочными заданиями | `` |
| Метаданные Самовывоз | `POST /api/marketplace/v3/click-collect/orders/meta/uin` | Закрепить УИН за сборочными заданиями | `` |
| Метаданные Самовывоз | `PUT /api/v3/click-collect/orders/{orderId}/meta/gtin` | Закрепить за сборочным заданием GTIN | `` |
| Метаданные Самовывоз | `PUT /api/v3/click-collect/orders/{orderId}/meta/imei` | Закрепить за сборочным заданием IMEI | `` |
| Метаданные Самовывоз | `PUT /api/v3/click-collect/orders/{orderId}/meta/sgtin` | Закрепить за сборочным заданием код маркировки товара | `` |
| Метаданные Самовывоз | `PUT /api/v3/click-collect/orders/{orderId}/meta/uin` | Закрепить за сборочным заданием УИН (уникальный идентификационный номер) | `` |
| Сборочные задания Самовывоз | `GET /api/v3/click-collect/orders` | Получить информацию о завершённых сборочных заданиях | `` |
| Сборочные задания Самовывоз | `GET /api/v3/click-collect/orders/new` | Получить список новых сборочных заданий | `` |
| Сборочные задания Самовывоз | `PATCH /api/v3/click-collect/orders/{orderId}/cancel` | Отменить сборочное задание | `` |
| Сборочные задания Самовывоз | `PATCH /api/v3/click-collect/orders/{orderId}/confirm` | Перевести на сборку | `` |
| Сборочные задания Самовывоз | `PATCH /api/v3/click-collect/orders/{orderId}/prepare` | Сообщить, что сборочное задание готово к выдаче | `` |
| Сборочные задания Самовывоз | `PATCH /api/v3/click-collect/orders/{orderId}/receive` | Сообщить, что заказ принят покупателем | `` |
| Сборочные задания Самовывоз | `PATCH /api/v3/click-collect/orders/{orderId}/reject` | Сообщить, что покупатель отказался от заказа | `` |
| Сборочные задания Самовывоз | `POST /api/marketplace/v3/click-collect/orders/status/cancel` | Отменить сборочные задания | `` |
| Сборочные задания Самовывоз | `POST /api/marketplace/v3/click-collect/orders/status/confirm` | Перевести сборочные задания на сборку | `` |
| Сборочные задания Самовывоз | `POST /api/marketplace/v3/click-collect/orders/status/info` | Получить статусы сборочных заданий | `` |
| Сборочные задания Самовывоз | `POST /api/marketplace/v3/click-collect/orders/status/prepare` | Сообщить, что сборочные задания готовы к выдаче | `` |
| Сборочные задания Самовывоз | `POST /api/marketplace/v3/click-collect/orders/status/receive` | Сообщить, что заказы приняты покупателями | `` |
| Сборочные задания Самовывоз | `POST /api/marketplace/v3/click-collect/orders/status/reject` | Сообщить об отказе от заказов | `` |
| Сборочные задания Самовывоз | `POST /api/v3/click-collect/orders/client` | Информация о покупателе | `` |
| Сборочные задания Самовывоз | `POST /api/v3/click-collect/orders/client/identity` | Проверить, что заказ принадлежит покупателю | `` |
| Сборочные задания Самовывоз | `POST /api/v3/click-collect/orders/status` | Получить статусы сборочных заданий | `` |

## Поставки FBW (07-orders-fbw.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Информация для формирования поставок | `GET /api/v1/transit-tariffs` | Транзитные направления | `` |
| Информация для формирования поставок | `GET /api/v1/warehouses` | Список складов | `` |
| Информация для формирования поставок | `POST /api/v1/acceptance/options` | Опции приёмки | `` |
| Информация о поставках | `GET /api/v1/supplies/{ID}` | Детали поставки | `` |
| Информация о поставках | `GET /api/v1/supplies/{ID}/goods` | Товары поставки | `` |
| Информация о поставках | `GET /api/v1/supplies/{ID}/package` | Упаковка поставки | `` |
| Информация о поставках | `POST /api/v1/supplies` | Список поставок | `` |

## Маркетинг и продвижение (08-promotion.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Календарь акций | `GET /api/v1/calendar/promotions` | Список акций | `` |
| Календарь акций | `GET /api/v1/calendar/promotions/details` | Детальная информация об акциях | `` |
| Календарь акций | `GET /api/v1/calendar/promotions/nomenclatures` | Список товаров для участия в акции | `` |
| Календарь акций | `POST /api/v1/calendar/promotions/upload` | Добавить товар в акцию | `` |
| Кампании | `GET /adv/v1/promotion/count` | Списки кампаний | `` |
| Кампании | `GET /api/advert/v2/adverts` | Информация о кампаниях | `` |
| Медиа | `GET /adv/v1/advert` | Информация о медиакампании | `` |
| Медиа | `GET /adv/v1/adverts` | Список медиакампаний | `` |
| Медиа | `GET /adv/v1/count` | Количество медиакампаний | `` |
| Поисковые кластеры | `DELETE /adv/v0/normquery/bids` | Удалить ставки поисковых кластеров | `` |
| Поисковые кластеры | `POST /adv/v0/normquery/bids` | Установить ставки для поисковых кластеров | `` |
| Поисковые кластеры | `POST /adv/v0/normquery/get-bids` | Список ставок поисковых кластеров | `` |
| Поисковые кластеры | `POST /adv/v0/normquery/get-minus` | Список минус-фраз кампаний | `` |
| Поисковые кластеры | `POST /adv/v0/normquery/list` | Списки активных и неактивных поисковых кластеров | `` |
| Поисковые кластеры | `POST /adv/v0/normquery/set-minus` | Установка и удаление минус-фраз | `` |
| Создание кампаний | `GET /adv/v1/supplier/subjects` | Предметы для кампаний | `` |
| Создание кампаний | `POST /adv/v2/seacat/save-ad` | Создать кампанию | `` |
| Создание кампаний | `POST /adv/v2/supplier/nms` | Карточки товаров для кампаний | `` |
| Создание кампаний | `POST /api/advert/v1/bids/min` | Минимальные ставки для карточек товаров | `` |
| Статистика | `GET /adv/v3/fullstats` | Статистика кампаний | `` |
| Статистика | `POST /adv/v0/normquery/stats` | Статистика поисковых кластеров | `` |
| Статистика | `POST /adv/v1/normquery/stats` | Статистика по поисковым кластерам с детализацией по дням | `` |
| Статистика | `POST /adv/v1/stats` | Статистика медиакампаний | `` |
| Управление кампаниями | `GET /adv/v0/delete` | Удаление кампании | `` |
| Управление кампаниями | `GET /adv/v0/pause` | Пауза кампании | `` |
| Управление кампаниями | `GET /adv/v0/start` | Запуск кампании | `` |
| Управление кампаниями | `GET /adv/v0/stop` | Завершение кампании | `` |
| Управление кампаниями | `GET /api/advert/v0/bids/recommendations` | Рекомендуемые ставки для карточек товаров и поисковых кластеров | `` |
| Управление кампаниями | `PATCH /adv/v0/auction/nms` | Изменение списка карточек товаров в кампаниях | `` |
| Управление кампаниями | `PATCH /api/advert/v1/bids` | Изменение ставок в кампаниях | `` |
| Управление кампаниями | `POST /adv/v0/rename` | Переименование кампании | `` |
| Управление кампаниями | `PUT /adv/v0/auction/placements` | Изменение мест размещения в кампаниях с ручной ставкой | `` |
| Финансы | `GET /adv/v1/balance` | Баланс | `` |
| Финансы | `GET /adv/v1/budget` | Бюджет кампании | `` |
| Финансы | `GET /adv/v1/payments` | Получение истории пополнений счёта | `` |
| Финансы | `GET /adv/v1/upd` | Получение истории затрат | `` |
| Финансы | `POST /adv/v1/budget/deposit` | Пополнение бюджета кампании | `` |

## Общение с покупателями (09-communications.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Возвраты покупателями | `GET /api/v1/claims` | Заявки покупателей на возврат | `` |
| Возвраты покупателями | `PATCH /api/v1/claim` | Ответ на заявку покупателя | `` |
| Вопросы | `GET /api/v1/new-feedbacks-questions` | Непросмотренные отзывы и вопросы | `` |
| Вопросы | `GET /api/v1/question` | Получить вопрос по ID | `` |
| Вопросы | `GET /api/v1/questions` | Список вопросов | `` |
| Вопросы | `GET /api/v1/questions/count` | Количество вопросов | `` |
| Вопросы | `GET /api/v1/questions/count-unanswered` | Неотвеченные вопросы | `` |
| Вопросы | `PATCH /api/v1/questions` | Работа с вопросами | `` |
| Закреплённые отзывы | `DELETE /api/feedbacks/v1/pins` | Открепить отзывы | `` |
| Закреплённые отзывы | `GET /api/feedbacks/v1/pins` | Список закреплённых и откреплённых отзывов | `` |
| Закреплённые отзывы | `GET /api/feedbacks/v1/pins/count` | Количество закреплённых и откреплённых отзывов | `` |
| Закреплённые отзывы | `GET /api/feedbacks/v1/pins/limits` | Лимиты закреплённых отзывов | `` |
| Закреплённые отзывы | `POST /api/feedbacks/v1/pins` | Закрепить отзывы | `` |
| Отзывы | `GET /api/v1/feedback` | Получить отзыв по ID | `` |
| Отзывы | `GET /api/v1/feedbacks` | Список отзывов | `` |
| Отзывы | `GET /api/v1/feedbacks/archive` | Список архивных отзывов | `` |
| Отзывы | `GET /api/v1/feedbacks/count` | Количество отзывов | `` |
| Отзывы | `GET /api/v1/feedbacks/count-unanswered` | Необработанные отзывы | `` |
| Отзывы | `PATCH /api/v1/feedbacks/answer` | Отредактировать ответ на отзыв | `` |
| Отзывы | `POST /api/v1/feedbacks/answer` | Ответить на отзыв | `` |
| Отзывы | `POST /api/v1/feedbacks/order/return` | Возврат товара по ID отзыва | `` |
| Чат с покупателями | `GET /api/v1/seller/chats` | Список чатов | `` |
| Чат с покупателями | `GET /api/v1/seller/download/{id}` | Получить файл из сообщения | `` |
| Чат с покупателями | `GET /api/v1/seller/events` | События чатов | `` |
| Чат с покупателями | `POST /api/v1/seller/message` | Отправить сообщение | `` |

## Тарифы (10-tariffs.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Комиссии | `GET /api/v1/tariffs/commission` | Комиссия по категориям товаров | `` |
| Стоимость возврата продавцу | `GET /api/v1/tariffs/return` | Тарифы на возврат | `` |
| Тарифы на остаток | `GET /api/v1/tariffs/box` | Тарифы для коробов | `` |
| Тарифы на остаток | `GET /api/v1/tariffs/pallet` | Тарифы для монопаллет | `` |
| Тарифы на поставку | `GET /api/tariffs/v1/acceptance/coefficients` | Тарифы на поставку | `` |

## Аналитика и данные (11-analytics.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Аналитика продавца CSV | `GET /api/v2/nm-report/downloads` | Получить список отчётов | `` |
| Аналитика продавца CSV | `GET /api/v2/nm-report/downloads/file/{downloadId}` | Получить отчёт | `` |
| Аналитика продавца CSV | `POST /api/v2/nm-report/downloads` | Создать отчёт | `` |
| Аналитика продавца CSV | `POST /api/v2/nm-report/downloads/retry` | Сгенерировать отчёт повторно | `` |
| Воронка продаж | `POST /api/analytics/v3/sales-funnel/grouped/history` | Статистика групп карточек товаров по дням | `postSalesFunnelGroupedHistory` |
| Воронка продаж | `POST /api/analytics/v3/sales-funnel/products` | Статистика карточек товаров за период | `postSalesFunnelProducts` |
| Воронка продаж | `POST /api/analytics/v3/sales-funnel/products/history` | Статистика карточек товаров по дням | `postSalesFunnelProductsHistory` |
| История остатков | `POST /api/analytics/v1/stocks-report/wb-warehouses` | Остатки на складах WB | `postV1StocksReportWbWarehouses` |
| История остатков | `POST /api/v2/stocks-report/offices` | Данные по складам | `` |
| История остатков | `POST /api/v2/stocks-report/products/groups` | Данные по группам | `` |
| История остатков | `POST /api/v2/stocks-report/products/products` | Данные по товарам | `` |
| История остатков | `POST /api/v2/stocks-report/products/sizes` | Данные по размерам | `` |
| Поисковые запросы по вашим товарам | `POST /api/v2/search-report/product/orders` | Заказы и позиции по поисковым запросам товара | `` |
| Поисковые запросы по вашим товарам | `POST /api/v2/search-report/product/search-texts` | Поисковые запросы по товару | `` |
| Поисковые запросы по вашим товарам | `POST /api/v2/search-report/report` | Основная страница | `` |
| Поисковые запросы по вашим товарам | `POST /api/v2/search-report/table/details` | Пагинация по товарам в группе | `` |
| Поисковые запросы по вашим товарам | `POST /api/v2/search-report/table/groups` | Пагинация по группам | `` |

## Отчёты (12-reports.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Доля бренда в продажах | `GET /api/v1/analytics/brand-share` | Получить отчёт | `` |
| Доля бренда в продажах | `GET /api/v1/analytics/brand-share/brands` | Бренды продавца | `` |
| Доля бренда в продажах | `GET /api/v1/analytics/brand-share/parent-subjects` | Родительские категории бренда | `` |
| Операции при приёмке | `GET /api/v1/acceptance_report` | Создать отчёт | `` |
| Операции при приёмке | `GET /api/v1/acceptance_report/tasks/{task_id}/download` | Получить отчёт | `` |
| Операции при приёмке | `GET /api/v1/acceptance_report/tasks/{task_id}/status` | Проверить статус | `` |
| Основные отчёты | `GET /api/v1/supplier/orders` | Заказы | `` |
| Основные отчёты | `GET /api/v1/supplier/sales` | Продажи | `` |
| Основные отчёты | `GET /api/v1/supplier/stocks` | Склады | `` |
| Отчёт о возвратах и перемещении товаров | `GET /api/v1/analytics/goods-return` | Получить отчёт | `` |
| Отчёт о товарах c обязательной маркировкой | `POST /api/v1/analytics/excise-report` | Получить отчёт | `` |
| Отчёт об остатках на складах | `GET /api/v1/warehouse_remains` | Создать отчёт | `` |
| Отчёт об остатках на складах | `GET /api/v1/warehouse_remains/tasks/{task_id}/download` | Получить отчёт | `` |
| Отчёт об остатках на складах | `GET /api/v1/warehouse_remains/tasks/{task_id}/status` | Проверить статус | `` |
| Отчёты об удержаниях | `GET /api/analytics/v1/deductions` | Подмены и неверные вложения | `getDeductions` |
| Отчёты об удержаниях | `GET /api/analytics/v1/measurement-penalties` | Удержания за занижение габаритов упаковки | `getMeasurementPenalties` |
| Отчёты об удержаниях | `GET /api/analytics/v1/warehouse-measurements` | Замеры склада | `getWarehouseMeasurements` |
| Отчёты об удержаниях | `GET /api/v1/analytics/antifraud-details` | Самовыкупы | `` |
| Отчёты об удержаниях | `GET /api/v1/analytics/goods-labeling` | Маркировка товара | `` |
| Платное хранение | `GET /api/v1/paid_storage` | Создать отчёт | `` |
| Платное хранение | `GET /api/v1/paid_storage/tasks/{task_id}/download` | Получить отчёт | `` |
| Платное хранение | `GET /api/v1/paid_storage/tasks/{task_id}/status` | Проверить статус | `` |
| Продажи по регионам | `GET /api/v1/analytics/region-sale` | Получить отчёт | `` |
| Скрытые товары | `GET /api/v1/analytics/banned-products/blocked` | Заблокированные карточки | `` |
| Скрытые товары | `GET /api/v1/analytics/banned-products/shadowed` | Скрытые из каталога | `` |

## Документы и бухгалтерия (13-finances.yaml)


| Tag | Endpoint | Description | Operation ID |
|-----|----------|-------------|--------------|
| Баланс | `GET /api/v1/account/balance` | Получить баланс продавца | `` |
| Документы | `GET /api/v1/documents/categories` | Категории документов | `` |
| Документы | `GET /api/v1/documents/download` | Получить документ | `` |
| Документы | `GET /api/v1/documents/list` | Список документов | `` |
| Документы | `POST /api/v1/documents/download/all` | Получить документы | `` |
| Финансовые отчёты | `GET /api/v5/supplier/reportDetailByPeriod` | Отчёт о продажах по реализации | `` |
| Финансовые отчёты | `POST /api/finance/v1/acquiring/detailed` | Детализации к отчётам об издержках на приём платежей за период | `postV1AcquiringDetailed` |
| Финансовые отчёты | `POST /api/finance/v1/acquiring/detailed/{reportId}` | Детализации к отчётам об издержках на приём платежей по ID отчётов | `postV1AcquiringDetailedReportId` |
| Финансовые отчёты | `POST /api/finance/v1/acquiring/list` | Список отчётов об издержках на приём платежей | `postV1AcquiringList` |
| Финансовые отчёты | `POST /api/finance/v1/sales-reports/detailed` | Детализации к отчётам реализации за период | `postV1SalesReportsDetailed` |
| Финансовые отчёты | `POST /api/finance/v1/sales-reports/detailed/{reportId}` | Детализации к отчётам реализации по ID отчётов | `postV1SalesReportsDetailedReportId` |
| Финансовые отчёты | `POST /api/finance/v1/sales-reports/list` | Список отчётов реализации | `postV1SalesReportsList` |
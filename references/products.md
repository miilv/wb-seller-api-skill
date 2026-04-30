# Products — Cards, Content, Prices, Discounts

_Работа с товарами_

**Source:** [`swagger/02-products.yaml`](../swagger/02-products.yaml)

**49 endpoints** across 8 tag(s).

## Карточки товаров

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/content/v2/get/cards/list` | Список карточек товаров |
| `POST` | `/content/v2/cards/error/list` | Список несозданных карточек товаров с ошибками |
| `POST` | `/content/v2/cards/update` | Редактирование карточек товаров |
| `POST` | `/content/v2/cards/moveNm` | Объединение и разъединение карточек товаров |
| `POST` | `/content/v2/cards/delete/trash` | Перенос карточек товаров в корзину |
| `POST` | `/content/v2/cards/recover` | Восстановление карточек товаров из корзины |
| `POST` | `/content/v2/get/cards/trash` | Список карточек товаров в корзине |

## Категории, предметы и характеристики

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/content/v2/object/parent/all` | Родительские категории товаров |
| `GET` | `/content/v2/object/all` | Список предметов |
| `GET` | `/content/v2/object/charcs/{subjectId}` | Характеристики предмета |
| `GET` | `/content/v2/directory/colors` | Цвет |
| `GET` | `/content/v2/directory/kinds` | Пол |
| `GET` | `/content/v2/directory/countries` | Страна производства |
| `GET` | `/content/v2/directory/seasons` | Сезон |
| `GET` | `/content/v2/directory/vat` | Ставка НДС |
| `GET` | `/content/v2/directory/tnved` | ТНВЭД-код |
| `GET` | `/api/content/v1/brands` | Бренды |

## Медиафайлы

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/content/v3/media/file` | Загрузить медиафайл |
| `POST` | `/content/v3/media/save` | Загрузить медиафайлы по ссылкам |

## Остатки на складах продавца

| Method | Path | Summary |
|--------|------|---------|
| `PUT` | `/api/v3/stocks/{warehouseId}` | Обновить остатки товаров |
| `DELETE` | `/api/v3/stocks/{warehouseId}` | Удалить остатки товаров |
| `POST` | `/api/v3/stocks/{warehouseId}` | Получить остатки товаров |

## Склады продавца

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v3/offices` | Получить список складов WB |
| `GET` | `/api/v3/warehouses` | Получить список складов продавца |
| `POST` | `/api/v3/warehouses` | Создать склад продавца |
| `PUT` | `/api/v3/warehouses/{warehouseId}` | Обновить склад продавца |
| `DELETE` | `/api/v3/warehouses/{warehouseId}` | Удалить склад продавца |
| `GET` | `/api/v3/dbw/warehouses/{warehouseId}/contacts` | Список контактов |
| `PUT` | `/api/v3/dbw/warehouses/{warehouseId}/contacts` | Обновить список контактов |

## Создание карточек товаров

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/content/v2/cards/limits` | Лимиты карточек товаров |
| `POST` | `/content/v2/barcodes` | Генерация баркодов |
| `POST` | `/content/v2/cards/upload` | Создание карточек товаров |
| `POST` | `/content/v2/cards/upload/add` | Создание карточек товаров с присоединением |

## Цены и скидки

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v2/upload/task` | Установить цены и скидки |
| `POST` | `/api/v2/upload/task/size` | Установить цены для размеров |
| `POST` | `/api/v2/upload/task/club-discount` | Установить скидки WB Клуба |
| `GET` | `/api/v2/history/tasks` | Состояние обработанной загрузки |
| `GET` | `/api/v2/history/goods/task` | Детализация обработанной загрузки |
| `GET` | `/api/v2/buffer/tasks` | Состояние необработанной загрузки |
| `GET` | `/api/v2/buffer/goods/task` | Детализация необработанной загрузки |
| `GET` | `/api/v2/list/goods/filter` | Получить товары с ценами |
| `POST` | `/api/v2/list/goods/filter` | Получить товары с ценами по артикулам |
| `GET` | `/api/v2/list/goods/size/nm` | Получить размеры товара с ценами |
| `GET` | `/api/v2/quarantine/goods` | Получить товары в карантине |

## Ярлыки

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/content/v2/tags` | Список ярлыков |
| `POST` | `/content/v2/tag` | Создание ярлыка |
| `PATCH` | `/content/v2/tag/{id}` | Изменение ярлыка |
| `DELETE` | `/content/v2/tag/{id}` | Удаление ярлыка |
| `POST` | `/content/v2/tag/nomenclature/link` | Управление ярлыками в карточке товара |


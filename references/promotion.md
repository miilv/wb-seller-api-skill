# Promotion — Marketing, Ads, Calendar

_Маркетинг и продвижение_

**Source:** [`swagger/08-promotion.yaml`](../swagger/08-promotion.yaml)

**37 endpoints** across 8 tag(s).

## Календарь акций

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/calendar/promotions` | Список акций |
| `GET` | `/api/v1/calendar/promotions/details` | Детальная информация об акциях |
| `GET` | `/api/v1/calendar/promotions/nomenclatures` | Список товаров для участия в акции |
| `POST` | `/api/v1/calendar/promotions/upload` | Добавить товар в акцию |

## Кампании

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/adv/v1/promotion/count` | Списки кампаний |
| `GET` | `/api/advert/v2/adverts` | Информация о кампаниях |

## Медиа

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/adv/v1/count` | Количество медиакампаний |
| `GET` | `/adv/v1/adverts` | Список медиакампаний |
| `GET` | `/adv/v1/advert` | Информация о медиакампании |

## Поисковые кластеры

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/adv/v0/normquery/get-bids` | Список ставок поисковых кластеров |
| `POST` | `/adv/v0/normquery/bids` | Установить ставки для поисковых кластеров |
| `DELETE` | `/adv/v0/normquery/bids` | Удалить ставки поисковых кластеров |
| `POST` | `/adv/v0/normquery/get-minus` | Список минус-фраз кампаний |
| `POST` | `/adv/v0/normquery/set-minus` | Установка и удаление минус-фраз |
| `POST` | `/adv/v0/normquery/list` | Списки активных и неактивных поисковых кластеров |

## Создание кампаний

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/advert/v1/bids/min` | Минимальные ставки для карточек товаров |
| `POST` | `/adv/v2/seacat/save-ad` | Создать кампанию |
| `GET` | `/adv/v1/supplier/subjects` | Предметы для кампаний |
| `POST` | `/adv/v2/supplier/nms` | Карточки товаров для кампаний |

## Статистика

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/adv/v0/normquery/stats` | Статистика поисковых кластеров |
| `GET` | `/adv/v3/fullstats` | Статистика кампаний |
| `POST` | `/adv/v1/stats` | Статистика медиакампаний |
| `POST` | `/adv/v1/normquery/stats` | Статистика по поисковым кластерам с детализацией по дням |

## Управление кампаниями

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/adv/v0/delete` | Удаление кампании |
| `POST` | `/adv/v0/rename` | Переименование кампании |
| `GET` | `/adv/v0/start` | Запуск кампании |
| `GET` | `/adv/v0/pause` | Пауза кампании |
| `GET` | `/adv/v0/stop` | Завершение кампании |
| `PUT` | `/adv/v0/auction/placements` | Изменение мест размещения в кампаниях с ручной ставкой |
| `PATCH` | `/api/advert/v1/bids` | Изменение ставок в кампаниях |
| `PATCH` | `/adv/v0/auction/nms` | Изменение списка карточек товаров в кампаниях |
| `GET` | `/api/advert/v0/bids/recommendations` | Рекомендуемые ставки для карточек товаров и поисковых кластеров |

## Финансы

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/adv/v1/balance` | Баланс |
| `GET` | `/adv/v1/budget` | Бюджет кампании |
| `POST` | `/adv/v1/budget/deposit` | Пополнение бюджета кампании |
| `GET` | `/adv/v1/upd` | Получение истории затрат |
| `GET` | `/adv/v1/payments` | Получение истории пополнений счёта |


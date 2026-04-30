# Analytics — Sales Funnel, Search Queries, Stocks

_Аналитика и данные_

**Source:** [`swagger/11-analytics.yaml`](../swagger/11-analytics.yaml)

**17 endpoints** across 4 tag(s).

## Аналитика продавца CSV

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v2/nm-report/downloads` | Создать отчёт |
| `GET` | `/api/v2/nm-report/downloads` | Получить список отчётов |
| `POST` | `/api/v2/nm-report/downloads/retry` | Сгенерировать отчёт повторно |
| `GET` | `/api/v2/nm-report/downloads/file/{downloadId}` | Получить отчёт |

## Воронка продаж

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/analytics/v3/sales-funnel/products` | Статистика карточек товаров за период |
| `POST` | `/api/analytics/v3/sales-funnel/products/history` | Статистика карточек товаров по дням |
| `POST` | `/api/analytics/v3/sales-funnel/grouped/history` | Статистика групп карточек товаров по дням |

## История остатков

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/analytics/v1/stocks-report/wb-warehouses` | Остатки на складах WB |
| `POST` | `/api/v2/stocks-report/products/groups` | Данные по группам |
| `POST` | `/api/v2/stocks-report/products/products` | Данные по товарам |
| `POST` | `/api/v2/stocks-report/products/sizes` | Данные по размерам |
| `POST` | `/api/v2/stocks-report/offices` | Данные по складам |

## Поисковые запросы по вашим товарам

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v2/search-report/report` | Основная страница |
| `POST` | `/api/v2/search-report/table/groups` | Пагинация по группам |
| `POST` | `/api/v2/search-report/table/details` | Пагинация по товарам в группе |
| `POST` | `/api/v2/search-report/product/search-texts` | Поисковые запросы по товару |
| `POST` | `/api/v2/search-report/product/orders` | Заказы и позиции по поисковым запросам товара |


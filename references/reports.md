# Reports — Statistics, Retention, Warehouses

_Отчёты_

**Source:** [`swagger/12-reports.yaml`](../swagger/12-reports.yaml)

**25 endpoints** across 10 tag(s).

## Доля бренда в продажах

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/analytics/brand-share/brands` | Бренды продавца |
| `GET` | `/api/v1/analytics/brand-share/parent-subjects` | Родительские категории бренда |
| `GET` | `/api/v1/analytics/brand-share` | Получить отчёт |

## Операции при приёмке

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/acceptance_report` | Создать отчёт |
| `GET` | `/api/v1/acceptance_report/tasks/{task_id}/status` | Проверить статус |
| `GET` | `/api/v1/acceptance_report/tasks/{task_id}/download` | Получить отчёт |

## Основные отчёты

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/supplier/stocks` | Склады |
| `GET` | `/api/v1/supplier/orders` | Заказы |
| `GET` | `/api/v1/supplier/sales` | Продажи |

## Отчёт о возвратах и перемещении товаров

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/analytics/goods-return` | Получить отчёт |

## Отчёт о товарах c обязательной маркировкой

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v1/analytics/excise-report` | Получить отчёт |

## Отчёт об остатках на складах

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/warehouse_remains` | Создать отчёт |
| `GET` | `/api/v1/warehouse_remains/tasks/{task_id}/status` | Проверить статус |
| `GET` | `/api/v1/warehouse_remains/tasks/{task_id}/download` | Получить отчёт |

## Отчёты об удержаниях

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/analytics/v1/measurement-penalties` | Удержания за занижение габаритов упаковки |
| `GET` | `/api/analytics/v1/warehouse-measurements` | Замеры склада |
| `GET` | `/api/analytics/v1/deductions` | Подмены и неверные вложения |
| `GET` | `/api/v1/analytics/antifraud-details` | Самовыкупы |
| `GET` | `/api/v1/analytics/goods-labeling` | Маркировка товара |

## Платное хранение

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/paid_storage` | Создать отчёт |
| `GET` | `/api/v1/paid_storage/tasks/{task_id}/status` | Проверить статус |
| `GET` | `/api/v1/paid_storage/tasks/{task_id}/download` | Получить отчёт |

## Продажи по регионам

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/analytics/region-sale` | Получить отчёт |

## Скрытые товары

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/analytics/banned-products/blocked` | Заблокированные карточки |
| `GET` | `/api/v1/analytics/banned-products/shadowed` | Скрытые из каталога |


# Finances — Reports, Documents, Accounting

_Документы и бухгалтерия_

**Source:** [`swagger/13-finances.yaml`](../swagger/13-finances.yaml)

**12 endpoints** across 3 tag(s).

## Баланс

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/account/balance` | Получить баланс продавца |

## Документы

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/documents/categories` | Категории документов |
| `GET` | `/api/v1/documents/list` | Список документов |
| `GET` | `/api/v1/documents/download` | Получить документ |
| `POST` | `/api/v1/documents/download/all` | Получить документы |

## Финансовые отчёты

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/finance/v1/sales-reports/list` | Список отчётов реализации |
| `POST` | `/api/finance/v1/sales-reports/detailed/{reportId}` | Детализации к отчётам реализации по ID отчётов |
| `POST` | `/api/finance/v1/sales-reports/detailed` | Детализации к отчётам реализации за период |
| `GET` | `/api/v5/supplier/reportDetailByPeriod` | Отчёт о продажах по реализации |
| `POST` | `/api/finance/v1/acquiring/list` | Список отчётов об издержках на приём платежей |
| `POST` | `/api/finance/v1/acquiring/detailed/{reportId}` | Детализации к отчётам об издержках на приём платежей по ID отчётов |
| `POST` | `/api/finance/v1/acquiring/detailed` | Детализации к отчётам об издержках на приём платежей за период |


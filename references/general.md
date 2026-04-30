# General — News, Seller Info, Common

_Общее_

**Source:** [`swagger/01-general.yaml`](../swagger/01-general.yaml)

**9 endpoints** across 4 tag(s).

## API новостей

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/communications/v2/news` | Получение новостей портала продавцов |

## Информация о продавце

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/seller-info` | Получить информацию о продавце |
| `GET` | `/api/common/v1/rating` | Получить рейтинг продавца |
| `GET` | `/api/common/v1/subscriptions` | Получить информацию о подписке Джем |

## Проверка подключения к WB API

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/ping` | Проверка подключения |

## Управление пользователями продавца

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/api/v1/invite` | Создать приглашение для нового пользователя |
| `GET` | `/api/v1/users` | Получить список активных или приглашённых пользователей продавца |
| `PUT` | `/api/v1/users/access` | Изменить права доступа пользователей |
| `DELETE` | `/api/v1/user` | Удалить пользователя |


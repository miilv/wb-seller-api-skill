# Communications — Feedbacks, Questions, Buyer Chat

_Общение с покупателями_

**Source:** [`swagger/09-communications.yaml`](../swagger/09-communications.yaml)

**25 endpoints** across 5 tag(s).

## Возвраты покупателями

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/claims` | Заявки покупателей на возврат |
| `PATCH` | `/api/v1/claim` | Ответ на заявку покупателя |

## Вопросы

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/new-feedbacks-questions` | Непросмотренные отзывы и вопросы |
| `GET` | `/api/v1/questions/count-unanswered` | Неотвеченные вопросы |
| `GET` | `/api/v1/questions/count` | Количество вопросов |
| `GET` | `/api/v1/questions` | Список вопросов |
| `PATCH` | `/api/v1/questions` | Работа с вопросами |
| `GET` | `/api/v1/question` | Получить вопрос по ID |

## Закреплённые отзывы

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/feedbacks/v1/pins` | Список закреплённых и откреплённых отзывов |
| `POST` | `/api/feedbacks/v1/pins` | Закрепить отзывы |
| `DELETE` | `/api/feedbacks/v1/pins` | Открепить отзывы |
| `GET` | `/api/feedbacks/v1/pins/count` | Количество закреплённых и откреплённых отзывов |
| `GET` | `/api/feedbacks/v1/pins/limits` | Лимиты закреплённых отзывов |

## Отзывы

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/feedbacks/count-unanswered` | Необработанные отзывы |
| `GET` | `/api/v1/feedbacks/count` | Количество отзывов |
| `GET` | `/api/v1/feedbacks` | Список отзывов |
| `POST` | `/api/v1/feedbacks/answer` | Ответить на отзыв |
| `PATCH` | `/api/v1/feedbacks/answer` | Отредактировать ответ на отзыв |
| `POST` | `/api/v1/feedbacks/order/return` | Возврат товара по ID отзыва |
| `GET` | `/api/v1/feedback` | Получить отзыв по ID |
| `GET` | `/api/v1/feedbacks/archive` | Список архивных отзывов |

## Чат с покупателями

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/api/v1/seller/chats` | Список чатов |
| `GET` | `/api/v1/seller/events` | События чатов |
| `POST` | `/api/v1/seller/message` | Отправить сообщение |
| `GET` | `/api/v1/seller/download/{id}` | Получить файл из сообщения |


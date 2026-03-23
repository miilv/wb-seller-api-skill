# Communication APIs (Feedbacks, Questions, Chat, Returns)

## Questions

Base URL: `https://feedbacks-api.wildberries.ru`
Token category: **Feedbacks and Questions**
Rate limit: 3 req/s, 333ms interval, burst 6

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/new-feedbacks-questions` | Info about unseen feedbacks and questions |
| GET | `/api/v1/questions/count-unanswered` | Count of unanswered questions (today and total) |
| GET | `/api/v1/questions/count` | Question count for a period |
| GET | `/api/v1/questions` | Paginated/sorted question list (max 10,000) |
| PATCH | `/api/v1/questions` | View, reject, or answer/edit a question |
| GET | `/api/v1/question` | Single question by ID |

## Feedbacks

Base URL: `https://feedbacks-api.wildberries.ru`
Rate limit: 3 req/s, 333ms interval, burst 6

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/feedbacks/count-unanswered` | Count of unanswered feedbacks (today and total) |
| GET | `/api/v1/feedbacks/count` | Feedback count for a period |
| GET | `/api/v1/feedbacks` | Paginated/sorted feedback list (max 5,000 per page) |
| POST | `/api/v1/feedbacks/answer` | Send reply to feedback |
| PATCH | `/api/v1/feedbacks/answer` | Edit reply (once within 60 days) |
| POST | `/api/v1/feedbacks/order/return` | Request product return for a feedback |
| GET | `/api/v1/feedback` | Single feedback by ID |
| GET | `/api/v1/feedbacks/archive` | Archived feedbacks |

## Pinned Feedback

Base URL: `https://feedbacks-api.wildberries.ru`
Rate limit: 3 req/s, 333ms interval, burst 6

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/feedbacks/v1/pins` | List pinned and unpinned feedback |
| POST | `/api/feedbacks/v1/pins` | Pin feedback to a card or merged group |
| DELETE | `/api/feedbacks/v1/pins` | Unpin feedback by pin IDs |
| GET | `/api/feedbacks/v1/pins/count` | Count of pinned/unpinned feedback for a period |
| GET | `/api/feedbacks/v1/pins/limits` | Pinned feedback limits for tariff/subscription |

## Buyers Chat

Base URL: `https://buyer-chat-api.wildberries.ru`
Token category: **Buyers Chat**
Rate limit: 10 req/10s, 1s interval, burst 10

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/seller/chats` | List all buyer chats |
| GET | `/api/v1/seller/events` | Message events for all chats (paginated) |
| POST | `/api/v1/seller/message` | Send message (text/files) to buyer |
| GET | `/api/v1/seller/download/{id}` | Download file/image from chat |

## Buyers Returns

Base URL: `https://returns-api.wildberries.ru`
Token category: **Buyers Returns**
Rate limit: 20 req/min, 3s interval, burst 10

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/claims` | Return applications for current 14 days |
| PATCH | `/api/v1/claim` | Answer (approve/reject) a return application |

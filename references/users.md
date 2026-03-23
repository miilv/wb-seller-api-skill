# User Management API

Base URL: `https://user-management-api.wildberries.ru`
Token category: **Users** (Personal access token only)
Rate limit: 1 req/s, burst 5 (except Delete: burst 10)

Only available to sellers from the Russian Federation. Requires token from active owner of seller account.

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/invite` | Create invitation for a new user with access settings |
| GET | `/api/v1/users` | List active or invited users (`isInviteOnly` param) |
| PUT | `/api/v1/users/access` | Update user access permissions |
| DELETE | `/api/v1/user` | Revoke user's access (query param: `deletedUserID`) |

## Common API (News, Seller Info)

Base URL: `https://common-api.wildberries.ru`
Token category: **any**
Rate limit: 1 req/min, burst 10

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/communications/v2/news` | Seller portal news (up to 100 items, `from` or `fromID` required) |
| GET | `/api/v1/seller-info` | Seller name and account ID |

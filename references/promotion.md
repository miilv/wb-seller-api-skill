# Promotion API

## Ad Campaigns

Base URL: `https://advert-api.wildberries.ru`
Token category: **Promotion**

### Campaign Info

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/adv/v1/promotion/count` | Campaign lists grouped by type and status | 5 req/s, 200ms interval |
| GET | `/api/advert/v2/adverts` | Campaign info by statuses, payment types, IDs (max 50) | 5 req/s |

### Campaign Creation

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| POST | `/api/advert/v1/bids/min` | Minimum bids for cards in kopecks | 20 req/min, 3s interval |
| POST | `/adv/v2/seacat/save-ad` | Create campaign (custom/standard bid, search/recommendations) | 5 req/min, 12s interval |
| GET | `/adv/v1/supplier/subjects` | Subjects with cards available for campaigns | 1 req/12s |
| POST | `/adv/v2/supplier/nms` | Cards available for campaigns by subject IDs | 5 req/min |

### Campaign Management

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/adv/v0/delete` | Delete campaign (status 4 only) | 5 req/s |
| POST | `/adv/v0/rename` | Rename campaign (max 100 chars) | 5 req/s |
| GET | `/adv/v0/start` | Launch campaign (status 4 or 11) | 5 req/s |
| GET | `/adv/v0/pause` | Pause active campaign (status 9) | 5 req/s |
| GET | `/adv/v0/stop` | Stop/end campaign (status 4, 9, or 11) | 5 req/s |
| PUT | `/adv/v0/auction/placements` | Change placements (custom bid, CPM only) | 1 req/s |
| PATCH | `/api/advert/v1/bids` | Change bids for cards in campaigns | 5 req/s |
| PATCH | `/adv/v0/auction/nms` | Add/remove cards in campaigns (statuses 4, 9, 11) | 1 req/s |

### Search Clusters

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| POST | `/adv/v0/normquery/get-bids` | Search clusters with bids by campaign IDs | 5 req/s, burst 10 |
| POST | `/adv/v0/normquery/bids` | Set bids for search clusters (custom bid, CPM) | 2 req/s, 500ms interval |
| DELETE | `/adv/v0/normquery/bids` | Delete bids from search clusters | 5 req/s, burst 10 |
| POST | `/adv/v0/normquery/get-minus` | Minus phrases by campaign IDs | 5 req/s, burst 10 |
| POST | `/adv/v0/normquery/set-minus` | Set/delete minus phrases (custom bid, CPM) | 5 req/s, burst 10 |

### Finances

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/adv/v1/balance` | Seller's net balance and bonuses | 1 req/s |
| GET | `/adv/v1/budget` | Budget for a specific campaign | 4 req/s |
| POST | `/adv/v1/budget/deposit` | Top up campaign budget | 1 req/s |
| GET | `/adv/v1/upd` | Costs history (max 31 days) | 1 req/s |
| GET | `/adv/v1/payments` | Account top-up history (max 31 days) | 1 req/s |

### Statistics

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| POST | `/adv/v0/normquery/stats` | Search cluster stats for a period (CPM only) | 10 req/min, 6s interval |
| GET | `/adv/v3/fullstats` | Full campaign stats (max 31 days, max 50 IDs) | 3 req/min, 20s interval |

## Media Campaigns

Base URL: `https://advert-media-api.wildberries.ru`
Rate limit: 10 req/s, 100ms interval, burst 10

| Method | Path | Description |
|--------|------|-------------|
| GET | `/adv/v1/count` | Number of media campaigns |
| GET | `/adv/v1/adverts` | List media campaigns with filtering |
| GET | `/adv/v1/advert` | Single media campaign details |
| POST | `/adv/v1/stats` | Media campaign statistics |

## Promotions Calendar

Base URL: `https://dp-calendar-api.wildberries.ru`
Token category: **Prices and Discounts**
Rate limit: 10 req/6s, 600ms interval, burst 5

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/calendar/promotions` | Promotions list with dates |
| GET | `/api/v1/calendar/promotions/details` | Promotion details (max 100 IDs) |
| GET | `/api/v1/calendar/promotions/nomenclatures` | Products eligible for a promotion |
| POST | `/api/v1/calendar/promotions/upload` | Upload products to a promotion |

**Note:** Data sync from DB every 3 min; status changes every 1 min; bid changes every 30s.

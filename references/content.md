# Content API

Base URL: `https://content-api.wildberries.ru`
Sandbox: `https://content-api-sandbox.wildberries.ru`
Token category: **Content**

## Categories, Subjects and Characteristics

Default rate limit: 100 req/min, 600ms interval, burst 5

| Method | Path | Description |
|--------|------|-------------|
| GET | `/content/v2/object/parent/all` | List all parent categories |
| GET | `/content/v2/object/all` | List all subjects with parent categories and IDs |
| GET | `/content/v2/object/charcs/{subjectId}` | List subject characteristics by ID |
| GET | `/content/v2/directory/colors` | Color characteristic values |
| GET | `/content/v2/directory/kinds` | Gender characteristic values |
| GET | `/content/v2/directory/countries` | Country of origin values |
| GET | `/content/v2/directory/seasons` | Season values |
| GET | `/content/v2/directory/vat` | VAT rate values |
| GET | `/content/v2/directory/tnved` | HS-codes (TNVED) by category name |
| GET | `/api/content/v1/brands` | List brands by subject ID. Rate: 1 req/s, burst 5 |

## Creating Product Cards

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| GET | `/content/v2/cards/limits` | Free and paid vendor limits for card creation | 100 req/min |
| POST | `/content/v2/barcodes` | Generate unique SKUs/barcodes for card sizes | 100 req/min |
| POST | `/content/v2/cards/upload` | Create product cards (max 100 per request) | 10 req/min, 6s interval |
| POST | `/content/v2/cards/upload/add` | Create cards by merging with existing (max 29) | 10 req/min, 6s interval |

## Product Cards

| Method | Path | Description | Rate Limit |
|--------|------|-------------|------------|
| POST | `/content/v2/get/cards/list` | List product cards (paginated) | 100 req/min |
| POST | `/content/v2/cards/error/list` | List failed cards (drafts) with errors | 10 req/min |
| POST | `/content/v2/cards/update` | Edit cards and add sizes (max 3000 nmIDs) | 10 req/min |
| POST | `/content/v2/cards/moveNm` | Merge or separate cards by imtID (max 30) | 100 req/min |
| POST | `/content/v2/cards/delete/trash` | Move card to trash (auto-deleted in 30 days) | 100 req/min |
| POST | `/content/v2/cards/recover` | Recover card from trash | 100 req/min |
| POST | `/content/v2/get/cards/trash` | List cards in trash | 100 req/min |

## Media Files

| Method | Path | Description |
|--------|------|-------------|
| POST | `/content/v3/media/file` | Upload one media file (image/video) to a card |
| POST | `/content/v3/media/save` | Upload media via external links |

Rate limit: 100 req/min, 600ms interval, burst 5

## Tags

| Method | Path | Description |
|--------|------|-------------|
| GET | `/content/v2/tags` | List seller's tags |
| POST | `/content/v2/tag` | Create tag (max 15 tags, 15 chars each) |
| PATCH | `/content/v2/tag/{id}` | Update tag name and color |
| DELETE | `/content/v2/tag/{id}` | Delete tag |
| POST | `/content/v2/tag/nomenclature/link` | Add/remove tags on a card (max 15 per card) |

Rate limit: 100 req/min, 600ms interval, burst 5

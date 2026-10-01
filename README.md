# Cloud E-Commerce Platform

Cloud-Based E-Commerce Application Deployment Platform.

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: MySQL/PostgreSQL
- Cloud: AWS
- Version Control: GitHub
## Database Schema

### Users

| Field | Type |
|---|---|
| id | Integer |
| name | String |
| email | String |
| password | String |
| role | String |
| created_at | DateTime |

### Products

| Field | Type |
|---|---|
| id | Integer |
| name | String |
| description | Text |
| price | Decimal |
| quantity | Integer |
| image | String |
| created_at | DateTime |

### Orders

| Field | Type |
|---|---|
| id | Integer |
| user_id | Integer |
| total_amount | Decimal |
| status | String |
| created_at | DateTime |
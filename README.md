\# 💰 Finance System Backend



A production-ready REST API backend for personal finance tracking, built with \*\*FastAPI\*\* and \*\*Python\*\*. Features role-based access control, JWT-style authentication, transaction management, and financial analytics.



\---



\## 🚀 Tech Stack



| Technology | Purpose |

|---|---|

| FastAPI | Web framework |

| SQLAlchemy | ORM \& database layer |

| SQLite | Database |

| Pydantic | Data validation |

| Uvicorn | ASGI server |

| Python 3.12 | Core language |



\---



\## 📁 Project Structure

finance\_system/

├── app/

│   ├── main.py                    # FastAPI app entry point

│   ├── database.py                # Database engine \& session

│   ├── models/

│   │   ├── user.py                # User model with roles

│   │   └── transaction.py        # Transaction model

│   ├── schemas/

│   │   ├── user.py                # User Pydantic schemas

│   │   ├── transaction.py        # Transaction schemas

│   │   └── analytics.py          # Analytics schemas

│   ├── services/

│   │   ├── user\_service.py        # User business logic

│   │   ├── transaction\_service.py # Transaction logic

│   │   └── analytics\_service.py  # Analytics logic

│   ├── routers/

│   │   ├── users.py               # User endpoints

│   │   ├── transactions.py        # Transaction endpoints

│   │   └── analytics.py          # Analytics endpoints

│   ├── middleware/

│   │   └── auth.py                # Auth middleware \& RBAC

│   └── utils/

│       └── auth.py                # Password hashing \& tokens

├── screenshots/                   # API testing screenshots

├── requirements.txt

└── README.md

\---



\## 🔐 Role-Based Access Control (RBAC)



Three user roles with different permission levels:



| Endpoint | Viewer | Analyst | Admin |

|---|---|---|---|

| View own profile | ✅ | ✅ | ✅ |

| View own transactions | ✅ | ✅ | ✅ |

| Create/Update transactions | ❌ | ✅ | ✅ |

| Delete transactions | ❌ | ❌ | ✅ |

| View analytics | ❌ | ✅ | ✅ |

| Manage users | ❌ | ❌ | ✅ |



\---



\## 📡 API Endpoints



\### Users

| Method | Endpoint | Description | Auth |

|---|---|---|---|

| POST | `/api/users/register` | Register new user | No |

| POST | `/api/users/login` | Login \& get token | No |

| GET | `/api/users/me` | Get current user | Yes |

| GET | `/api/users/` | List all users | Admin |

| GET | `/api/users/{user\_id}` | Get user by ID | Admin |

| PUT | `/api/users/{user\_id}` | Update user | Admin |

| DELETE | `/api/users/{user\_id}` | Delete user | Admin |



\### Transactions

| Method | Endpoint | Description | Auth |

|---|---|---|---|

| POST | `/api/transactions/` | Create transaction | Analyst/Admin |

| GET | `/api/transactions/` | List transactions | Yes |

| GET | `/api/transactions/{tx\_id}` | Get transaction | Yes |

| PUT | `/api/transactions/{tx\_id}` | Update transaction | Analyst/Admin |

| DELETE | `/api/transactions/{tx\_id}` | Delete transaction | Admin |



\### Analytics

| Method | Endpoint | Description | Auth |

|---|---|---|---|

| GET | `/api/analytics/summary` | Income/expense summary | Analyst/Admin |

| GET | `/api/analytics/category-breakdown` | Spending by category | Analyst/Admin |

| GET | `/api/analytics/monthly` | Monthly totals | Analyst/Admin |



\---



\## ⚙️ Setup \& Installation



\### Prerequisites

\- Python 3.10+

\- pip



\### Steps

```bash

\# 1. Clone the repository

git clone https://github.com/Abhishek0905Sharma/finance-system-backend.git

cd finance-system-backend



\# 2. Install dependencies

pip install fastapi uvicorn sqlalchemy pydantic\[email]



\# 3. Run the server

uvicorn app.main:app --reload



\# 4. Open API docs

\# Visit: http://127.0.0.1:8000/docs

```



\---



\## 🧪 API Testing (Swagger UI)



The API comes with built-in interactive documentation powered by Swagger UI.



\### Quick Test Flow:

1\. Open `http://127.0.0.1:8000/docs`

2\. Register a user via `POST /api/users/register`

3\. Login via `POST /api/users/login` — copy the token

4\. Click \*\*Authorize\*\* → paste token

5\. Create transactions and view analytics



\---



\## 📸 Screenshots



\### User Registration

!\[Register](screenshots/POST%20api-users-register.png)



\### User Login

!\[Login](screenshots/POST%20api-users-login.png)



\### Create Transaction

!\[Transaction](screenshots/POST%20api-transactions.png)



\### Analytics Summary

!\[Summary](screenshots/GET%20api-analytics-summary.png)



\### Monthly Totals

!\[Monthly](screenshots/GET%20-api-analytics-monthly.png)



\---



\## ✨ Key Features



\- ✅ \*\*JWT-style Authentication\*\* — HMAC-signed tokens, no external library

\- ✅ \*\*Role-Based Access Control\*\* — viewer, analyst, admin roles

\- ✅ \*\*Transaction Management\*\* — full CRUD with filtering \& pagination

\- ✅ \*\*Financial Analytics\*\* — summary, category breakdown, monthly reports

\- ✅ \*\*Data Validation\*\* — Pydantic schemas with custom validators

\- ✅ \*\*Clean Architecture\*\* — separated routers, services, models, schemas

\- ✅ \*\*Auto API Docs\*\* — Swagger UI at `/docs`



\---



\## 👨‍💻 Author



\*\*Abhishek Sharma\*\*  

Python Developer Intern Assignment  

Built with FastAPI \& SQLAlchemy


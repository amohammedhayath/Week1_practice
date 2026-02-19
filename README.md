```md
# Mini Backend App (FastAPI + PostgreSQL + JWT Auth)

This is a mini backend application built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic** with **JWT Authentication**.

---

## Features

### Public Endpoints
- `GET /health` → Health check
- `GET /users` → Get all users
- `GET /products` → Get all products
- `POST /login` → Login and get JWT token

### Protected Endpoint
- `GET /profile` → Get current logged-in user profile (JWT required)

---

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Alembic (Migrations)
- JWT Authentication (python-jose)
- Password Hashing (bcrypt + passlib)

---

## Folder Structure

```

app/
core/
security.py          # password hashing + verification
jwt_handler.py       # JWT token create + verify
deps.py              # get_current_user dependency
db/
database.py          # engine + session + Base
deps.py              # get_db dependency
models/
user.py              # User model
product.py           # Product model
routes/
health.py            # /health
users.py             # /users
products.py          # /products
auth.py              # /login + /profile
schemas/
user_schema.py
product_schema.py
auth_schema.py
main.py                # FastAPI entry point

alembic/
versions/              # migration scripts
alembic.ini              # alembic configuration
.env                     # environment variables (ignored in git)

````

---

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
````

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available, install manually:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic python-dotenv python-jose passlib bcrypt
```

---

## Database Setup (PostgreSQL)

### Create Database

```sql
CREATE DATABASE mini_app_db;
```

### Create User

```sql
CREATE USER mini_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE mini_app_db TO mini_user;
```

### Fix Schema Permission

```sql
GRANT ALL ON SCHEMA public TO mini_user;
ALTER SCHEMA public OWNER TO mini_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mini_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mini_user;
```

---

## Environment Variables

Create `.env` file in project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mini_app_db
DB_USER=mini_user
DB_PASSWORD=yourpassword

SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

⚠️ `.env` must not be pushed to GitHub.

---

## Alembic Migrations

### Generate Migration

```bash
alembic revision --autogenerate -m "create users and products"
```

### Apply Migration

```bash
alembic upgrade head
```

---

## Run Application

Start server:

```bash
uvicorn app.main:app --reload
```

App runs at:

* `http://127.0.0.1:8000`
* Swagger Docs: `http://127.0.0.1:8000/docs`

---

## API Testing

### 1. Health Check

`GET /health`

Response:

```json
{
  "status": "ok"
}
```

---

### 2. Login

`POST /login`

Request:

```json
{
  "email": "test@gmail.com",
  "password": "test123"
}
```

Response:

```json
{
  "access_token": "xxxxx.yyyyy.zzzzz",
  "token_type": "bearer"
}
```

---

### 3. Profile (Protected)

`GET /profile`

Header:

```
Authorization: Bearer <token>
```

Response:

```json
{
  "id": 1,
  "name": "Test User",
  "email": "test@gmail.com"
}
```

---

## Sample Data Scripts

### Create User

Run:

```bash
python create_user.py
```

### Create Product

Run:

```bash
python create_product.py
```

---

## Interview Questions

### What is a REST API?

A REST API is an architectural style where server resources are exposed using HTTP endpoints and standard methods:

* GET → Fetch data
* POST → Create data
* PUT/PATCH → Update data
* DELETE → Remove data

REST APIs are stateless and usually exchange data using JSON.

---

### How does authentication work in an API?

Authentication verifies the identity of a user.

JWT authentication flow:

1. User sends credentials to `/login`
2. Server verifies credentials
3. Server generates a JWT token
4. Client stores the token
5. Client sends token in every request inside:
   `Authorization: Bearer <token>`
6. Server verifies token and allows access to protected routes.

---

## Git Ignore (.env)

Add `.env` to `.gitignore`:

```
.env
venv/
__pycache__/
*.pyc
```

If `.env` was already committed:

```bash
git rm --cached .env
```

---

## Status

All required endpoints are working and tested:

* `/health`
* `/users`
* `/products`
* `/login`
* `/profile` (protected)

---

```
```

# Py Multi-Tenant SAAS Prototype

Production-ready FastAPI + MongoDB + JWT authentication starter  
Built to evolve into a real multi-tenant SaaS (2025 edition).

## Current features
- FastAPI with async everything
- Real MongoDB persistence (Motor)
- Secure JWT auth (access + refresh tokens)
- Argon2 password hashing (no bcrypt native issues)
- Clean layered architecture (routers → models → db → core)
- Automatic OpenAPI docs + Swagger UI
- Ready for multi-tenancy, Docker, tests, CI/CD

## Tech stack
- Python 3.12+
- FastAPI
- Motor (async MongoDB)
- Pydantic v2
- Argon2 via passlib
- JWT with python-jose

## Quick start (works everywhere)

```bash
# 1. Clone & enter
git clone <your-repo>
cd py-multi-tenant-SAAS-proto

# 2. Create virtual env
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies (one command = zero pain)
pip install -r requirements.txt

# 4. Make sure MongoDB is running
sudo systemctl start mongod
sudo systemctl enable mongod   # optional: start on boot

# 5. Run the API
uvicorn main:app --reload

# Multi-Tenancy – How to activate and use a tenant

### 1. Create your first tenant
```bash
curl -X POST http://127.0.0.1:8000/tenants \
  -H "Content-Type: application/json" \
  -d '{"name": "Acme Corp", "subdomain": "acme"}'```

## Multi-Tenancy – How to activate and use a tenant

Access as that tenant (3 easy ways)

```bash
curl -H "host: acme.localhost:8000" http://127.0.0.1:8000/users/me \
  -H "Authorization: Bearer <your-jwt>"

## Payload Example:

curl -X POST http://127.0.0.1:8000/auth/register \
  -H "host: acme.localhost:8000" \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@acme.com","password":"secret123"}'

## Environment configuration

Create a .env file with the following custom values:

# .env
ENV=<your-value>

# MongoDB
MONGODB_URL=<your-value>
DATABASE_NAME=<your-value>

# JWT
SECRET_KEY=<your-value>
ACCESS_TOKEN_EXPIRE_MINUTES=<your-value>
REFRESH_TOKEN_EXPIRE_DAYS=<your-value>

# App
APP_HOST=<your-value>
APP_PORT=<your-value>
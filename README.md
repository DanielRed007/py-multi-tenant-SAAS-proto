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
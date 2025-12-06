# Py Multi-Tenant SAAS Prototype

FastAPI + Pydantic + (future) MongoDB + JWT + Multi-tenancy  
A clean, production-ready starter template built to grow into a real SAAS.

## Features (so far)
- Clean architecture (routers / models / db layer)
- Proper Pydantic request/response models
- Fake in-memory DB (hot-swap ready for MongoDB with zero router changes)
- Automatic interactive OpenAPI docs (Swagger UI + ReDoc)
- Ready for JWT auth, tenancy, background tasks, WebSockets, etc.

## Project structure

py-multi-tenant-SAAS-proto/
├── main.py                # FastAPI app entrypoint
├── routers/               # All API routers
│   └── users.py
├── models/                # Pydantic models
│   ├── init.py        # public API
│   └── user.py
├── db.py                  # Database layer (fake now → MongoDB later)
├── requirements.txt
└── README.md


## Quick start

### 1. Clone & enter the project
```bash
git clone <your-repo>
cd py-multi-tenant-SAAS-proto 
```

### 2. Create virtual environment (recommended)

python -m venv venv
source venv/bin/activate        # Linux/Mac
# or
venv\Scripts\activate           # Windows

### 3. Run the server

uvicorn main:app --reload

Server will be available at: http://127.0.0.1:8000


### 4. Open the interactive API documentationSwagger UI (best for testing):
http://127.0.0.1:8000/docs
ReDoc (beautiful static docs):
http://127.0.0.1:8000/redoc




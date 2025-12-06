# main.py
from fastapi import FastAPI
from routers import users  # Import your router

app = FastAPI(title="My Simple API")

# Include the users router
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Welcome! Visit /docs for API documentation"}
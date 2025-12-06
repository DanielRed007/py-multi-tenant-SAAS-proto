# routers/users.py
from fastapi import APIRouter
from models import User, UserCreate

# Create a router (like Express Router)
router = APIRouter(
    prefix="/users",  # All routes start with /users
    tags=["Users"]     # Groups in API docs
)

# Fake database (we'll replace this later)
fake_users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@router.get("/")
def get_all_users():
    """Get all users"""
    return fake_users_db

@router.get("/{user_id}")
def get_user(user_id: int):
    """Get one user by ID"""
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

@router.post("/")
def create_user(user: UserCreate):
    """Create a new user"""
    new_user = {
        "id": len(fake_users_db) + 1,
        "name": user.name,
        "email": user.email
    }
    fake_users_db.append(new_user)
    return new_user
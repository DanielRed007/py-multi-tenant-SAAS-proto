# routers/users.py
from fastapi import APIRouter, HTTPException, status
from models import UserCreate, User  # We'll make User a response model soon
from db import get_all, get_by_id, create  # ← clean separation!

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[User])
def get_all_users():
    return get_all()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    new_user = create({
        "name": user.name,
        "email": user.email
    })
    return new_user
# routers/users.py
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from models import UserCreate, User, UserInDB
from db import get_all, get_by_id, create_user, update, delete
from core.security import get_current_user
from core.tenant import get_current_tenant

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[User])
async def get_all_users():
    return await get_all()

@router.get("/me", response_model=User)
async def read_users_me(
    current_user: User = Depends(get_current_user),
    tenant: dict = Depends(get_current_tenant)
):
    if current_user.get("tenant_id") != tenant["id"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return current_user


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    new_user = await create_user({
        "name": user.name,
        "email": user.email
    })
    return new_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update):
    update_data = {k: v for k, v in user_update.dict(exclude_unset=True).items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    updated = await update(user_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    if not await delete(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return None
# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models import UserCreate, User, Token
from db import create_user, get_by_email
from jose import jwt, JWTError
from core.security import verify_password, create_access_token, create_refresh_token

router = APIRouter(prefix="/auth", tags=["Auth"])
SECRET_KEY = "change-me-to-a-random-256-bit-string-in-prod-please"

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    print(user, "My User")
    new_user = await create_user(user)   # ← pass the whole Pydantic model, not dict
    
    access_token = create_access_token(data={"sub": str(new_user["id"])})
    refresh_token = create_refresh_token(data={"sub": str(new_user["id"])})
    return Token(access_token=access_token, refresh_token=refresh_token)

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_by_email(form_data.username)  # using username as email
    if not user or not verify_password(form_data.password, user.get("hashed_password", "")):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    access_token = create_access_token(data={"sub": str(user["id"])})
    refresh_token = create_refresh_token(data={"sub": str(user["id"])})
    return Token(access_token=access_token, refresh_token=refresh_token)

@router.post("/refresh", response_model=Token)
async def refresh_token(refresh_token: str):
    
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    access_token = create_access_token(data={"sub": user_id})
    new_refresh = create_refresh_token(data={"sub": user_id})
    return Token(access_token=access_token, refresh_token=new_refresh)
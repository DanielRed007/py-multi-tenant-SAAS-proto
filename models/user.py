# models.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class User(UserCreate):        # Inherits name + email
    id: int                    # Adds the id that comes from DB

    class Config:
        from_attributes = True  # Important for future ORM mode
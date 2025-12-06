# models.py
from pydantic import BaseModel

class User(BaseModel):
    """User data structure"""
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    """Data needed to create a user"""
    name: str
    email: str
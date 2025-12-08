# models/tenant.py
from pydantic import BaseModel
from typing import Optional

class TenantBase(BaseModel):
    name: str
    subdomain: str                     # e.g. "acme" → acme.yourapp.com

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int

    class Config:
        from_attributes = True
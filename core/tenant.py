# core/tenant.py
from fastapi import Request, HTTPException, Depends
import motor.motor_asyncio
from core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
db = client[settings.DATABASE_NAME]

tenants_collection = db.tenants

async def get_current_tenant(request: Request) -> dict:
    host = request.headers.get("host", "localhost:8000")
    parts = host.split(".")
    subdomain = parts[0].lower()

    # Local dev fallback
    if subdomain in ["localhost", "127", "0"]:
        subdomain = request.headers.get("x-tenant", "public")

    tenant = await tenants_collection.find_one({"subdomain": subdomain})
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    tenant["id"] = tenant.pop("id", str(tenant["_id"]))
    tenant.pop("_id", None)
    return tenant

current_tenant = Depends(get_current_tenant)
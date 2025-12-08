# routers/tenants.py
from fastapi import APIRouter, Depends, HTTPException
from models import TenantCreate, Tenant
from core.tenant import tenants_collection

router = APIRouter(prefix="/tenants", tags=["Tenants"])

async def get_next_tenant_id() -> int:
    result = await tenants_collection.db.counters.find_one_and_update(
        {"_id": "tenant_id"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=True
    )
    return result["seq"]

@router.post("/", response_model=Tenant)
async def create_tenant(tenant_in: TenantCreate):
    existing = await tenants_collection.find_one({"subdomain": tenant_in.subdomain})
    if existing:
        raise HTTPException(status_code=400, detail="Subdomain already taken")

    tenant_dict = tenant_in.model_dump()
    tenant_dict["id"] = await get_next_tenant_id()

    result = await tenants_collection.insert_one(tenant_dict)
    created = await tenants_collection.find_one({"_id": result.inserted_id})
    created["id"] = created.pop("id", str(created["_id"]))
    created.pop("_id", None)
    return created
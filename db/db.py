# db.py
import motor.motor_asyncio
from typing import List, Dict, Any, Optional
from bson import ObjectId
from models import User, UserCreate
from core.security import get_password_hash

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.myapp
collection = db.users

_counter = 0

async def get_counter() -> int:
    global _counter
    cursor = db.counters.find_one({"_id": "user_id"})
    if cursor:
        _counter = cursor.get("seq", 0)
    else:
        _counter = 0
    return _counter

async def increment_counter() -> int:
    global _counter
    _counter += 1
    await db.counters.update_one(
        {"_id": "user_id"},
        {"$set": {"seq": _counter}},
        upsert=True
    )
    return _counter

async def get_all() -> List[Dict[str, Any]]:
    users = await collection.find().to_list(length=100)
    for user in users:
        user["id"] = user.get("id", user["_id"])
        if "_id" in user:
            del user["_id"]
    return users

async def get_by_id(user_id: int):
    user = await collection.find_one({"id": user_id})
    if user:
        user["id"] = user.pop("id", str(user["_id"]))
        user.pop("_id", None)
        user.pop("hashed_password", None)
    return user

async def get_by_email(email: str):
    user = await collection.find_one({"email": email})
    if user:
        user["id"] = user.pop("id", str(user["_id"]))
        user.pop("_id", None)
    return user

# db.py
async def create_user(user: UserCreate, tenant_id: int) -> dict:
    existing = await collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_dict = user.model_dump()
    user_dict["tenant_id"] = tenant_id
    user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))

    user_dict["id"] = await increment_counter()
    result = await collection.insert_one(user_dict)

    created = await collection.find_one({"_id": result.inserted_id})
    created["id"] = created.pop("id", str(created["_id"]))
    created.pop("_id", None)
    created.pop("hashed_password", None)
    return created


async def update(user_id: int, update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    result = await collection.update_one({"id": user_id}, {"$set": update_data})
    if result.modified_count == 0:
        return None
    return await get_by_id(user_id)

async def delete(user_id: int) -> bool:
    result = await collection.delete_one({"id": user_id})
    return result.deleted_count > 0
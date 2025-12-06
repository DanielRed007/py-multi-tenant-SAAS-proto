# db.py
from typing import List, Dict, Any

# This is your fake database for now
fake_users_db: List[Dict[str, Any]] = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# These are the functions your router will call
def get_all() -> List[Dict[str, Any]]:
    return fake_users_db

def get_by_id(user_id: int) -> Dict[str, Any] | None:
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    return None

def create(user_data: Dict[str, Any]) -> Dict[str, Any]:
    user_data["id"] = len(fake_users_db) + 1
    fake_users_db.append(user_data)
    return user_data
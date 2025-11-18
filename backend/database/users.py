import json
import os
from typing import Optional, Dict, List
from datetime import datetime

USERS_FILE = "backend/database/users.json"

def init_db():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump([], f)

def get_all_users() -> List[Dict]:
    init_db()
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users: List[Dict]):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def get_user_by_email(email: str) -> Optional[Dict]:
    users = get_all_users()
    for user in users:
        if user['email'] == email:
            return user
    return None

def create_user(name: str, email: str, hashed_password: str) -> Dict:
    users = get_all_users()
    
    if get_user_by_email(email):
        raise ValueError("User with this email already exists")
    
    user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": hashed_password,
        "created_at": datetime.utcnow().isoformat()
    }
    
    users.append(user)
    save_users(users)
    
    return {k: v for k, v in user.items() if k != 'password'}

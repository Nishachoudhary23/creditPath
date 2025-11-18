from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, EmailStr
from typing import Optional
from backend.auth.password import hash_password, verify_password
from backend.auth.jwt_handler import create_access_token, verify_token
from backend.database.users import get_user_by_email, create_user

router = APIRouter()

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict

@router.post("/signup", response_model=TokenResponse)
async def signup(request: SignupRequest):
    try:
        existing_user = get_user_by_email(request.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_pwd = hash_password(request.password)
        user = create_user(request.name, request.email, hashed_pwd)
        
        token = create_access_token(data={"sub": user["email"], "user_id": user["id"]})
        
        return {
            "access_token": token,
            "token_type": "bearer",
            "user": user
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    user = get_user_by_email(request.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    if not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_access_token(data={"sub": user["email"], "user_id": user["id"]})
    
    user_data = {k: v for k, v in user.items() if k != 'password'}
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user_data
    }

async def get_current_user(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user = get_user_by_email(payload.get("sub"))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return {k: v for k, v in user.items() if k != 'password'}

@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return current_user

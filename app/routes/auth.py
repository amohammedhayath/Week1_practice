from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_current_user
from app.models.user import User
from app.db.deps import get_db
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.core.security import verify_password
from app.core.jwt_handler import create_access_token
from app.schemas.user_schema import UserResponse


router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(401, "Invalid credentials")

    if verify_password(data.password, user.password_hash) is False:
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}

@router.get("/profile", response_model=UserResponse)
def get_user(current_user = Depends(get_current_user)):
    return current_user
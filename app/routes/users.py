from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.models.user import User
from app.schemas.user_schema import UserResponse
from typing import List

router = APIRouter()

@router.get("/users", response_model = List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users_list = db.query(User).all()
    return users_list
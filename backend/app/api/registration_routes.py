from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from app.database.models import User
from app.database.connection import SessionLocal
from app.auth.authentication import get_password_hash

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    password: str


@router.post("/register", response_model=dict)
def register_user(user: UserCreate):
    """
    Endpoint to register a new user.
    """
    db = SessionLocal()
    # Check if user already exists
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    # Hash the password and create a new user
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"id": new_user.id, "username": new_user.username}

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from db import get_db
from models.user import User
from schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["users"])
db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=UserRead)
async def read_all_users(db: db_dependency):
	users = db.query(User).all()
	return users

@router.get("/{user_id}", response_model=UserRead)
async def read_user(db: db_dependency, user_id: int):
	user = db.get(User, user_id)
	if user is None:
		raise HTTPException(status_code=404, detail="User not found")
	return user
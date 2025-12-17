from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from db import get_db
from models.book import Book

router = APIRouter(prefix="/books", tags=["books"])

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/")
def read_all(db: db_dependency):
	return db.query(Book).all()

@router.get("/{book_id}")
def read_book_by_id(book_id: int, db: db_dependency):
	book_model = db.query(Book).filter(Book.id == book_id).first()
	if book_model is not None:
		return book_model
	raise HTTPException(status_code=404, detail="Book not found")
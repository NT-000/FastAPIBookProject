from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import Annotated, Optional
from db import get_db
from models.book import Book
from schemas.book import BookCreate, BookRead, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/")
def read_all(db: db_dependency):
	return db.query(Book).all()

@router.get("/{book_id}")
def read_book_by_id(db: db_dependency, book_id: int = Path(gt=0)):
	book_model = db.get(Book, book_id)
	if book_model is not None:
		return book_model
	raise HTTPException(status_code=404, detail="Book not found")

@router.get("/categories/")
def read_book_by_category(db: db_dependency, category : Optional[str] = None):
	query = db.query(Book)
	if category is not None:
		query = query.filter(Book.category == category)
	return query.all()

@router.post("/", response_model=BookRead, status_code=201)
def create_book(db: db_dependency, book: BookCreate):
	db_book = Book(**book.model_dump(), user_id=1) # temp default user_id
	db.add(db_book) # pre transaction, getting the db ready
	db.commit() # doing the transaction to the db
	db.refresh(db_book) # gets id from db
	return db_book

@router.put("/{book_id}", status_code=204)
def update_book(db: db_dependency, book_update: BookUpdate, book_id: int = Path(gt=0)):
	book_model = db.get(Book, book_id)
	if book_model is None:
		raise HTTPException(status_code=404, detail="Book not found")

	if book_update.title is not None:
		book_model.title = book_update.title
	if book_update.author is not None:
		book_model.author = book_update.author
	if book_update.description is not None:
		book_model.description = book_update.description
	if book_update.price is not None:
		book_model.price = book_update.price
	if book_update.category is not None:
		book_model.category = book_update.category
	if book_update.rating is not None:
		book_model.rating = book_update.rating

	db.commit()
	db.refresh(book_model)

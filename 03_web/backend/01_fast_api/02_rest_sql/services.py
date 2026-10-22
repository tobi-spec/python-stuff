from typing import List

from database import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def create_book(db: Session, data: BookCreate) -> Book:
    book = Book(*data.model_dump())
    db.add(book)
    db.commit()
    db.refresh()
    return book

def get_books(db: Session) -> list[type[Book]]:
    return db.query(Book).all()
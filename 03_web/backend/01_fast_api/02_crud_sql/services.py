from database import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def create_book(db: Session, data: BookCreate) -> Book:
    book = Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db: Session) -> list[type[Book]]:
    return db.query(Book).all()

def get_book(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, data: BookCreate) -> Book:
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        for key, value in data.model_dump().items():
            setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book
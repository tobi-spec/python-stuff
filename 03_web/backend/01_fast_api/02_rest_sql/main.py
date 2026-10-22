from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
import services, database, schemas
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/books", response_model=List[schemas.Book])
def get_all_books(db: Session = Depends(database.get_db)):
    return services.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(database.get_db)):
    result = services.get_book(db, book_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return result

@app.post("/books", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return services.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book_by_id(book: schemas.BookCreate, book_id: int, db: Session = Depends(database.get_db)):
    result = services.update_book(db, book_id, book)
    if result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return result

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book_by_id(book_id: int, db: Session = Depends(database.get_db)):
    result = services.delete_book(db, book_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return result



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
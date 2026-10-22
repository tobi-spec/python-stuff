from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
import services, database, schemas
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/books", response_model=List[schemas.Book])
def get_books_endpoint(db: Session = Depends(database.get_db)):
    return services.get_books(db)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
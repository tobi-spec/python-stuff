from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    description: str
    author: str
    year: int = 2024

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class config:
        from_attribute = True
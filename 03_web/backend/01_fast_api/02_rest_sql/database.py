from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Integer, Column, String

engine = create_engine('postgresql+psycopg2://admin:admin@localhost:5432/exampledb', echo=True)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)


def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()

def create_table() -> None:
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_table()
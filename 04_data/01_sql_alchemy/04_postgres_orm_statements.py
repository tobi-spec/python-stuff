from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker
)

engine = create_engine('postgresql+psycopg2://admin:admin@localhost:5432/exampledb', echo=True)

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

try:
    with Session.begin() as session:
        session.add_all([
            Person(name="John", age=22),
            Person(name="Sarah", age=31),
        ])
except SQLAlchemyError as e:
    print(f"Insert failed: {e}")

try:
    with Session() as session:
        people = session.scalars(select(Person)).all()
        for person in people:
            print(person.name, person.age)
except SQLAlchemyError as e:
    print(f"Select failed: {e}")

try:
    with Session.begin() as session:
        person = session.get(Person, 1)
        if person is not None:
            person.age = 99
except SQLAlchemyError as e:
    print(f"Update failed: {e}")

try:
    with Session() as session:
        people = session.scalars(select(Person).where(Person.name == "John")).all()
        for person in people:
            print(person.name, person.age)
except SQLAlchemyError as e:
    print(f"Select failed: {e}")




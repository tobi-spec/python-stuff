from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.sqltypes import Integer, String

# dialect+driver://username:password@host:port/dbname
engine = create_engine('postgresql+psycopg2://admin:admin@localhost:5432/exampledb', echo=False)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer)
)

meta.create_all(engine)

# atomic execution
try:
    with engine.begin() as connection:
        insert_statement = people.insert().values(name="John", age=22)
        result = connection.execute(insert_statement)
        print(f"Inserted row with id {result.inserted_primary_key[0]}")
except SQLAlchemyError as e:
    print(f"Error: {e}")

try:
    with engine.begin() as connection:
        insert_statement = people.insert().values(name="Sarah", age=31)
        result = connection.execute(insert_statement)
    print(f"Inserted row with id {result.inserted_primary_key[0]}")
except SQLAlchemyError as e:
    print(f"Error: {e}")

try:
    with engine.begin() as connection:
        select_statement = people.select()
        result = connection.execute(select_statement)
        for row in result.fetchall():
            print(row)
except SQLAlchemyError as e:
    print(f"Error: {e}")

try:
    with engine.begin() as connection:
        update_statement = people.update().where(people.c.id == 1).values(age=50)
        result = connection.execute(update_statement)
    print(f"Updated {result.rowcount} row(s)")
except SQLAlchemyError as e:
    print(f"Error: {e}")

try:
    with engine.begin() as connection:
        select_statement = people.select().where(people.c.name == "John")
        result = connection.execute(select_statement)
        for row in result.fetchall():
            print(row)
except SQLAlchemyError as e:
    print(f"Error: {e}")




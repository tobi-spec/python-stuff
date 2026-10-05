from sqlalchemy import create_engine, MetaData, Table, Column, Float
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

things = Table(
    "things",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("value", Float),
    Column("owner", String, foreign_key="people.id")
)

insert_people = people.insert().values([
    {"name": "John", "age": 22},
    {"name": "Sarah", "age": 33},
    {"name": "Mike", "age": 38},
])

insert_things = things.insert().values([
    {"name": "Phone", "values": 112, "owner": 1},
    {"name": "Keyboard", "values": 12, "owner": 1},
    {"name": "Mouse", "values": 60, "owner": 2},
    {"name": "Screen", "values": 150, "owner": 3},
])

meta.create_all(engine)

try:
    with engine.begin() as connection:
        connection.execute(insert_people)

    with engine.begin() as conection:
        connection.execute(insert_things)
except SQLAlchemyError as e:
    print(e)

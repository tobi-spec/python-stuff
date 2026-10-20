from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# sqlite
# driver not needed, python assumes the build-it sqlite3 driver
engine = create_engine('sqlite:///mydatabase.db', echo=True)

connection = engine.connect()
connection.execute(text("CREATE TABLE IF NOT EXISTS people(name str, age int)"))
connection.commit()

session = Session(engine)
session.execute(text("INSERT INTO people(name, age) VALUES ('mike', '30')"))
session.commit()
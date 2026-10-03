import sqlite3
from employee import Employee

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE employees  (
                first text,
                last text,
                pay integer)""")

emp_1 = Employee(first="John", last="Smith", pay=80000)
emp_2 = Employee(first="Jane", last="Smith", pay=80000)

cursor.execute(f"INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
connection.commit()

cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})
connection.commit()

cursor.execute("SELECT * FROM employees WHERE last=?", ('Smith', ))
print(cursor.fetchall())

cursor.execute("SELECT * FROM employees WHERE first=:first", {"first": emp_1.first})
print(cursor.fetchall())

connection.commit()
connection.close()

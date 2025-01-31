import sqlite3

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


conn = sqlite3.connect('employee.db')

# we can run sql commands with cursor
curs = conn.cursor()
def create_table():
    curs.execute("""CREATE TABLE employees (
                   first text,
                   last text,
                   pay integer
                   )""")
def insert_to_db (cursor, first, last, pay):
    cursor.execute(f"INSERT INTO employees VALUES ('{first}', '{last}', {pay})")

insert_to_db(curs, "Samandar", "Buriyev", 200000)

# saving changes to db
conn.commit()
#closing the connection
conn.close()
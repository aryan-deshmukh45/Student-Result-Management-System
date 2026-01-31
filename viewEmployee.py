import sqlite3

con = sqlite3.connect("employee.db")
cur = con.cursor()

cur.execute("SELECT * FROM employee")
for row in cur.fetchall():
    print(row)

con.close()

import sqlite3

con = sqlite3.connect("rms.db")
cur = con.cursor()

# Example table name (change if different)
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)

con.close()

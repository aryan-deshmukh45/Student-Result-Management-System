import sqlite3
def create_db():
    con = sqlite3.connect(database="employee.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name TEXT,
            l_name TEXT,
            contact TEXT,
            email TEXT UNIQUE,
            question TEXT,
            answer TEXT,
            password TEXT
        )
    """)
    con.commit()
    con.close()

create_db()

import sqlite3

conn = sqlite3.connect("nothing.db")
c = conn.cursor()

c.execute("""UPDATE chart SET first_name = 'Bob' WHERE rowid = 6 """)

c.execute("SELECT * FROM chart")

print(c.fetchall())

conn.commit()
conn.close()

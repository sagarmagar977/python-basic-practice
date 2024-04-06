import sqlite3
conn=sqlite3.connect("database.db")

data=conn.execute("SELECT * FROM student")
st_id=input("enter student id :")
conn.execute("DELETE FROM student where st_id="+st_id)
conn.commit()
conn.close()
conn=sqlite3.connect("database.db")
data=conn.execute("SELECT * FROM student")
for n in data:
    print(n[1],n[2],n[3])


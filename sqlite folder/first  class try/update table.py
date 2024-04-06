import sqlite3
conn=sqlite3.connect("database.db")
conn.execute(""" update student set St_name="hari thapa" where st_id=3
             """)
conn.execute(""" update student set St_class="Bsc. " where st_id=3
             """)
conn.commit()
conn.close()
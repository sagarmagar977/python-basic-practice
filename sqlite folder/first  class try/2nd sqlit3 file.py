import sqlite3
conn=sqlite3.connect("database.db")
ins='''
     insert into student (st_name, st_class,st_email) values ("Ravi","12th","ravi@gmail.com")

      '''
conn.execute(ins)
conn.commit()
conn.close()
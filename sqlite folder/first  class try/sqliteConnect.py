import sqlite3
conn=sqlite3.connect("database.db")
conn.execute("""
Create table student (
      st_id INT AUTO_INCREMENT PRIMARY KEY,
      st_name  VARACHAR(50),
      st_class VARCHAR(10),
      st_email VARCHAR(30)        
    



)
             
             
             """)
conn.close()
  
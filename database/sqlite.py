import sqlite3

conexion = sqlite3.connect("productos ")
cursor = conexion.cursor()
conexion.execute("PRAGMA FOREIGN_KEY = ON")

cursor.execute("""CREATE TABLE  IF NOT EXISTS product(
    ID_PRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT ,
    price TEXT  
)
               """)
conexion.commit()


conexion.close()
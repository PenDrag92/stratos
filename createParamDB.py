import time, os,sys, sqlite3


location = "C:\\sqlite\db\pythonsqlite.db"

conn = sqlite3.connect(location)
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS myTable (id INTEGER PRIMARY KEY, name VARCHAR, code INTEGER);")
c.execute("INSERT INTO myTable (code,name) VALUES (100,\'Hola\');")
c.execute("INSERT INTO myTable (code,name) VALUES (20,\'Quien Soy\');")
c.execute("INSERT INTO myTable (code,name) VALUES (200,\'Adios\');")
conn.commit()

c.close()
conn.close()

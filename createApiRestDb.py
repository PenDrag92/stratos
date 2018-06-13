import time, os,sys, sqlite3


location = "C:\\sqlite\db\pythonsqlite.db"

conn = sqlite3.connect(location)
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS apiTable (id INTEGER PRIMARY KEY, insertDate VARCHAR, params VARCHAR);")
c.execute("INSERT INTO apiTable (insertDate,params) VALUES (10,\'aa\');")
c.execute("INSERT INTO apiTable (insertDate,params) VALUES (20,\'bb\');")
c.execute("INSERT INTO apiTable (insertDate,params) VALUES (200,\'cc\');")
conn.commit()

c.close()
conn.close()

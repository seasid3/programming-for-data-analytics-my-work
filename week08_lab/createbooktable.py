# This code will create a SQLite database and a table named 'books' with specified columns.
# Author: Andrew Beatty lab

import sqlite3
con = sqlite3.connect('pfda.db') # calling this database pfda.db
cur = con.cursor()
# sql = "DROP TABLE IF EXISTS books;" # drop table if it already exists
# cur.execute(sql)

cur.execute("CREATE TABLE book(title, author, ISBN)")
con.commit()
con.close()
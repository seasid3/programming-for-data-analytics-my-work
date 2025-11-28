# This code will insert a new book record into the 'books' table in the SQLite database.
# Author: Andrew Beatty lab

import sqlite3
con = sqlite3.connect('pfda.db')  # connecting to the database pfda.db
cur = con.cursor()

# check there is nothing in the db
result = cur.execute("select * from book;")
print (result.fetchall())

# insert a book
sql = "INSERT INTO book VALUES (?, ?, ?)"
data = [
        ('Harr1', 'Just kid', "123"),
        ('Harr2', 'Just kid 2', "124")
]     
cur.executemany(sql, data)

con.commit() 

result = cur.execute("select * from book")
print(result.fetchall())
con.close()



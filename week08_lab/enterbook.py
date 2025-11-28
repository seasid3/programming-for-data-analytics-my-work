# Code that cannot allow sql injection
# Author: Andrew Beatty lab

import sqlite3
con = sqlite3.connect('pfda.db')  # connecting to the database pfda.db
cur = con.cursor()

book = {}
book['title'] = input("Enter book title: ")
book['author'] = input("Enter book author: ")
book['ISBN'] = input("Enter book ISBN: ")
# print (book)

data =  [book] # should be [] although some docs say ()
sql = "insert into book values (:title, :author, :ISBN)" # named parameters
cur.executemany(sql, data)
con.commit()

for row in cur.execute("SELECT * FROM book"):
    print(f"row {row}")

con.close()
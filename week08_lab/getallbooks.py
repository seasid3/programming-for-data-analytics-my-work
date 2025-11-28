# this code will see the whole table
# Author: Andrew Beatty lab

import sqlite3
con = sqlite3.connect('pfda.db')  # connecting to the database pfda.db
cur = con.cursor()

for row in cur.execute("SELECT * FROM book"):
    print(f"row {row}")
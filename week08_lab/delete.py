# This code will delete an entry in a table
# Author: Andrew Beatty lab

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()
sql = "DELETE FROM students1 WHERE id = %s"
values = (1, )

cursor.execute(sql, values)
db.commit()
print("delete done")
cursor.close()
db.close()
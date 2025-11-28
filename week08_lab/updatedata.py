# This code will update the student1 table
# Author: Andrew Beatty lab

import mysql.connector

db = mysql.connector.connect(
    host="localhost",       
    user="root",
    password="",    
    database="wsaa"
)

cursor = db.cursor()
sql = "UPDATE students1 SET name = %s, age=%s where id = %s"
values = ("Alice", 23, 2)

cursor.execute(sql, values)
db.commit()
print("update done")
cursor.close()
db.close()
# This code will view data in the student1 table
# Author: Andrew Beatty lab

import mysql.connector

db = mysql.connector.connect(
    host="localhost",       
    user="root",
    password="",                
    database="wsaa"
)

cursor = db.cursor()
sql = "SELECT * FROM students1 where id = %s"
values = (1, )

cursor.execute(sql, values)
result = cursor.fetchall()      
for x in result:
    print(x)

cursor.close()
db.close()
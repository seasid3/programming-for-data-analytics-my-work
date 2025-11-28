# this code will insert data
# Author: Andrew Beatty lab

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",                
    database="wsaa"
)

cursor = db.cursor()    
sql = "INSERT INTO students1 (name, age) VALUES (%s, %s)"
data = [
        ('Andrew', 21),
        ('John', 22),
        ('Mary', 20)
]           

cursor.executemany(sql, data)
db.commit()     

print("1 recoded insterted, ID:", cursor.lastrowid)
cursor.close()
db.close()

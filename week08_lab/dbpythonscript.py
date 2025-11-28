# this code will create a table in hte wsaa database using mysql and python
# Author: Andrew Beatty lab

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

mycursor = mydb.cursor()
sql = "CREATE TABLE students1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

mycursor.execute(sql)   
mydb.close()
mycursor.close()


# This file will put everything into a file taht can be used from another dile (e.g. from your flask app)

import mysql.connector

class StudentDAO:
    host = ""
    user = ""
    password = ""       
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        # these should be read from a config file
        self.host = "localhost"
        self.user = "root"  
        self.password = ""
        self.database = "wsaa"

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeall(self):
        self.cursor.close()
        self.connection.close()

    def create(self, values):
        cursor = self.getcursor()
        sql = "INSERT INTO students1 (name, age) VALUES (%s, %s)"
        cursor.execute(sql, values)
       
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeall()
        return newid
    
    def getall(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM students1"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeall()
        return result
    
    def findbyid(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM students1 WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeall()
        return result
    
    def update(self, values):
        cursor = self.getcursor()
        sql = "UPDATE students1 SET name = %s, age = %s WHERE id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        affected = cursor.rowcount
        self.closeall()
        return affected
    
    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM students1 WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        affected = cursor.rowcount
        self.closeall()
        return affected

studentDAO = StudentDAO()
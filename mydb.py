import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'zajar@gmail7799'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE ictm3")

print('all done!')
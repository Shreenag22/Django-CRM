import mysql.connector 
dataBase=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd='Virat@123'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE may23")

print("all done")
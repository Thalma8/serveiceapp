import mysql.connector
database = mysql.connector.connect(
 host = 'localhost',
 user = 'root',
 passwd = '',
 )

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE serviceapp")

print("All done")
import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", passwd="Deer@ps8401")


# preparea cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE ubpool")

print("Database created")

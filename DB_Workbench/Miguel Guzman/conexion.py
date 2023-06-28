import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root2013",
    database="proyectov1"
)

print(midb)
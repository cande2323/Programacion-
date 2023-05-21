import mysql.connector
midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="123456",
 database="projecto_integrador"
)
print(midb)

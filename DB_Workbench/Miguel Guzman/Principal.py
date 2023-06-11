import mysql.connector

midb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Root2013",
 database="projecto_integrador"
)
print(midb)

cursor=midb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)
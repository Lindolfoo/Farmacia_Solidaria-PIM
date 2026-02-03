import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="farmacia_solidaria",
    port=3306
)

print("Conectou com sucesso!")
conn.close()

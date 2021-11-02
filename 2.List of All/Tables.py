import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='raghu', host='127.0.0.1', database='1.tutorialspoint'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Retrieving the list of Tables:-
print("List of Tables: ")
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

#Closing the connection
conn.close()
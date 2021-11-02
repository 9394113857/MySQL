import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='raghu', host='127.0.0.1')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

# Closing the connection
conn.close()

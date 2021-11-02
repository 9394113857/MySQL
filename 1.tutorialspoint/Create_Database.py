import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='raghu', host='127.0.0.1')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Doping database 1.tutorialspoint if already exists.
cursor.execute("DROP database IF EXISTS 1.tutorialspoint")

# Preparing query to create a database
sql = "CREATE database 1.tutorialspoint";

# Creating a database
cursor.execute(sql)

print("1.Database Created Successfully")

# Retrieving the list of databases
print("2.List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

# Closing the connection
conn.close()

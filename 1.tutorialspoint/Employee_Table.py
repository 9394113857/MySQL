import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='raghu', host='127.0.0.1', database='1.tutorialspoint'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)

print("1.Table Created Succesfully")

# Retrieving the list of Tables:-
print("2.List of Tables: ")
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

#Closing the connection
conn.close()
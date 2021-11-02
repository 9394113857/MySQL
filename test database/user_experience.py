import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='raghu', host='localhost', database='test'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS USER_EXPERIENCE")

#Creating table as per requirement
sql ='''CREATE TABLE USER_EXPERIENCE(
   USER_EXP_ID INT(10) auto_increment primary key,
   USER_ID	INT(10),
   HOSPITAL_NAME VARCHAR(100),
   FROM_DATE DATE,
   TO_DATE DATE
)'''
cursor.execute(sql)

# Retrieving the list of Tables:-
print("List of Tables: ")
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

#Closing the connection
conn.close()
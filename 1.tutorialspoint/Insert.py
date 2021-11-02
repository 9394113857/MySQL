import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='raghu', host='127.0.0.1', database='1.tutorialspoint')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

   # Fetching 1st row from the table
   result = cursor.fetchone();
   print(result)

   # Fetching 1st row from the table
   result = cursor.fetchall();
   print(result)


except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='raghu', host='127.0.0.1', database='test')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO USER_EXPERIENCE(
   USER_ID, HOSPITAL_NAME)
   VALUES (1, 'Apollo')"""

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Retrieving single row
   sql_data = '''SELECT * from EMPLOYEE'''

   # Executing the query
   cursor.execute(sql_data)

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
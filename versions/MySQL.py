import mysql.connector

# Create the connection object
# myconn = mysql.connector.connect(host="localhost", user="root", passwd="raghu")
myconn = mysql.connector.connect(user='root', password='raghu',
                               host='127.0.0.1', database='clinicalfirst')


# printing the connection object:-
print("printing the connection object:-")
print(myconn)

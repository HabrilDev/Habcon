import mysql.connector


connection = mysql.connector.connect(host='192.168.1.70',
                                     database='servercon',
                                     user='sockuser',
                                     password='pwd')

mySql_Create_Table_Query = """CREATE TABLE Login( 
                         Name VARCHAR(250) NOT NULL,
                         EmailID VARCHAR(320)NOT NULL,
                         Password CHAR(120),
                         LastLogin DATETIME NOT NULL,
                         LoginIp VARCHAR(250) NOT NULL,
                         AccountCreation DATETIME NOT NULL,
                         PRIMARY KEY (EmailID))"""

cursor = connection.cursor()
result = cursor.execute(mySql_Create_Table_Query)
print("Users table created successfully ")

if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")


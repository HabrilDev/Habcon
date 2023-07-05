import mysql.connector

connection = mysql.connector.connect(host='192.168.1.70',
                                     database='servercon',
                                     user='sockuser',
                                     password='pwd')
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)


if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
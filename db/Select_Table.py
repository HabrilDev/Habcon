import mysql.connector


connection = mysql.connector.connect(host='65.1.195.121',
                                     database='db',
                                     user='uname',
                                     password='pwd')

sql_select_Query = "select * from Laptop"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)
print("\nPrinting each row")
for row in records:
    print("UserID = ", row[0], )
    print("Name = ", row[1])
    print("Price  = ", row[2])
    print("Purchase date  = ", row[3], "\n")

if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")


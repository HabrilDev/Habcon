import mysql.connector


connection = mysql.connector.connect(host='192.168.1.70',
                                         database='servercon',
                                         user='sockuser',
                                         password='pwd')

sql_select_Query = "select * from Login"
cursor = connection.cursor()
cursor.execute(sql_select_Query)

records = cursor.fetchall()
print("Total number of rows in table:", cursor.rowcount,"\n")

for row in records:
    print("Name = ", row[0])
    print("Email ID  = ", row[1])
    print("Password = ", row[2])
    print("Last Login  = ", row[3])
    print("Login Ip  = ", row[4])
    print("Account Creation  = ", row[5], "\n")


if connection.is_connected():
    connection.close()
    cursor.close()
    print("MySQL connection is closed")
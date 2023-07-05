import mysql.connector

def insert_varibles_into_table(name, emailID, password, lastLogin, loginIp, accountCreation):
    connection = mysql.connector.connect(host='192.168.1.70',
                                         database='servercon',
                                         user='sockuser',
                                         password='pwd')
    cursor = connection.cursor()
    mySql_insert_query = """INSERT INTO Login (Name, EmailID, Password, LastLogin, LoginIp, AccountCreation) 
                            VALUES (%s, %s, %s, %s, %s, %s) """

    record = (name, emailID, password, lastLogin, loginIp, accountCreation)
    cursor.execute(mySql_insert_query, record)
    connection.commit()
    print("Record inserted successfully into Laptop table")
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


insert_varibles_into_table('Ting', 'email', '$2b$12$NTZCih/HMZOjl1CM3GU2I.SLP9nGXkaNJ2ByFXu/peTnBt1/.y8EO', '2021-05-28 12:38:58.463228', '192.168.1.60', '2021-05-27 17:23:48.703520')

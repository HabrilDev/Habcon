import time

import mysql.connector

connection = mysql.connector.connect(host='192.168.1.70',
                                     database='servercon',
                                     user='sockuser',
                                     password='pwd')
cursor = connection.cursor()


def username(usern):
    sql_select_Query = "select * from Login"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    status = 0
    for row in records:
        if row[1] == usern:
            status = "found"
            break
        else:
            status = "notfound"
    return status
def password(passw, name):
    sql_select_Query = "select * from Login"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    verify = 0
    for row in records:
        if row[2] == passw and row[1] == name:
            verify = "correct"
            break
        else:
            verify = "wrong"
    return verify
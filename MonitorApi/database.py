import mysql.connector


class Database():
    def __init__(self):
        self.connection = mysql.connector.connect(host='192.168.1.70',
                                             database='servercon',
                                             user='sockuser',
                                             password='pwd')
        self.cursor = self.connection.cursor()


    def username(self, usern):
        sql_select_Query = "select * from Login"
        self.cursor.execute(sql_select_Query)
        records = self.cursor.fetchall()
        status = 0
        for row in records:
            if row[1] == usern:
                status = "found"
                break
            else:
                status = "notfound"
        return status
    def password(self, passw, name):
        sql_select_Query = "select * from Login"
        self.cursor.execute(sql_select_Query)
        records = self.cursor.fetchall()
        verify = 0
        for row in records:
            if row[2] == passw and row[1] == name:
                verify = "correct"
                break
            else:
                verify = "wrong"
        return verify
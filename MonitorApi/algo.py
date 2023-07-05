from MonitorApi import database
import time
import threading

class Algo:
    def __init__(self, dhost, duser, dpass, db):
        self.dhost = dhost
        self.duser = duser
        self.dpass = dpass
        self.db = db

    def passwordver(self, passw):
        pass

    def userver(self, *args):
        pass

    def run(self, task, pay1, pay2):
        if task == "lpass":
            self.passwordver(pay1)
        if task == "luser":
            self.userver(pay1)





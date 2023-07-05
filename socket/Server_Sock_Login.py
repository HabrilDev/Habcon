import socket
import time
import threading
import logging
import mysql.connector
from MonitorApi import database

logging.basicConfig(filename="server_monitor.log", format="%(asctime)s - %(levelname)s - %(message)s",
                    filemode="w")


class ServerSock:
    def __init__(self):
        self.host = ''
        self.port = 49158
        self.ss = socket.socket()
        self.ss.bind((self.host, self.port))
        self.ss.listen(1)
        self.conn = "a"
        self.address = "a"
        self.thread = "a"

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.ksignal = False

    def handler(self, server, addr):
        connection = mysql.connector.connect(host='192.168.1.70',
                                             database='servercon',
                                             user='sockuser',
                                             password='pwd')
        sql_select_Query = "select * from Login"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        outdata = "o"
        indata = "o"
        logged = False
        while not indata == "Received output":
            if self.ksignal:
                server.send("bye".encode())
                self.logger.info(f"Bye message sent for thread kill: {addr}")
                time.sleep(5)
                server.close()
                self.logger.info(f"Thread kill has been initiated: {addr}")
                break
            indata = server.recv(1024).decode()
            self.logger.info(f"Input from {addr}: " + str(indata))
            print(f"Input from {addr}: " + str(indata))
            if not logged:
                if indata == "Hello":
                    outdata = "NUOE"
                    server.send(outdata.encode())
                    self.logger.info(f"NUOE message has been sent to: {addr}")
                    time.sleep(5)
                elif indata == "e":
                    outdata = "UN"
                    server.send(outdata.encode())
                    self.logger.info(f"UN message has been sent to: {addr}")
                elif indata[0] == "U":
                    uname = indata[3:]
                    if database.username(uname) == "found":
                        outdata = "PA"
                        server.send(outdata.encode())
                        self.logger.info(f"PA message has been sent to: {addr}")
                    else:
                        outdata = "UNF"
                        server.send(outdata.encode())
                        self.logger.info(f"UNF message has been sent to: {addr}")
                elif indata[0] == "P":
                    uname = indata[2:]
                    if database.username(uname) == "correct":
                        logged = True
                        outdata = "LI"
                        server.send(outdata.encode())
                        self.logger.info(f"LI message has been sent to: {addr}")
                    else:
                        outdata = "WP"
                        server.send(outdata.encode())
                        self.logger.info(f"WP message has been sent to: {addr}")

    def threader(self):
        while True:
            if threading.activeCount() >= 10:
                self.ksignal = True
                self.logger.info(f"Kill signal sent to threads.")
                time.sleep(10)
                self.end()
                break

            self.conn, self.address = self.ss.accept()
            self.thread = threading.Thread(target=self.handler, args=(self.conn, self.address))
            self.thread.start()
            print(f"Thread count: {threading.activeCount()}")
            self.logger.info(f"New thread created, thread count: {threading.activeCount()}")
            print(f"Active connections: {threading.activeCount() - 1}")
            self.logger.info(f"New connection from: {self.address}")

    def end(self):
        self.ss.close()
        self.logger.info(f"Main socket has been closed")


sock = ServerSock()
accthread = threading.Thread(target=sock.threader())

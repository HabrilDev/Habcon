import socket
import time

class ServerSock:
    def __init__(self):
        self.host = ''
        self.port = 49158
        self.ss = socket.socket()
        self.ss.bind((self.host, self.port))
        self.ss.listen(1)
        self.conn = 0
        self.address = 0
        self.indata = "a"
        self.outdata = "a"

    def accept(self):
        self.conn, self.address = self.ss.accept()
        print("Connection from: " + str(self.address))

    def recvcmd(self):
        while not self.indata == "Received output":
            self.indata = self.conn.recv(1024).decode()
            print("Input from user: " + str(self.indata))
            if self.indata.isdigit():
                break
            elif self.indata == "hello":
                self.outdata = "Hello from proxima"
                self.conn.send(self.outdata.encode())
                time.sleep(5)
            elif self.indata == "temp":
                self.outdata = "10"
                self.conn.send(self.outdata.encode())



    def end(self):
        self.ss.close()



sock = ServerSock()
sock.accept()
sock.recvcmd()
sock.end()

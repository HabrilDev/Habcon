import socket
import time
import threading


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

    def handler(self, server, addr):
        # self.server = server
        # self.addr = addr
        outdata = "o"
        indata = "o"
        while not indata == "Received output":
                indata = server.recv(1024).decode()
                print(f"Input from {addr}: " + str(indata))
                if indata.isdigit():
                    break
                elif indata == "Hello from commander":
                    outdata = "Hello from proxima"
                    server.send(outdata.encode())
                    time.sleep(5)
                elif indata == "temp":
                    outdata = "10"
                    server.send(outdata.encode())



    def threader(self):
        while True:
            self.conn, self.address = self.ss.accept()
            self.thread = threading.Thread(target=self.handler, args=(self.conn, self.address))
            self.thread.start()
            print(f"Thread count: {threading.activeCount()}")
            print(f"Active connections: {threading.activeCount() - 1}")

    def end(self):
        self.ss.close()



sock = ServerSock()
accthread = threading.Thread(target=sock.threader())
sock.end()

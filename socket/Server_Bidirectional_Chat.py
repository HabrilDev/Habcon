import socket
import time
import threading
import logging
logging.basicConfig(filename="server_monitor.log", format="%(asctime)s - %(levelname)s - %(message)s",
                            filemode="w")

class ServerSock():
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
        outdata = "o"
        indata = "o"
        while not indata == "Received output":
            if self.ksignal == True:
                server.send("bye".encode())
                self.logger.info(f"Bye message sent for thread kill: {addr}")
                time.sleep(5)
                server.close()
                self.logger.info(f"Thread kill has been initiated: {addr}")
                break
            indata = server.recv(1024).decode()
            self.logger.info(f"Input from {addr}: " + str(indata))
            print(f"Input from {addr}: " + str(indata))
            if indata.isdigit():
                break
            elif indata == "Hello from commander":
                outdata = "Hello from proxima"
                server.send(outdata.encode())
                self.logger.info(f"Hello message has been sent to: {addr}")
                time.sleep(5)
            elif indata == "temp":
                outdata = "10"
                server.send(outdata.encode())
                self.logger.info(f"Temperature of proxima has been sent to: {addr}")
                server.send("bye".encode())
                self.logger.info(f"Bye message has been sent to: {addr}")

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


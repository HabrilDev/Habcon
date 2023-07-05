import time
import socket


class Task:
    def __init__(self, host, port):
        self.temp = "a"
        self.host = host
        self.port = port
        self.cs = socket.socket()
        self.cs.connect((host, port))
        self.lstatus = True
        self.data = "a"

    def temperature(self):
        self.cs.send("Hello from commander".encode())
        while self.lstatus:
            self.data = self.cs.recv(1024).decode()
            if self.data == "bye":
                self.end()
                break
            elif self.data == "Hello from proxima":
                print(self.data)
                self.cs.send("temp".encode())
            elif self.data.isdigit():
                print(f"Temperature is: {self.data}")
                self.cs.send("Received output".encode())

    def end(self):
        self.cs.close()


command = Task("192.168.1.70", 49158)
command.temperature()


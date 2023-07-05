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
        self.NUOE = "s"

    def temperature(self):
        self.cs.send("Hello".encode())
        while self.lstatus:
            self.data = self.cs.recv(1024).decode()
            if self.data == "bye":
                self.end()
                break
            elif self.data == "NUOE":
                while True:
                    self.NUOE = input("Are you an existing or a new user? e/n")
                    if self.NUOE == "e" or self.NUOE == "E" or self.NUOE == "Existing" or self.NUOE == "existing":
                        self.cs.send("e".encode())
                        break
                    elif self.NUOE == "n" or self.NUOE == "N" or self.NUOE == "New" or self.NUOE == "new":
                        self.cs.send("e".encode())
                        break
                    else:
                        print("Enter a valid input. n/e")
                        continue
            elif self.data == "UN":
                uname = "UN="+input("Enter your Email id: ")
                self.cs.send(uname.encode())
            elif self.data == "WUN":
                print("User name doesn't exist.")
                print("Please try again.")
                break
            elif self.data == "PA":
                password = "PA="+input("Enter your password: ")
                self.cs.send(password.encode())
            elif self.data == "LI":
                print("You have logged in.")
        self.cs.close()

    def end(self):
        self.cs.close()


command = Task("192.168.1.70", 49158)
command.temperature()


import paramiko

host = "proxima.boldmoon.in"
port = 22
username = "uname"
password = "pwd"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)
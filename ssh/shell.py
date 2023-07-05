import paramiko
import time
import sys
username = "uname"
hostname = "proxima.boldmoon.in"
password = "pwd"
ssh = paramiko.SSHClient()


def run_command(host, secret, uname):
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, uname, secret)
    shell = ssh.invoke_shell()
    shell.settimeout(0.25)

    shell.send('ls -lrt\n')
    time.sleep(2)
    sys.stdout.buffer.write(shell.recv(10000))
    sys.stdout.buffer.flush()

    shell.send('\x01')
    shell.send('\x11')

    time.sleep(2)
    sys.stdout.buffer.write(shell.recv(10000))
    sys.stdout.buffer.flush()
    print()
    time.sleep(2)

run_command(hostname, password, username)

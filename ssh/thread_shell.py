import paramiko

import time



buff = ''
resp = ''

import paramiko

username = "uname"
hostname = "proxima.boldmoon.in"
password = "pwd"
ssh = paramiko.SSHClient()


def run_command(host, secret, uname, command):
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, uname, secret)
    ssh.send(command)
    ssh.send('\n')
    time.sleep(1)
    resp = ssh.recv(9999)
    output = resp.decode('ascii').split(',')
    print(''.join(output))
    ssh.close()
    # for cmd in command:
    #     stdin, stdout, stderr = ssh.exec_command(cmd)
    #     lines = stdout.readlines()
    #     print(lines)
    # ssh.close()

run_command(hostname, password, username, "ls")




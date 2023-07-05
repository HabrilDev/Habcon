import paramiko

username = "uname"
hostname = "proxima.boldmoon.in"
password = "pwd"
ssh = paramiko.SSHClient()


def run_command(host, secret, uname, command):
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, uname, secret)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)
    # for cmd in command:
    #     stdin, stdout, stderr = ssh.exec_command(cmd)
    #     lines = stdout.readlines()
    #     print(lines)
    ssh.close()

run_command(hostname, password, username, "ls && cd / && ls")

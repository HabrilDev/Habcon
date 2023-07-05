import paramiko

router_ip = "proxima.boldmoon.in"
router_username = "uname"
router_password = "pwd"

ssh = paramiko.SSHClient()


def run_command(ip_address, username, password, command):
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    total_attempts = 3
    for attempt in range(total_attempts):
        try:
            print("Attempt to connect: %s" % attempt)
            ssh.connect(router_ip,
                        username=router_username,
                        password=router_password,
                        look_for_keys=False)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            output = ssh_stdout.readlines()
            ssh.close()
            return output

        except Exception as error_message:
            print("Unable to connect")
            print(error_message)

router_output = run_command(router_ip, router_username, router_password, "show ip route")

if router_output != None:
    for line in router_output:
        if "0.0.0.0/0" in line:
            print("Found default route:")
            print(line)
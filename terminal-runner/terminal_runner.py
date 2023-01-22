import subprocess
from getpass import getpass

def run_ls():
    command = "ls -la".split()
    cmd = subprocess.run(
        command, stdout=subprocess.PIPE
    )
    output = cmd.stdout.decode()
    print(cmd.stdout)
    print(output)

def run_ls_as_sudo():
    #pwd = getpass("password: ")
    command = "sudo -S ls -la".split()
    cmd = subprocess.run(
        command, stdout=subprocess.PIPE, encoding="ascii"
    )
    #output = cmd.stdout.decode()
    print(cmd.stdout)
    #print(output)


if __name__ == '__main__':
    #run_ls()
    run_ls_as_sudo()
    #cmd = subprocess.run(
    #    ls, stdout=subprocess.PIPE, input=getpass("password: "), encoding="ascii",
    #)
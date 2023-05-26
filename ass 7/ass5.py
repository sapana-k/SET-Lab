# import os

# def execute_command(command):
#     os.system(command)

# command = input("Enter a command to execute: ")
# execute_command(command)

import subprocess

def execute_command(command):
    subprocess.call(command.split())

command = input("Enter a command to execute: ")
execute_command(command)

# import subprocess

# command = "ls -l"
# output = subprocess.check_output(command.split())
# print(output.decode())
# MalPython
# PyCon APAC 2024
#
# Example of Python code as payload
# Run simple shell command

import subprocess

# simple command as sample
COMMAND = r"whoami"

# spawn new process for each command
def run(cmd):
    result = subprocess.Popen(
        cmd, 
        shell=True, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, 
        close_fds=True)
    output = result.stdout.read()
    return output

# run the command and print the result
print(run(COMMAND))
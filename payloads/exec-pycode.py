# MalPython 
# PyCon APAC 2024
# 
# Compile string of python code and execute it

import platform 

# code snippet for executing (evaluate) python code

def payload():
    if platform.system().startswith("Linux"):
        code="print('malicious code for Linux')"
        eval(compile(code, "<string>", "exec"))
    elif platform.system().startswith("Windows"):
        code="print('malicious code for Windows')"
        eval(compile(code, "<string>", "exec"))

payload()
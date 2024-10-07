# Malicious Module Example

This module is used to demonstrate common tricks by threat actor to masquerade malicious code.

Cython is used to convert python code into shared library (unix `.so` or windows `.pyd`).

## Malmod 2: Autoload (PYTHONSTARTUP)

A module is loaded automatically at runtime for each python invokation.

In this example we will use `PYTHONSTARTUP` environment variable that would notify python to load a file during invocation.

Note:
- the environment variable must be available.
- only applicable when running interactive python.

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

Edit the [config.py](config.py) and replace `PAYLOAD_PATH` to the path of the module.

add environment variable and point to the location of our `config.py` (ex: `/tmp/config.py`) then run the python.

```sh
export PYTHONSTARTUP="/tmp/config.py"
python3
```
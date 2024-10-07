# Malicious Package Example

This package is used to demonstrate common tricks by threat actor to masquerade malicious code.

## Malpkg 1: Malicious Module

Malicious code is inserted in package as separate module (file) or inside of existing module (file).

Possible triggers that can be used to execute the code:
- packages/modules import.
- certain function execution.
- event or exception handling (ie: HTTP 404 error).

In this example, our payload is python code that will be execute during import.

## Usage

To test locally, use following command for building and installing

```sh
python3 setup.py sdist
pip install dist/malpkg1-0.1.0.tar.gz
```

and then import the package

```python
import malpkg1
```
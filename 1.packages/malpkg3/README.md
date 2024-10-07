# Malicious Package Example

This package is used to demonstrate common tricks by threat actor to masquerade malicious code.

## Malpkg 3: Malicious Setup (Install Hook)

Malicious code is inserted into `setup.py` file.

The code will be executed as part of installation process by package manager (ie: pip). Specifically, it create an install hook that will be executed during installation.

The base64-encoded payload is a command that will be executed as subprocess.

## Usage

To test locally, use following command for building and installing

```sh
python3 setup.py sdist
pip install dist/malpkg3-0.1.0.tar.gz
```

check for the existence of file `result.txt`.
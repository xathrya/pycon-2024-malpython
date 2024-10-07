# Malicious Modules

Tricks to execute malicious code by masquerading into python modules.

The purpose of this approach is mostly to gain persistence or accessing the compromised machine after exploitation.

Some of the samples will use Cython to create shared library that will host malicious python code.

Content:
- `Malmod 1 - Autoload (Site Customize)`: create file that will be automatically loaded for each python invokation.
- `Malmod 2 - Autoload (PYTHONSTARTUP)`: set environment variable to script that will load or execute payload.
- `Malmod 3 - Autoload (Site)`: add code in `site.py` which will load the malicious python code.
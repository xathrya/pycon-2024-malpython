# Malicious Interpreter

Tricks to execute malicious code which inserted into the python binary. This section focus on modification of the Python source code.

The purpose of this approach is mostly to gain persistence or accessing the compromised machine after exploitation.

The sample will use `Python 3.11.9` as base code and each sample contain patch file, which should be applied to the source code.

Content:
- `Malinterp 1 - Retrieve Environment Variables`: retrieve all environment variables and just print.
- `Malinterp 2 - Run Payload on New Thread`: spawn new thread and execute the payload on that code.
- `Malinterp 3 - Run Python Code`: embed python code and execute it.
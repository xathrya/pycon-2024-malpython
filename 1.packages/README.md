# Malicious Packages

Tricks to execute malicious code by masquerading into python packages.

The purposes of this approach is mostly to compromising developer or end-user, by tricking them to install malicious packages directly or indirectly.

Content:
- `Malpkg1 - Malicious Module`: insert code into package that would be imported or used as dependency by other packages/modules.
- `Malpkg2 - Malicious Setup`: insert code into `setup.py` and execute it during installation
- `Malpkg3 - Malicous Setup (Hook)`: insert code into `setup.py` and hook into function for installation.

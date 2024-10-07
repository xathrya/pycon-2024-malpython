from setuptools.command.install import install 
import subprocess
import setuptools 
import base64
import json
import os 

# malicious code in install hook
class PyInstall(install):
    # PAYLOAD: run command
    def run(self):
        cmd = base64.b64decode("ZWNobyAnUHlDb24gQVBBQyAyMDI0JyA+IHJlc3VsdC50eHQ7IGlkID4+IHJlc3VsdC50eHQK")
        res = subprocess.Popen (
            cmd, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT
        ).stdout.read().decode()

        # continue the flow
        install.run(self)


setuptools.setup(
    name="malpkg3",
    version="0.1.0",
    author="Satria Ady Pradana",
    description="Simple package to demonstrate malicious package",
    packages=setuptools.find_packages(),
    cmdclass={
        "install": PyInstall,
    },
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
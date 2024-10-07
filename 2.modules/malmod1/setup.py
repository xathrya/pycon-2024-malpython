# Building the cython module

from setuptools import setup 
from Cython.Build import cythonize 

setup(
    ext_modules = cythonize("payload.pyx")
)
import setuptools 

setuptools.setup(
    name="malpkg1",
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
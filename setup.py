
from setuptools import setup, find_packages

setup(
    name="lockpdf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyPDF2>=1.26.0",  # Ensure you specify correct version requirements
    ],
    entry_points={
        "console_scripts": [
            "lockpdf=lockpdf.lockpdf:main",  # 'lockpdf' command will call 'main' function in 'lockpdf.py'
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple tool to encrypt PDF files",
    keywords="PDF encrypt",
)
    
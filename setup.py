from setuptools import setup, find_packages

setup(
    name='lockPDF',
    version='0.1.0',
    author='Majix',
    author_email='',
    description='A command-line tool to encrypt PDF files using AES encryption.',
    long_description='This package provides a command-line tool to securely encrypt PDF files with a password, using AES encryption provided by the pikepdf library.',
    packages=find_packages(),
    install_requires=[
        'pikepdf',
    ],
    entry_points={
        'console_scripts': [
            'lockpdf=encrypt.encrypt_pdf:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security :: Cryptography',
    ],
    python_requires='>=3.7',
)

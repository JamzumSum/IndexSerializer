# setup.py
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='indexserial',
    version='1.1.0',
    description='Serialize objects and allow random reading.',
    author='JamzumSum',
    author_email='zzzzss990315@gmail.com',
    install_requires=[
        'torch',
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)

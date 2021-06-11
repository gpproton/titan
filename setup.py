#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="titan",
    version="0.01",
    description="An easy to use python background task scheduler",
    long_description=read("README.md"),
    author="Godwin peter .O",
    author_email="me@godwin.dev",
    url="hhttps://github.com/TolaramGroup/titanProject/",
    license="MIT",
    platforms=["windows", "osx", "linux"],
    packages=["titan"],
    python_requires=">=3.6.2",
    package_dir={"": "."},
    package_data={},
    install_requires=[
        "click",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "titan=titan:main",
        ]
    },
)

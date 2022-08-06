#!/usr/bin/env python
import os
from setuptools import setup
from titan.common.defaults import constant


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name=constant.project_name,
    version=constant.project_version,
    description=constant.project_description,
    long_description=read("README.md"),
    author=constant.project_author,
    author_email=constant.project_author_email,
    url=constant.project_url,
    license=constant.project_license,
    platforms=["windows", "osx", "linux"],
    packages=[constant.project_name],
    python_requires=">=3.6",
    package_dir={"": "."},
    package_data={},
    install_requires=[
        # "click",
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

#!/usr/bin/env python
import os
from setuptools import setup
from titan.common.Default import Constant


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name=Constant.project_name,
    version=Constant.project_version,
    description=Constant.project_description,
    long_description=read("README.md"),
    author=Constant.project_author,
    author_email=Constant.project_author_email,
    url=Constant.project_url,
    license=Constant.project_license,
    platforms=["windows", "osx", "linux"],
    packages=[Constant.project_name],
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

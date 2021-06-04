#!/usr/bin/env python
import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='Titan',
      version='0.01',
      description='An easy to use python background task scheduler',
      long_description=read('README.md'),
      author='Godwin peter .O',
      author_email='me@godwin.dev',
      url='hhttps://github.com/TolaramGroup/titanProject/',
      license='MIT',
      platforms=['windows', 'osx', 'linux'],
      packages=['titan', 'titan.command'],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    )
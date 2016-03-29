#!/usr/bin/env python
# coding=utf-8
# this project is used to learn how to program a python project, and how the stucture of a 
# python project looks like.
# @author:james. lengjiabing@gmail.com
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'James\' project, initiation.',
    'author': 'James, Leng Jiabing',
    'url' : 'github.com',
    'version' : '1.0.0'
}

setup(**config)

#!/usr/bin/python
# Filename: second_hello.py

import second_module
second_module.hello()

from second_module import hello
hello()

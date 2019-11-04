#!/usr/bin/python
# Filename: ex_local.py

x = 50
def func(x):
    print('x is ', x)
    x = 2
    print('Changed local x to ', x)

func(x)
print('Value of x is ', x)

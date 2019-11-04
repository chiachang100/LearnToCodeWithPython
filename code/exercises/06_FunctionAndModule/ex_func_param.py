#!/usr/bin/python
# Filename: ex_func_param.py

def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

if __name__ == "__main__":
    printMax(3, 4) # directly give literal values

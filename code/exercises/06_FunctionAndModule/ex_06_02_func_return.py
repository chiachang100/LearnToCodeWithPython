#!/usr/bin/python
# Filename: ex_func_return.py

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

if __name__ == "__main__":
    print(maximum(2, 3))

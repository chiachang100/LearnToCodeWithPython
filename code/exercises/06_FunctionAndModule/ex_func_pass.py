#!/usr/bin/python
# Filename: ex_func_pass.py

def maximum(x, y):
    if x > y:
        return x
    else:
        pass

if __name__ == "__main__":
    print(maximum(2, 3))

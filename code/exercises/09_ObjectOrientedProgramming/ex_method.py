#!/usr/bin/python
# Filename: ex_method.py

class Person:
    def sayHi(self):
        print('Hello, how are you?')

#
if __name__ == "__main__":
    p = Person()
    p.sayHi()
    # This short example can also be written as Person().sayHi()

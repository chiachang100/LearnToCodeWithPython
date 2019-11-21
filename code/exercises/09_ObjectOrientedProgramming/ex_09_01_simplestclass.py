#!/usr/bin/python
# Filename: ex_simplestclass.py

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

#
if __name__ == "__main__":
    ben = Person('Ben', 10)
    print(ben.name, ben.age)

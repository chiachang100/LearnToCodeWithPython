#!/usr/bin/python
# Filename: ex_person.py

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

#
if __name__ == "__main__":
    ben = Person("Ben", 26)
    print("Before the birthday, {0}'s age is {1}.".format(ben.name, ben.age))
#
    ben.birthday()
    print("After the birthday, {0}'s age is {1}.\n".format(ben.name, ben.age))

#
    mary = Person("Mary", 15)
    print("Before the birthday, {0}'s age is {1}.".format(mary.name, mary.age))
#
    mary.birthday()
    print("After the birthday, {0}'s age is {1}.\n".format(mary.name, mary.age))

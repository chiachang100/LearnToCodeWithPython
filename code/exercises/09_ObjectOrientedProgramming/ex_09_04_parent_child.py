#!/usr/bin/python
# Filename: ex_person.py

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = self.age + 1

class Parent(Person):
    def __init__(self, name, age):
        Person.__init__(self,name,age)
        self.children = []

    def add_child(self,child):
        self.children.append(child)

    def print_children(self):
        print("The children of ", self.name, " are:")
        for child in self.children:
            print(child.name)

#=================================================================
if __name__ == "__main__":
    parent = Parent("Parent", 36)
    print("{0}'s age is {1}.".format(parent.name, parent.age))

    #
    daughter = Person("Daughter", 10)
    print("{0}'s age is {1}.".format(daughter.name, daughter.age))
    #
    son = Person("Son", 8)
    print("{0}'s age is {1}.\n".format(son.name, son.age))

    # add children
    parent.add_child(daughter)
    parent.add_child(son)

    #
    parent.print_children()


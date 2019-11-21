#!/usr/bin/python
# Filename: ex_using_tuple.py
#
# Tuples are immutable, and their elements are usually heterogeneous and are accessed via unpacking or indexing.
#

shoptuple = ('apple', 'mango', 'carrot', 'banana')
for item in shoptuple:
    print(item, end=' ')

print('My shopping list is: ', shoptuple)

#shoptuple[0] = 'strawberry'

#=============================================
person = ("Simon", 180.0, 35)
person[0]

person[1]

# Convert a sequence to a tuple
#x = tuple(y) #error
x = tuple(person)

#=============================================
# An empty tuple
myempty = ()
print('myempty = ', myempty)

# Single item
singleton = (2, )
print('singleton = ', singleton)

#
zoo = ('python', 'elephant', 'penguin') # remember the parentheses are optional
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
len(new_zoo)-1+len(new_zoo[2]))

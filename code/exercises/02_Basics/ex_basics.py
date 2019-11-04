#!/usr/bin/python
# Filename: ex_basics.py

# Numbers
spam = 10
fp = 10.50

import math
degrees = 45
radians = degrees / 360.0 * 2 * math.pi

10 + 15
print(10+15)
print(10+15+5)
print(10+15+5+100)

# Variables and Values
fizz = 10
eggs = 15
print('fizz =', fizz)
print('eggs =', eggs)
spam = fizz + eggs
print('spam =', spam)

spam = spam + 5
print('spam =', spam)

spam += 100
print('spam =', spam)

# Values Have Type
type(spam)

# What type is a?
a = 100
print(type(a))
a = "100"
print(type(a))
a = list()
print(type(a))
a = "100"
print(type(a))
a = 100
type(a)
print(type(a))

# What type is x?
from random import random
if random() > 0.5:
    x = 3.1415
else:
    x = "pi"

print(x)
print(type(x))

# What type is c?
a = 100
print(type(a))
b = "100"
print(type(b))
c = a + int(b)
print(type(c))

# Other surprises...
print("abc" * 10)

print(5 / 2)
print(5 // 2) # floor
print(5 / 2.0)

print(2 + 2j)

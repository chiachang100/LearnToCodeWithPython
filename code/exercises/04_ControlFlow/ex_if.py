#!/usr/bin/python
# Filename: ex_if.py

color = 'white'
print("In the beginning, the color is {0}.".format(color))
if color == 'red':
    color = 'orange'
elif color == 'orange':
    color = 'yellow'
else:
    color = 'red'

print("At the end, the color is {0}.".format(color))

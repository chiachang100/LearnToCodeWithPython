#!/usr/bin/python
# Filename: ex_temperature_converter_v2.py

celsius = 20
fahrenheit = (celsius * 9 / 5) + 32
print(fahrenheit)
#print("celsius = " + celsius + ", fahrenheit = " + fahrenheit)
print("celsius = " + str(celsius) + ", fahrenheit = " + str(fahrenheit))
print("celsius = %d, fahrenheit = %f" % (celsius, fahrenheit))
print("celsius = {0}, fahrenheit = {1}".format(celsius, fahrenheit))

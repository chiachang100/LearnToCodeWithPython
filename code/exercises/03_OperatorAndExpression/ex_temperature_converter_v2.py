#!/usr/bin/python
# Filename: ex_temperature_converter_v2.py

celsius = int(input("Enter celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("celsius = {0}, fahrenheit = {1}".format(celsius, fahrenheit))

#fahrenheit = 68
celsius = (fahrenheit - 32) * 5 / 9
print("fahrenheit = {0}, celsius = {1}".format(fahrenheit, celsius))

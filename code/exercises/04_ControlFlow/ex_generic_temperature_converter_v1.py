#!/usr/bin/python
# Filename: ex_temperature_converter_v2.py

choice = input("Enter choice of 'c2f' or 'f2c' : ")
temperature = int(input("Enter temperature: "))

if choice == 'c2f':
    # convert celsius to fahrenheit
    celsius = temperature
    fahrenheit = (celsius * 9 / 5) + 32
    print("celsius = {0}, fahrenheit = {1}".format(celsius, fahrenheit))
elif choice == 'f2c':
    # convert fahrenheit to celsius
    fahrenheit = temperature
    celsius = (fahrenheit - 32) * 5 / 9
    print("fahrenheit = {0}, celsius = {1}".format(fahrenheit, celsius))
else:
    print("Invalid choice: " + choice)

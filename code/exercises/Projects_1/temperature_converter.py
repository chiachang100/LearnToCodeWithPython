#!/usr/bin/python
# Filename: temperature_converter.py

choice = input("Enter choice of 'c2f' or 'f2c' : ")
temperature = int(input("Enter temperature: "))

def celsiusToFahrenheit(temperature):
    celsius = temperature
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheitToCelsius(temperature):
    fahrenheit = temperature
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

#
if __name__ == "__main__":
    if choice == 'c2f':
        # convert celsius to fahrenheit
        celsius = temperature
        fahrenheit = celsiusToFahrenheit(temperature)
        print("celsius = {0}, fahrenheit = {1}".format(celsius, fahrenheit))
    elif choice == 'f2c':
        # convert fahrenheit to celsius
        fahrenheit = temperature
        celsius = fahrenheitToCelsius(temperature)
        print("fahrenheit = {0}, celsius = {1}".format(fahrenheit, celsius))
    else:
        print("Invalid choice: " + choice)

#!/usr/bin/python
# Filename: ex_func_default.py

def say(message, times = 1):
    print(message * times)

if __name__ == "__main__":
    say('Hello')
    say('World', 5)

#!/usr/bin/python
# Filename: ex_continue.py

while True:
    s = (input('Enter something: '))
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too short: ', len(s))
        continue
    print('Input is too long: ', len(s))

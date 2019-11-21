#!/usr/bin/python
# Filename: myinput.py

f = open('myinput.py')
while True:
  line = f.readline()
  if len(line) == 0: # EOF
    break
  print(line, end='')
f.close()

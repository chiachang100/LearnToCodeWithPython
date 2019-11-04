#!/usr/bin/python
# Filename: ex_using_with.py

with open("poem.txt") as f:
    for line in f:
        print(line, end='')

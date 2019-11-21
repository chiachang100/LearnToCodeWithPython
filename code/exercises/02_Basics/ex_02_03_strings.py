#!/usr/bin/python
# Filename: ex_strings.py

#=====================================================
# Single Quotes
#=====================================================
msg = 'Quote me on this'
print('msg = ', msg)

#=====================================================
# Double Quotes work exactly as single quotes
#=====================================================
msg = "What's your name?"
print('msg = ', msg)

#=====================================================
# Triple Quotes (""" or ''')
#=====================================================
msg = '''This is the first line.
This is the second line.
'''
print('msg = ', msg)

#=====================================================
# Escape
#=====================================================
print('What\'s your name?')
print('What\'s your name?')
print("Newlines are indicated by \n")

#=====================================================
# Raw Strings
#=====================================================
print(r"Newlines are indicated by \n")

print(R"Newlines are indicated by \n")

#=====================================================
# Concatenate Strings
#=====================================================
print('Hello, ' + 'World!')

#=====================================================
# Two string literals side by side, they are automatically concatenated by Python
#=====================================================
print('What\'s ' 'your name?')

#=====================================================
# Multiplying Strings
#=====================================================
print(10 * 'a')

#=====================================================
# Strings Format
#=====================================================
age = 25
name = 'John'

#=====================================================
# Error
#=====================================================
print(name + " is " + age + " years old.")

print(name + " is " + str(age) + " years old.")

print("%s is %d years old." % (name, age))

print("{0} is {1} years old.".format(name, age))

#=====================================================
# Keeping Text in Strings (0-based index)
#=====================================================
print("abcde"[0])
print("abcde"[1])
#print("abcde"[10])

print("abcde"[1:3])
print("abcde"[:3])
print("abcde"[3:])

print(len("abcde"))
print("abc" + "def")

#=====================================================
# Strings are also objects and have methods.
#=====================================================
name = 'Python'

if name.startswith('Py'):
  print('Yes, the string starts with “Py"')

if 't' in name:
  print('Yes, it contains the string "t"')

if name.find('thon') != -1:
  print('Yes, it contains the string "thon"')

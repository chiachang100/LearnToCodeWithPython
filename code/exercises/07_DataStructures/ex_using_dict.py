#!/usr/bin/python
# Filename: ex_using_dict.py

ab = { 'John' : 'jdoe@acme.com',
  'Tony' : 'tsmith@acme.com'
}

ab['John']
ab['John'] = 'jdoe@live.com'

#=======================================
x = { "Rank": 7, "Score": 93.4 }

"Rank" in x

x["Rank"]

# Try x.keys(), x.values(), and x.items()

#=======================================
# 'ab' is short for 'a'ddress'b'ook

ab = { 'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
    }

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab: # OR ab.has_key('Guido')
    print("\nGuido's address is", ab['Guido'])

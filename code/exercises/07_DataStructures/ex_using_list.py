#!/usr/bin/python
# Filename: ex_using_list.py
#
# List holds an ordered collection of items enclosed in square brackets.
# Lists are mutable, and their elements are usually homogeneous and are accessed via iteration.
#

def printList():
    print('These items are:', end=' ')

    for item in shoplist:
        print(item, end=' ')

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

printList()

shoplist = ['strawberry', 'mango', 'carrot', 'banana']

# Modify an element
shoplist[0] = 'strawberry'
printList()

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

#===================================
list1 = [1, 2, 3, 4]
list2 = ['I ate chocolate', 'and want more']
list3 = list1 + list2
print(list3)

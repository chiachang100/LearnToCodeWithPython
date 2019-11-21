#!/usr/bin/python
# Filename: ex_set.py

x = {1, 3, 3, 5, 7}
# or set([1, 3, 3, 5, 7])
3 in x

x

len(x)

#============================================
bri = set(['brazil', 'russia', 'india'])
print('india' in bri)

print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))

bri.remove('russia')
print(bri & bric) # OR bri.intersection(bric)

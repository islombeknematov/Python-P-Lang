"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable
    and do not allow duplicates(Duplicate values will overwrite
                                               existing values).
"""
dictionary = {
    "Brand": 'BMW',
    "Model": 'X6',
    'Horse Power': 1000
}

<<<<<<< HEAD
print(dictionary['Model'])
print(dictionary.items())     # returns each item in a dictionary, as tuples in a list.

a = dictionary.get('Brand')
print(a)

print(dictionary.keys())
print(dictionary.values())

dictionary['Model'] = 'Mustang'   # UPDATING VALUE OF A DICTIONARY
print(dictionary)


dictionary['Color'] = 'Black'     # ADDING KEY VALUE TO A DICTIONARY
print(dictionary)

if "BMW" in dictionary.values():
    print('Yes it is')

dictionary.update({'Model': 23})
print(dictionary)
=======
# print(dictionary['Model'])
# print(dictionary.items())     # returns each item in a dictionary, as tuples in a list.

# a = dictionary.get('Brand')
# print(a)

# print(dictionary.keys())
# print(dictionary.values())

# dictionary['Model'] = 'Mustang'   # UPDATING VALUE OF A DICTIONARY
# print(dictionary)


# dictionary['Color'] = 'Black'     # ADDING KEY VALUE TO A DICTIONARY
# print(dictionary)

# if "BMW" in dictionary.values():
#     print('Yes it is')

# dictionary.update({'Model': 23})
# print(dictionary)
>>>>>>> 926687a (tasks.py file updated)







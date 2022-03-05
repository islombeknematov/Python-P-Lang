
"""
    Set - is an unordered, unindexed collection of unique elements,
          no duplicate members. Set items are unchangeable, but you
          can remove and/or add items.

    Ordered - When we say that tuples are ordered, it means that the
              items have a defined order, and that order will not change.
"""

<<<<<<< HEAD
str1 = {1, 2, 3, 4, 5}
str2 = {1, 2, 3, 6}

str1.add(6)
str1.clear()    # Removes all elements

str3 = str1.union(str1, str2)
print(str3)

str3 = str1.copy()      # Returns a shallow copy (no effect to org. copy)
print(str1)
str3.clear()
print(str1, str3)

str1.update('Hi')
str1.update(['sss'])
str1.update([11, 22])
print(str1)


print(str1.intersection(str2))   # Returns elements in both sets

print(str2.difference(str1))     # Returns elements in str2, which doesn't exist in str1


add - Add an element to a set.
     This has no effect if the element is already present.

clear  Remove all elements from this set.

copy     Return a shallow copy of a set.

difference - Return the difference of two or more sets as a new set.
     (i.e. all elements that are in this set but not the others.)


difference_update  - Remove all elements of another set from this set.

discard -            Remove an element from a set if it is a member.
                        If the element is not a member, do nothing.


intersection -       Return the intersection of two sets as a new set.
                    (i.e. all elements that are in both sets.)

intersection_update - Update a set with the intersection of itself and another.


isdisjoint - Return True if two sets have a null intersection.

issubset - Report whether another set contains this set.

issuperset - Report whether this set contains another set.

pop - Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.


remove - Remove an element from a set; it must be a member.
           If the element is not a member, raise a KeyError.


symmetric_difference - Return the symmetric difference of two sets as a new set.
           (i.e. all elements that are in exactly one of the sets.)

symmetric_difference_update - Update a set with the symmetric difference of itself and another

union - Return the union of sets as a new set
         (i.e. all elements that are in either set.)

update - Update a set with the union of itself and others.
=======
# str1 = {1, 2, 3, 4, 5}
# str2 = {1, 2, 3, 6}

# str1.add(6)
# str1.clear()    # Removes all elements

# str3 = str1.union(str1, str2)
# print(str3)

# str3 = str1.copy()      # Returns a shallow copy (no effect to org. copy)
# print(str1)
# str3.clear()
# print(str1, str3)

# str1.update('Hi')
# str1.update(['sss'])
# str1.update([11, 22])
# print(str1)


# print(str1.intersection(str2))   # Returns elements in both sets

# print(str2.difference(str1))     # Returns elements in str2, which doesn't exist in str1


# add - Add an element to a set.
#      This has no effect if the element is already present.

# clear  Remove all elements from this set.

# copy     Return a shallow copy of a set.

# difference - Return the difference of two or more sets as a new set.
#      (i.e. all elements that are in this set but not the others.)


# difference_update  - Remove all elements of another set from this set.

# discard -            Remove an element from a set if it is a member.
#                         If the element is not a member, do nothing.


# intersection -       Return the intersection of two sets as a new set.
#                     (i.e. all elements that are in both sets.)

# intersection_update - Update a set with the intersection of itself and another.


# isdisjoint - Return True if two sets have a null intersection.

# issubset - Report whether another set contains this set.

# issuperset - Report whether this set contains another set.

# pop - Remove and return an arbitrary set element.
#         Raises KeyError if the set is empty.


# remove - Remove an element from a set; it must be a member.
#            If the element is not a member, raise a KeyError.


# symmetric_difference - Return the symmetric difference of two sets as a new set.
#            (i.e. all elements that are in exactly one of the sets.)

# symmetric_difference_update - Update a set with the symmetric difference of itself and another

# union - Return the union of sets as a new set
#          (i.e. all elements that are in either set.)

# update - Update a set with the union of itself and others.
>>>>>>> 926687a (tasks.py file updated)



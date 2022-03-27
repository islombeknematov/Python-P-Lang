"""
    Tuple - is an ordered, indexed, immutable collection of elements
            Allows duplicate elements
"""

# index()	Searches the tuple for a specified value and returns the position of where it was found

tpl = (1, 2, 3, 4, 5)
print(tpl.index(5))     # throws an error, if element doesn't exist

# count()	Returns the number of times a specified value occurs in a tuple

tpl = (1, 2, 3, 4, 5, 3, 4, 5, 4, 4)
print(tpl.count(5))    # returns 0, if element doesn't exist
                       # else return the number of elements



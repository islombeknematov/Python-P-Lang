
"""
    Lambda - is a small anonymous function, can take any number of
             arguments but can only have 1 expression
"""


<<<<<<< HEAD
                    SIMPLE FUNCTION
def square(n):
    return n ** 2
print(square(5))

                    LAMBDA FUNCTION
square = lambda n: n ** 2
print(square(5))

gth = lambda a, b: a if a > b else b
print(gth(5, 4))
=======
#                     SIMPLE FUNCTION
# def square(n):
#     return n ** 2
# print(square(5))

#                     LAMBDA FUNCTION
# square = lambda n: n ** 2
# print(square(5))

# gth = lambda a, b: a if a > b else b
# print(gth(5, 4))
>>>>>>> 926687a (tasks.py file updated)
from functools import reduce

"""
    Filter - returns an iterator where the items are filtered through 
             a function to test if the item is accepted or not.
    filter(function, iterable)
"""
<<<<<<< HEAD
                                With Simple Function
nums = [1, 5, 3, 6, 4, 8, 0, 9]
def is_even(n):
    return n % 2 == 0

evens = filter(is_even, nums)
print(list(evens))

                                With Lambda Function
nums = [1, 2, 3, 4, 5]
def is_odd(n):
    return n % 2 == 1

odds = filter(lambda n: n % 2 == 1, nums)
print(list(odds))
=======
#                                 With Simple Function
# nums = [1, 5, 3, 6, 4, 8, 0, 9]
# def is_even(n):
#     return n % 2 == 0

# evens = filter(is_even, nums)
# print(list(evens))

#                                 With Lambda Function
# nums = [1, 2, 3, 4, 5]
# def is_odd(n):
#     return n % 2 == 1

# odds = filter(lambda n: n % 2 == 1, nums)
# print(list(odds))
>>>>>>> 926687a (tasks.py file updated)


"""
    Map - applies a given function to all the iterables and returns a new list
    map(function, iterables)
"""


<<<<<<< HEAD
def func(a, b):
    return a + b
x = map(func, ('apple', 'banana'), ('orange', 'pineapple'))
convert the map into a list, for readability:
print(list(x))                |
                            SAME
x = lambda a, b: a + b       # |
c = map(x,  ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(c))
=======
# def func(a, b):
#     return a + b
# x = map(func, ('apple', 'banana'), ('orange', 'pineapple'))
# convert the map into a list, for readability:
# print(list(x))                |
#                             SAME
# x = lambda a, b: a + b       # |
# c = map(x,  ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(list(c))
>>>>>>> 926687a (tasks.py file updated)


"""
    Reduce - applies a given function to the iterables and returns a single value
    reduce(function, sequence)
"""


<<<<<<< HEAD
lst = [1, 2, 3, 4, 5]

prod = reduce((lambda x, y: x * y), lst)
print(prod)
=======
# lst = [1, 2, 3, 4, 5]
#
# prod = reduce((lambda x, y: x * y), lst)
# print(prod)
>>>>>>> 926687a (tasks.py file updated)














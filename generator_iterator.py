"""
ITERATOR - is an object which uses iter() method to create
            an iterator containing an iterable objects (list, tuple, sets & etc.)
            and next() method to get next value of sequence.

GENERATOR - is a simple way of creating an iterator, and it
            is a function that produces or yields  sequence
            of values using yield method.
"""


<<<<<<< HEAD
                  ITERATOR

my_set = {'Apple', 'Banana', 'Cherry'}
new_set = iter(my_set)
print(next(new_set))
print(new_set.__next__())
print(new_set.__next__())
print(new_set.__next__())   # ERROR STOP ITERATION


my_list = iter(['Apple', 'Cherry', 'Banana'])
print(next(my_list))
print(my_list.__next__())


                  GENERATOR

def func():
    yield 1
    yield 2
    yield 3


new_f = func()

for i in func():
    print(i)
=======
#                   ITERATOR

# my_set = {'Apple', 'Banana', 'Cherry'}
# new_set = iter(my_set)
# print(next(new_set))
# print(new_set.__next__())
# print(new_set.__next__())
# print(new_set.__next__())   # ERROR STOP ITERATION


# my_list = iter(['Apple', 'Cherry', 'Banana'])
# print(next(my_list))
# print(my_list.__next__())


#                   GENERATOR

# def func():
#     yield 1
#     yield 2
#     yield 3


# new_f = func()

# for i in func():
#     print(i)
>>>>>>> 926687a (tasks.py file updated)

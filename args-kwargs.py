"""
    Both Python *args and **kwargs let you pass a several number
    of arguments into a function. *args have no keywords
    whereas **kwargs arguments each are associated with a keyword.
    It lets you pass arguments/keyword arguments to a function when
    you are unsure how many arguments/keyword arguments you want to pass.
"""

# *args


def student(name, *data):
    print(name)
    print(data)     # here *data returns tuple


student("Islombek", 20, 'Tashkent')
# def student(name, *data):
#     print(name)
#     print(data)     # here *data returns tuple
#
#
# student("Islombek", 20, 'Tashkent')


# **kwargs


def student(name, **data):
    print(name)
    print(data)     # here **data returns dict


student("Islombek", age=20, city='Tashkent')
# def student(name, **data):
#     print(name)
#     print(data)     # here **data returns dict


# student("Islombek", age=20, city='Tashkent')





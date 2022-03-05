
"""
GLOBAL - is a variable declared outside the function
    or in global scope. We can access a global variable
    inside and outside the function.

LOCAL - is a variable declared inside the function.
    We can access a local variable inside but not outside the function

NONLOCAL - is a variable used in nested functions whose local
    scope is not defined. Means that the variable exists neither
    in the local nor in the global scope.
"""

<<<<<<< HEAD
                    GLOBAL

x = 'global'

def func():
    print('x inside: ', x)

func()
print('x outside: ', x)


x = 'global '

def func():
    global x    # We can only access the global variable but
    x *= 2      # cannot modify it from inside the function.
    print(x)

func()


                    LOCAL

def func():
    x = 10
    print(x)

func()


                    NONLOCAL

def outer():
    x = 'local'

    def inner():
        nonlocal x  # We use nonlocal keywords to create nonlocal variables
        x = 'nonlocal'
        print('inner: ', x)

    inner()
    print('outer: ', x)


outer()
=======
#                     GLOBAL

# x = 'global'

# def func():
#     print('x inside: ', x)

# func()
# print('x outside: ', x)


# x = 'global '
#
# def func():
#     global x    # We can only access the global variable but
#     x *= 2      # cannot modify it from inside the function.
#     print(x)
#
# func()


#                     LOCAL

# def func():
#     x = 10
#     print(x)
#
# func()


#                     NONLOCAL

# def outer():
#     x = 'local'
#
#     def inner():
#         nonlocal x  # We use nonlocal keywords to create nonlocal variables
#         x = 'nonlocal'
#         print('inner: ', x)
#
#     inner()
#     print('outer: ', x)
#
#
# outer()
>>>>>>> 926687a (tasks.py file updated)




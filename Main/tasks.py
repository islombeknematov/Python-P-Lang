#      1.  Write a Python program to check if a given positive
#               integer is a power of two.
#
#
# power = int(input('Enter a number: '))
#
# while power > 0 and power % 2 == 0:
#     power = power / 2
#
# if power == 1:
#     print(True)
# else:
#     print(False)
#
# -------------------------------------------------------------------------
#
#         2.  Write a Python program to check if a given positive
#            integer is a power of three.
#
# n = int(input('Enter: '))
# while n > 0 and n % 3 == 0:
#     n /= 3
#
# if n == 1:
#     print(True)
# else:
#     print(False)
#
# -------------------------------------------------------------------------
#
#        3.  Fibonacci numbers
#
# fibo = int(input('Enter a number: '))
# n1 = 0
# n2 = 1
# count = 0

# while count < fibo:
#     next_n = n1 + n2
#     n1 = n2
#     n2 = next_n
#     count += 1

# print(next_n)
#
#
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#
# -------------------------------------------------------------------------
#
#       5.  Write a Python program that accepts an integer (n) and
#           computes the value of n+nn+nnn. Go to the editor
#           Sample value of n is 5
#           Expected Result : 615
#
#
# num = int(input('Enter n: '))
# a = str(num) * 2
# b = str(num) * 3
# print(num + int(a) + int(b))
#
#
# def number(n):
#     a, b = str(n) * 2, str(n) * 3
#     print(n + int(a) + int(b))
#
# number(5)
#
# -------------------------------------------------------------------------
#
#       6.  Given a year, return the century it is in. The first century spans from the year 1 up to
#           and including the year 100, the second - from the year 101 up to and including the year 200, etc.
#
# Example
#
# For year = 1905, the output should be
# solution(year) = 20;
# For year = 1700, the output should be
# solution(year) = 17.
#
# def solution(year):
#     if year % 100 == 0:
#         print(year // 100)
#     elif year % 100 != 0:
#         print(year // 100 + 1)
#
# solution(2001)
#
# -------------------------------------------------------------------------
#
#       7.  Given the string, check if it is a palindrome.
#
# def palindrome(my_str):
#     if my_str[:] == my_str[::-1]:
#         return True
#     return False
#
# print(palindrome('aabbaa'))
#
# -------------------------------------------------------------------------
#
#       8.  Given an array of integers, find the pair of adjacent
#           elements that has the largest product and return that product.
#
#                             SOLUTION MINE
# def solution(inputArray):
#     container = []
#     result = []
#     for i in range(len(inputArray) - 1):
#         container.append(inputArray[i] * inputArray[i + 1])
#
#     for j in range(len(container) - 1):
#         if container[j] > container[j + 1]:
#             result.append(container[j])
#             container[j], container[j + 1] = container[j + 1], container[j]
#
#         else:
#             if len(result) != 0:
#                 result.pop(0)
#                 result.append(container[j + 1])
#             else:
#                 result.append(container[j + 1])
#     print(container[-1])
#
#
# solution([3, 6, -2, -5, 7, 3])
#
#                                 SOLUTION -> OTHERS
# def solution(inputArray):
#     return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
#
# print(solution([3, 10, -2, -5, 7, 3]))
#
# -------------------------------------------------------------------------
#
# <<<<<<< HEAD
#      1.  Write a Python program to check if a given positive
# =======
#      9.  Write a Python program to check if a given positive
# >>>>>>> 926687a (tasks.py file updated)
#               integer is a power of two.
#
# def power(number):
#     if number > 2:
#         while number > 0 and number % 2 == 0:
#             number /= 2
#
#         if number == 1:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(False)
#
#
# numbers = int(input('Enter: '))
# <<<<<<< HEAD
# # power(numbers)
#
#
#
# =======
# power(numbers)
#
# ------------------------------------------------------------------
#
#            10. Given an array of integers nums and an integer target, return
#            indices of the two numbers such that they add up to target.
#
# def two_sum(nums, target):
#     for i in range(len(nums)-1):
#         if nums[i] + nums[i + 1] == target:
#             print('Numbers: ', nums[i], nums[i + 1])
#             print('Indices: ', i, i + 1)
#         else:
#             continue
#
#
# two_sum([2, 7, 11, 15], int(input('Enter target: ')))
#
# ----------------------------------------------------------------------
#
#               11. Below we will define an n-interesting polygon. Your task is to find
#                   the area of a polygon for a given n.
#
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting
# polygon is obtained by taking the n - 1-interesting polygon and appending
# 1-interesting polygons to its rim, side by side. You can see
# the 1-, 2-, 3- and 4-interesting polygons in the picture below.
#
# https://codesignal.s3.amazonaws.com/tasks/shapeArea/img/area.png?_tm=1624642306583
#
# Example
#
# For n = 2, the output should be
# solution(n) = 5;
# For n = 3, the output should be
# solution(n) = 13.
#
#                       Source code
#
# def solution(n):
#   return n ** 2 + (n - 1) ** 2
#          or
#   return 2 * n * (n - 1) + 1
#          or
#     result = 1
#     for i in range(n):
#         result += 4 * i
#     return result
#
#
# print(solution(15))
#
#
#

#               12. Given an array of integers nums and an integer target, return indices of the two numbers
#               such that they add up to target.
#               You may assume that each input would have exactly one solution, and you
#               may not use the same element twice.

#                                 MY SOLUTION
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i, len(nums) - 1):
#             if nums[i] + nums[j + 1] == target:
#                 return i, j + 1
#             else:
#                 continue
#
#
# print(two_sum([2, 5, 5, 11], int(input('Enter target: '))))


#                   OTHERS SOLUTION


# def two_sum(nums, target):
#     seen = {}
#     for i, value in enumerate(nums):
#         remaining = target - nums[i]
#         if remaining in seen:
#             return [i, seen[remaining]]
#         seen[value] = i
#
#
# print(two_sum([2, 5, 5, 11], int(input('Enter target: '))))



					# FIBONACCI WITH MEMOIZATION 
					# AN EFFICIENT WAY
# fib_cache = {}

# def fib(n):

# 	# if we have cached value, then return it
# 	if n in fib_cache:
# 		return fib_cache[n]

# 	# Compute the Nth term
# 	if n <= 2:
# 		value = 1
# 	else:
# 		value = fib(n - 1) + fib(n - 2)

# 	# Cache the value and return it
# 	fib_cache[n] = value
# 	return value


# for n in range(1, 11):
# 	print(n, fib(n))


# cache = {}
# def fib(n):
# 	if n in cache:
# 		return cache[n]

# 	elif n <= 2:
# 		result = 1

# 	elif n > 2:
# 		result = fib(n - 1) + fib(n - 2)

# 	cache[n] = result

# 	return result


# for n in range(1, 51):
# 	print(n, fib(n))



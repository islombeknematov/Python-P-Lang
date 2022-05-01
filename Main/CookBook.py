
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(line)
# print(uname, '--> uname')
# print(fields, '--> fields')
# print(homedir, '--> homedir')
# print(sh, '--> sh')


# record = ('ACME', 50, 123.45, (12, 18, 2012))
# name, *_, (*_, year) = record
# print(name)
# print(_)


# def func(a, *b, **c):
#     print(a)
#     print(b)
#     print(c)


# func(5, 6, 7, 8, s=4, d=6)


# def the_sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head


# print(the_sum([10, 7, 4, 5, 9]))


# from collections import deque


# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
#
#
# Example use on a file
#
# if __name__ == '__main__':
#     with open('somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-'*20)


# q = deque(maxlen=3)
# q.append(1)
# q.append(2)
# q.append(3)
# print(q)

# q.append(4)
# print(q)

# q.append(5)             # adds item to the right
# print(q)


# q.appendleft(9)         # adds item to the left
# print(q)


# print(q.popleft())
# print(q.pop())

# -----------------------------------------------------------------


import heapq


# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums))  # Prints[43, 37, 23]
# print(heapq.nsmallest(3, nums))  # Prints[-4, 1, 2]



# Both functions also accept a key parameter that allows them to be used with more
# complicated data structures. For example:

# portfolio = [
#  	{'name': 'IBM', 'shares': 100, 'price': 91.1},
#  	{'name': 'AAPL', 'shares': 50, 'price': 543.22},
#  	{'name': 'FB', 'shares': 200, 'price': 21.09},
#  	{'name': 'HPQ', 'shares': 35, 'price': 31.75},
#  	{'name': 'YHOO', 'shares': 45, 'price': 16.35},
#  	{'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]


# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# print(cheap)
# expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
# print(expensive)

# nums = [4, 3, 7, 2, 9, 1, 5, 0, 10, 6]
# heap = list(nums)
# heapq.heapify(heap)
# print(heap[4])


# 							Problem
# You want to implement a queue that sorts items by a given priority and always returns
# the item with the highest priority on each pop operation.


# class PriorityQueue:
# 	def __init__(self):
# 		self._queue = []
# 		self._index = 0

# 	def push(self, item, priority):
# 		heapq.heappush(self._queue, (-priority, self._index, item))
# 		self._index += 1

# 	def pop(self):
# 		return heapq.heappop(self._queue)[-1]


# class Item:
# 	def __init__(self, name):
# 		self.name = name 

# 	def __repr__(self):
# 		return 'Item ({!r})'.format(self.name)

# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# q.push(Item('grok'), 2)

# print(q.pop())
# print(q.pop())
# print(q.pop())



"""		Problem
You want to make a dictionary that maps keys to more than one 
value (a so-called “multidict”)
"""

from collections import defaultdict

# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
# print(d)

# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['b'].add(4)
# print(d)


# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(2)
# d.setdefault('b', []).append(4)



from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
	print(key, d[key])


import json
print(json.dumps(d))


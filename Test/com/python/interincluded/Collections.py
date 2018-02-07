# -*-coding:utf-8-*-

from collections import namedtuple, deque

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p
print isinstance(p, Point)

q = deque(['1', '2', '3'])
q.append('4')
q.appendleft('5')
print q

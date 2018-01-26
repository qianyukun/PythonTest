# -*- coding:utf-8 -*-
import math

print abs(100)
print abs(-20)
print abs(12.34)

print max(1, 2, 3, 4, 5, 6, 4, -12)
print min(1, 2, 3, 4, 5, 6, 4, -12)

print int('123')
print int(12.12)
print float('123.123')
print str(1.23)
print bool(1)
print bool('')

a = abs
print a(-1)

for i in list(range(8, 17, 1)):
    print hex(i)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print my_abs(-11)


def my_ads1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print my_ads1(-12.111)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx , ny

x,y = move(100,100,60,math.pi/6)
print x,y
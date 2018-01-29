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
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x, y


def quadratic(a, b, c):
    temp = math.pow(b, 2) - 4 * a * c
    if math.pow(b, 2) - 4 * a * c >= 0:
        x1 = (-b + math.sqrt(temp)) / (2 * a)
        x2 = (-b - math.sqrt(temp)) / (2 * a)
        return x1, x2
    return None


print quadratic(1, 5, 3)


def calc(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    return sum


# 可变参数
def calc1(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    return sum


print calc([1, 2, 3, 4])
print calc((1, 2, 3, 4, 5))
nums = [1, 2, 3, 4, 5, 6]
print calc1(*nums)


def persion(name, age, **extra):
    print name, age, extra


extra = {"job": "engineer"}
persion("jack", 12, **extra)


def f1(a, b, c=0, *args, **extra):
    print(a, b, c, args, extra)


f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', extra=3)
# -*- coding:utf-8 -*
# 遍历
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print value

from collections import Iterable

print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 2)]:
    print(x, y)

# 列表生成
print [x * x for x in list(range(1, 11, 1))]
print [x * x for x in list(range(1, 11, 1)) if x % 2 == 0]
print [m + n for m in 'AB' for n in 'CD']

import os

print [d for d in os.listdir('.')]

d = {'a': 1, 'b': 2, 'c': 3}
print [k + "=" + v.__str__() for k, v in d.items()]

s = ['Hello', 'World']
print [ss.lower() for ss in s]

# Generator
print [x for x in list(range(1, 5, 1))]
p = (x for x in list(range(1, 5, 1)))
print p
print p.next()
print p.next()
print p.next()


# 构造斐波那契数列的生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print fib(5)
p = fib(5)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

num = 12
pp = fib(num)
print 'start to print fib (%d)' % num
while True:
    try:
        x = next(pp)
        print x
    except StopIteration as e:
        print 'end'
        break


# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass
# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
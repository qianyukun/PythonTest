# -*-coding:utf-8-*-
def fun(a, b, f):
    return f(a) + f(b)


print fun(1, -2, abs)

# map

print list(map(str, [1, 2, 3, 4, 5, 6]))


def func(a):
    return a * a


print list(map(func, [1, 2, 3, 4, 5, 6]))


# reduce
def add(a, b):
    return a + b


def power(a):
    return a * a


print reduce(add, [1, 2, 3, 4])
print reduce(add, map(power, [1, 2, 3, 4]))


# filter
def is_odd(n):
    return n % 2 == 1


print list(filter(is_odd, [1, 2, 3, 4, 5, 6]))


def not_empty(s):
    return s and s.strip()


print list(filter(not_empty, ['a', '', ' ', None]))

# sorted
print sorted([1, 4, 3, 6, 2, 7, 8])
print sorted([12, 23, 123, 56, 87, 35, 23, -123], key=abs)

print sorted(['asd', 'qucaqwd', 'Afqwfacae', 'Zqawdexs'], key=str.lower)
print sorted(['asd', 'qucaqwd', 'Afqwfacae', 'Zqawdexs'], key=str.lower, reverse=True)

# test
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


print sorted(L, key=by_name)
print sorted(L, key=by_score)


# return function
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print lazy_sum(1, 2, 3, 4)
f = lazy_sum(1, 2, 3, 4)
print f()


# 闭包
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
        # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print f1()
print f2()
print f3()


# 匿名函数
def build(x):
    return lambda x: x * x


print build(12)
b = build(12)
print b(112)


# 装饰器
def now():
    print '2018-1-29'


f = now
f()


def log(func):
    def wrapper(*args, **kw):
        print 'call %s()' % func.__name__
        return func(*args, **kw)

    return wrapper


@log
def tomorrow():
    print '2018-1-30'


tomorrow()

import functools


def log1(text):
    def detect(function):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s call %s()' % (text, function.__name__)
            return function(*args, **kw)

        return wrapper

    return detect


@log1('excute')
def yestoday():
    print '2018-1-27'


yestoday()
print yestoday.__name__

# 偏函数
int2 = functools.partial(int, base=2)
print int2('1010')

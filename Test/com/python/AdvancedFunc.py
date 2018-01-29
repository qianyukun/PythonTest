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

# -*- coding: utf-8 -*-
age = 3
print "yout age is %d" % age
if age >= 18:
    print "adult"
elif age >= 6:
    print "teenager"
else:
    print "kid"

birth = input("input birth year: ")

if birth > 2000:
    print "00后"
elif birth > 1990:
    print "90后"
else:
    print "you are too old"

names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for num in [1, 2, 3, 4, 5, 6, 7]:
    print "+%d" % num
    sum += num
print sum

_sum = 0
for num in list(range(1, 99, 1)):
    _sum += num
print "sum from 0 to 100 , step 1,result is %d" % _sum

__sum = 0
n = 99
while n > 0:
    __sum += n
    n -= 1
    if n == 10:
        break
print "from 99 to 10,step 1,sum:%d" % __sum

i = 0
while i < 10:
    if i % 2 == 0:
        print '偶数 :%d' % i
    i += 1

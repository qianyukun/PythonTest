# -*- coding: utf-8 -*-
age = 3
print "yout age is %d" % age
if age >= 18:
    print "adult"
elif age >= 6:
    print "teenager"
else:
    print "kid"

birth = input("birth : ")

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
print "sum from 0 to 100 ,result is %d" % _sum

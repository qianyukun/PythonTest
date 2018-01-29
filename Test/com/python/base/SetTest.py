# -*- coding:utf-8 -*-
s = set([1, 2, 3])
print s

s = set([1, 1, 2, 3, 4, 5, 5, 5])
print "1, 1, 2, 3, 4, 5, 5, 5 to set :" + s.__str__()

s.add(2)
print "s.add(2): " + s.__str__()

s.add(6)
print "s.add(6):" + s.__str__()

s.remove(6)
print "after remove 6:" + s.__str__()

s1 = {1, 3, 5, 7}
s2 = {2, 4, 5, 6}
s3 = set(s1 | s2)
s4 = set(s1 & s2)
print "s1" + s1.__str__()
print "s2" + s2.__str__()
print "s1 | s2:" + s3.__str__()
print "s1 & s2:" + s4.__str__()

a = ['c', 'b', 'a']
print a
a.sort()
print "after sort :" + a.__str__()

b = 'aaaaaaaa'
print b
c=b.replace('a', 'A')
print "after replace a to A:" + c

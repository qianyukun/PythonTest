# -*- coding:utf-8 -*-
d = {'Micheal': 95, 'Bob': 75, 'Tracy': 78}
print "all dict items :" + d.__str__()
print "Micheal 's age :%d" % d['Micheal']

newPersonName = raw_input("input name of person you want to add :\n")
newPersonAge = input("input age of person you want to add\n")

d[newPersonName] = newPersonAge

print "after add ," + d.__str__()

if 'Jack' in d:
    print "Jack is in dict"
else:
    print "Jack is not in dict"

print "get (Mary) is " + d.get('Mary').__str__()

if d.get('Mary') is None:
    print 'null'
else:
    print d.get('Mary')

d.pop("Bob")
print "after pop Bob" + d.__str__()


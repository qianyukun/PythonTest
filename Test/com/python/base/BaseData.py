#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print "asd"
print ord('a')
print chr(66)

print b'ABC'.encode('ascii')

print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

print len('abc')

print len(b'asdasd')

print 'hello , %s here are %d apples' % ('alter',101)

print 'hello %d %%' % 7

classmates = ['Michael','Bob','Tracy']
print classmates
print len(classmates)

print classmates[0]
print ("get the last one :"+classmates[-1])
print ("get the last two : "+classmates[-2]+" , "+classmates[-1])

classmates.append("jack")

print ('after append Jack :')
print classmates

classmates.insert(0,'jack')
print "after insert Jack ："+classmates.__str__()

classmates.pop()
print "remove the last one "+classmates.__str__()

classmates.pop(1)
print "remove the second item "+classmates.__str__()

classmates[0] = 'reName'
print "rename first person "+classmates.__str__()

s = ['python','java',['asp','php'],'scheme']
print "list s's length is %d " % len(s)
print "list s is "+s.__str__()

_tuple = (1,2)
print "tuple is "+_tuple.__str__()

_tuple = (1)
print "_tuple = (1) this is not tuple "+_tuple.__str__()

_tuple = (1,)
print "tuple is "+_tuple.__str__()

_tuple = ()
print "tuple is "+_tuple.__str__()
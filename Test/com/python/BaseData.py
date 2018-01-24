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






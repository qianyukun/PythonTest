# -*- coding:utf-8-*-
import time
from datetime import datetime, timedelta

print datetime.now()
print type(datetime.now())

print datetime(2018, 3, 5)

dt = datetime.now()
print dt
print time.time()
print dt.utcfromtimestamp(time.time())
print datetime.fromtimestamp(time.time())

print "str to datetime " + datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S').__str__()

print "datetime to str " + datetime.now().strftime('%a, %b %d %H:%M').__str__()

print "datetime + -"

print datetime.now()+timedelta(days=1,hours=10)



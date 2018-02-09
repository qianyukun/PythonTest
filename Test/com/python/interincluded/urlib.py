# -*-coding:utf-8-*-
import urllib2
import urllib
import json

try:
    f = urllib2.urlopen('https://api.douban.com/v2/book/2129650')
    data = f.read()
    print f.info()
    # for k, v in f.headers:
    #     print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
finally:
    pass

# get
print '------------------'
req = urllib2.Request('https://api.douban.com/v2/book/2129650')
req.add_header("pasd","asd")
data = {"name":"JackBauer"}
req.add_data(json.dumps(data))
response = urllib2.urlopen(req)
print response.read()

# post
print '-----------------'
url = 'http://www.baidu.com'
response = urllib2.urlopen(url)
the_page = response.read()
print the_page



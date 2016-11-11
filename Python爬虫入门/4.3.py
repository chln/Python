#-*- coding: utf-8 -*-
import urllib, urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
values = {"username":"XXXXXX","password":"XXXXXX"}
headers = {'User-Agent':user_agent}
#headers = {'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
#           'Referer':'http://www.zhihu.com/articles'}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
print response.read()
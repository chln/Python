#-*- coding: utf-8 -*-
import urllib, urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
data = None
headers = {'User-Agent': 'Mozilla/4.0)'}
try:
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    print response.getcode()
    #print response.read().decode('utf-8')
except urllib2.URLError, e:
    print e
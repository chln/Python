#-*- coding: utf-8 -*-
import urllib, urllib2

values = {"username":"XXXXXX","password":"XXXXXX"}
data = urllib.urlencode(values)
url = r"https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
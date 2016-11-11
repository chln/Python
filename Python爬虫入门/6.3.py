#-*- coding: utf-8 -*-
import urllib2, cookielib

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard = True, ignore_expires = True)
#创建请求的request
req = urllib2.Request('http://www.baidu.com')
#创建handler用urllib2用urllib2.HTTPCookieProcessor方法
handler = urllib2.HTTPCookieProcessor(cookie)
#创建opener用urllib2.build_opener的方法
opener = urllib2.build_opener(handler)
response = opener.open(req)
print response.read()

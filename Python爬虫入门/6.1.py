#-*- coding: utf-8 -*-
import urllib2, cookielib

#声明一个CooKieJar对象实例保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过hander来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print "Name="+item.name
    print "Value="+item.value
#-*- coding: utf-8 -*-
import urllib, urllib2, cookielib

filename = 'coolie.txt'
#声明一个MozillaCoolieJar对象实例来保存cookie，之后写入文件
cookie = cookie.MozillaCookieJar(filename)
#创建handler用urllib2用urllib2.HTTPCookieProcessor方法
handler = urllib2.HTTPCookieProcessor(cookie)
#创建opener用urllib2.build_opener的方法
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({
                            'stuid':'201200131012',
                            'pwd','232332155'
                            })
#登陆教务系统的URL
loginUrl = 'Http://jwxt.stu.edu.cn:7890/pls/wwwbks/bks_login2.login'                    
#模拟登陆，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard = True, ignore_expires = True)
#利用coolie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网站
result = opener.open(gradeUrl)
print result.read()

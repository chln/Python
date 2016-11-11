# -*- coding:utf-8 -*-
import urllib, urllib2, re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
data = None
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
try:
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    #print response.read().decode('utf-8')
    content = response.read().decode('utf-8')
    pattern = re.compile(r'<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>(.*?)<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
                               #作者                                       内容        其他（包含图片url）    好笑度                        评论数    
    items = re.findall(pattern,content)
    for item in items:
            haveImg = re.search("img",item[2])
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,"\n",item[1])
                print u"作者：%s\n段子：%s\n好笑度：%s 评论数：%s\n\n"% (item[0].strip(), text.strip(), item[3].strip(), item[4].strip())
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
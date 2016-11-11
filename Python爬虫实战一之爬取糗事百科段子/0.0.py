#-*- coding: utf-8 -*-
import re
#print u'连接糗事百科失败,错误原因'
#print '连接糗事百科失败,错误原因'.decode('utf-8')
#print '连接糗事百科失败,错误原因'

string = r'nihao nihao'
pattern = r' '#空格也是可以匹配的
pat = re.compile(pattern)
ittems = re.findall(pat, string)
for ittem in ittems:
    print u'--'+ittem+u'--'
 
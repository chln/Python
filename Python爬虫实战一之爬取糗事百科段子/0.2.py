#-*- coding: utf-8 -*-
import re

string = r'   dfhadkhfk    hdfh<br/>fdfadfad    '
print '--'+string+'--'
rep = re.compile('<br/>')
ittems = re.sub(rep,"\n",string) #re.sub(pattern, replace, string)正则替代函数
print '--'+ittems.strip()+'--'
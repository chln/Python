#-*- coding:utf-8 -*- 
import re

key = r"http://fljdjf https://djfljsdj"
p1 = r"https*://"
#*跟在其他符号后面表达可以匹配到它0次或多次
#可能既有http://开头的，又有https://开头的
pattern1 = re.compile(p1)
print pattern1.findall(key)

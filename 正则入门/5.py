#-*- coding:utf-8 -*-
import re

key = r"fdhjf<hTml>hello</Html>fdfjdfjd"
p1 = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]>"
#[]代表匹配里面的字符中的任意一个
#在<html></html>这对标签上，大小写混用
pattern1 = re.compile(p1)
print pattern1.findall(key)
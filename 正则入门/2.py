#-*- coding:utf-8 -*-
import re

key = r"<h1>hello world<h1>"
p1 = r"<h1>.+<h1>"
#.字符在正则表达式代表着可以代表任何一个字符（包括它本身）
#+的作用是将前面一个字符或一个子表达式重复一遍或者多遍。
#比方说表达式“ab+”那么它能匹配到“abbbbb”，但是不能匹配到"a"
pattern1 = re.compile(p1)
print pattern1.findall(key)
#findall返回的是所有符合要求的元素列表，
#包括仅有一个元素时，它还是给你返回的列表。
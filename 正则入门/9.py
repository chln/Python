#-*- coding: utf-8 -*-
#假如你在写一个爬虫，你得到了一个网页的HTML源码。其中有一段html
#<html><body><h1>hello world</h1></body></html>
#你想要把这个hello world提取出来
import re

key = r"<html><body><h1>hello world</h1></body></html>"
#这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=</h1>)"
#这是我们写的正则表达式规则
#简单来说，就是你要匹配的字符是XX，但必须满足形式是AXXB这样的字符串，那么你就可以这样写正则表达式
#p = r"(?<=A)XX(?=B)"
#匹配到的字符串就是XX。并且，向前查找向后查找不需要必须同时出现。
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1, key)
print matcher1.group(0)
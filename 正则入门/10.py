#-*- coding:utf-8 -*-
import re

key = r"<h1>hello world</h3> <h2>hello world</h2> <h2>hello world</h3>"
p1 = r"<h([1-6])>.+</h([1-6])>"
p2 = r"<h([1-6])>.+</h\1>"
#看到\1了吗？原本那个位置应该是[1-6]
#在这里1表示第一个子表达式，也就是说，它是动态的，是随着前面第一个子表达式的匹配到的东西而变化的。比方说前面的子表达式内是[1-6]，在实际字符串中找到了1，那么后面的\1就是1，如果前面的子表达式在实际字符串中找到了2，那么后面的\1就是2。
pattern1 = re.compile(p1)
m1 = re.search(pattern1,key)
print m1.group(0)
pattern2 = re.compile(p2)
m2 = re.search(pattern2,key)
print m2.group(0)
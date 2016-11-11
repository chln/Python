#-*- coding: utf-8 -*-
import re

key = r"mat cat hat pat"
p1 = r"[^p]at"
#这代表除了p以外都匹配
#[^]代表除了内部包含的字符以外都能匹配
#cat,hat,mat,qat这个例子，我们想匹配除了qat以外的
pattern1 = re.compile(p1)
print pattern1.findall(key)
#正则表达式	代表的匹配字符
#[0-9]	0123456789任意之一
#[a-z]	小写字母任意之一
#[A-Z]	大写字母任意之一
#\d 	等同于[0-9]
#\D 	等同于[^0-9]匹配非数字
#\w 	等同于[a-z0-9A-Z_]匹配大小写字母、数字和下划线
#\W 	等同于[^a-z0-9A-Z_]等同于上一条取非
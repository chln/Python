#-*- coding: utf-8 -*-

import re

pattern = re.compile(r'\d+')
#将正则表达式编译成pattern对象，注意hello前面的r的意思是“原生字符串”
result1 = re.split(pattern, 'hello world!')

print result1
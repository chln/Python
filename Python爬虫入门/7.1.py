#-*- coding: utf-8 -*-

import re

pattern = re.compile(r'hello')
#将正则表达式编译成pattern对象，注意hello前面的r的意思是“原生字符串”
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

print result1.group(), result2.group(0), result4.group()#result3.group(), #
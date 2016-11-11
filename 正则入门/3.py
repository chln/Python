#-*- coding:utf-8 -*-
import re

key = r"adifkdjafjasjdchulin@hit.edu.cndhfhdfhd"
p1 = r"chulin@hit\.edu\.cn"
#在.的前面加上了转义符\，但是并不是代表匹配“\.”的意思，而是只匹配“.”的意思！
pattern1 = re.compile(p1)
print pattern1.findall(key)
#-*- coding: utf-8 -*- 

import re

contactInfo = 'Doe,John:555-1212'
re.search(r'\w+,\w+:\S+', contactInfo)
search = re.search(r'(\w+),(\w+):(\S+)', contactInfo)
print search.group(0)
print search.group(1)
print search.group(2)
print search.group(3)
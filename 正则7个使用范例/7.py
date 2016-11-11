#-*- coding: utf-8 -*- 

import re

contactInfo = 'Doe,John:555-1212'
re.search(r'\w+,\w+:\S+', contactInfo)
search = re.search(r'(?P<last>\w+),(?P<first>\w+):(?P<phone>\S+)', contactInfo)
print search.group(0)
print search.group('last')
print search.group('first')
print search.group('phone')


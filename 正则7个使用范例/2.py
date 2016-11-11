#-*- coding: utf-8 -*- 

import re

re.match(r'dog', 'dog cat dog')
match = re.match(r'dog', 'dog cat dog')
print match.group(0)
print re.match(r'dog', 'dog cat dog').group(0)

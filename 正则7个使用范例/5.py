#-*- coding: utf-8 -*- 

import re

match = re.match(r'dog', 'dog cat dog')
print match.start()
print match.end()
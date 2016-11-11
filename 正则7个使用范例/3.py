#-*- coding: utf-8 -*- 

import re

re.search(r'cat', 'dog cat cat dog')
search = re.search(r'cat', 'dog cat cat dog')
print search.group(0)
print re.search(r'cat', 'dog cat cat dog').group(0)

#search()方法会在它查找到一个匹配项之后停止继续查找，因此在我们的示例字符串中用match()方法查找‘dog’只找到其首次出现的位置。
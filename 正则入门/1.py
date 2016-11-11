#-*- coding:utf-8 -*-
import re#导入模块

key = r"javapythonhtmlvhdq"#这是源文本
p1 = r"python"#这是正则表达式
pattern1 = re.compile(p1)#编译
matcher1 = re.search(pattern1,key)#查询
print matcher1.group(0)#输出
#print marcher1 错误写法
print pattern1.findall(key)#输出元素列表
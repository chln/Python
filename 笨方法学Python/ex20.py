# -*- coding: utf-8 -*-

from sys import argv #导入sys模组

script, input_file = argv #将argv分包给script和input_file

def print_all(f): #定义函数，功能为读取并打印f文件
    print f.read()
	
def rewind(f): #定义函数，功能为跳转到f文件数据的开头
    f.seek(0)
	
def print_a_line(line_count, f): #定义函数，功能为读取一行并打印该行
    print line_count, f.readline()
	
current_file = open(input_file) #打开文件

print "First let's print the whole file:\n" #打印一段话

print_all(current_file) #调用读取打印函数

print "Now let's rewind, kind of like a tape." #打印一段话

rewind(current_file) #调用跳转数据开头函数

print "Now let's print three lines:" #打印一段话

current_line = 1 #行1
print_a_line(current_line, current_file) #调用读取打印行函数

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
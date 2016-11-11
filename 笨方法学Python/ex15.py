# -*- coding: utf-8 -*-

from sys import argv #将sys模组中argv变量引入

script, filename = argv #将argv变量解包到script和filename

txt = open(filename) #打开名字为filename的文件并传递给txt变量

print "Here's your file %r:" % filename #打印一段话
print txt.read() #打印读取txt变量存储

print "Type the filename again:" #打印一段话
file_again = raw_input(">") #打印>并输入字符串给file_again变量

txt_again = open(file_again) #打开名字为file_again的文件并传递给txt_again变量

print txt_again.read() #打印读取txt_again变量存储

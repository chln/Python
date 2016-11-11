from sys import argv #添加sys模组

script, filename = argv #argv分包给script和filename

print "We're going to erase %r." % filename #打印一段话
print "If you don't want that, hit CTRL-C (^C)." #打印一段话
print "If you do want that, hit RETURN." #打印一段话

raw_input("?") #打印？并输入不带返回值

print "Opening the file..." #打印一段话
target = open(filename, 'w') #以写的方式打开一个文件

print "Truncating the file. Goodbye!" #打印一段话
target.truncate() #调用文件truncate清空功能

print "Now I'm going to ask you for three lines." #打印一段话

line1 = raw_input("line 1:") #输入一段话
line2 = raw_input("line 2:") #输入一段话
line3 = raw_input("line 3:") #输入一段话

print "I'm going to write thess to the file." #打印一段话

target.write(line1) #写入一段话
target.write("\n") #写入回车
target.write(line2) #写入一段话
target.write("\n") #写入回车
target.write(line3) #写入一段话
target.write("\n") #写入回车

print "And finally, we close it." #打印一段话
target.close() #关闭文件


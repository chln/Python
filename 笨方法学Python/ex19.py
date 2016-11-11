# -*- coding: utf-8 -*- #utf-8格式

def cheese_and_crackers(cheese_count, boxes_of_crackers): #定义函数与变量
    print "You have %d cheeses!" % cheese_count #打印含变量的一段话
    print "You have %d boxes of crackers!" % boxes_of_crackers #打印含变量的一段话
    print "Man that's enough for a party!" #打印一段话
    print "Get a blanket. \n" #打印一段话
	
print "We can just give the function numbers directly:" #打印一段话
cheese_and_crackers(20, 30) #给函数赋值

print "OP, we can use variables from our script:" #打印一段话
amount_of_cheese = 10 #给变量赋值
amount_of_crackers = 50 #给变量赋值

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #给函数赋变量

print "We can even do math inside too:" #打印一段话
cheese_and_crackers(10 + 20, 5 + 6) #给函数赋变量

print "And we can combine the two, variables and math:" #打印一段话
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers +1000) #给函数赋值
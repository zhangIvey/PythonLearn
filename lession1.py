#!/usr/bin/env python3
print("我的第一个python程序")
print(100 + 200)

"""
name = input()
sex = input()
company = input()

print("name = ",name,"sex = ",sex,"company = ",company)
"""

# 当行注释

'''
多行注释
多行注释
'''

"""
多行注释
多行注释
"""

import keyword
print("保留字 ： ",keyword.kwlist)


#行与缩进
if True:
	print("Answer")
	print("true")
else:
	print("Answer")
	print("false")


#多行语句
itemOne = 1
itemTwo = 2
itemThree = 3
total = itemOne + \
		itemTwo + \
		itemThree
print("total ：",total)


#字符串
word = "stringWord"
print("word = " + word)

word = 'stringWord2'
print("word = " + word)

word = '''这是一个比较长的字符串，
	   所以需要换行和多行，进行显示
	设置多行文字，
	需要使用三个连续的单引号或者三个连续的双引号
	'''
print("word = " + word)



print("打印最左边的两个字符："+word[0:2])
print("打印最右边的三个字符："+word[3:-1])


times = 3  #多次输出同一个字符串
print("输出",times,"次字符串："+word*3)

# 转义字符\
print("我要换行\n"+"换行完成")


#输入
# input("请输入内容\n\n")

x = "a"
y = "b"
print("--------------")
print(x,end=" ")
print(y,end="\n")
print()

# import 与 from...import

import sys
for i in sys.argv:
	print(i)

print("\n python 路径为",sys.path)

from sys import argv,path
print('path:',path)
print("argv:",argv)

a = b = c = 1
print(a, b, c)


a, b, c = "a","b", 123
print(a, b, c)

stringWord = r"weijos!@#$%^&|?{}0\\\';./"
print(stringWord)


#list


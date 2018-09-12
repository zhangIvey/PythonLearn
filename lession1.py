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
citysList= ["济南","北京",'上海',"莱芜","临沂"]
print(citysList)
print(citysList[1])
print(citysList[0:3])
citysList[1] = "泰安"  #元素可变更
print(citysList[0:2])
citysList[0] = 12
print(citysList)


#tuple
namesTuple = ("张三","李四","王五",12345,citysList)
print(namesTuple)
print(namesTuple[1])
print(namesTuple[0:3])
# citysList[1] = "泰安"  #元素不可变更
print(namesTuple[0:2])
# citysList[0] = 12
print(namesTuple)
citysList[0] = 9999999
print(namesTuple)

agesTuple = () # 空元组
agesTuple = (12,)# 一个元素，需要在元素后添加逗号

allTuple = namesTuple + agesTuple #元组拼接
print(allTuple)

#集合
fruitsSet = {"西瓜","葡萄","橘子","荔枝","榴莲","西瓜"}
fruits2Set = {"苹果","水蜜桃","西瓜"}
print(fruitsSet)
print(fruits2Set)

charsSet = set("adfewfgzgrtjudhs")
print(charsSet)
chars2Set = set("bn,j,;lhlhasdnrsgjh")
print(chars2Set)

#set可以进行运算
print(charsSet - chars2Set)  #a和b的差集
print(fruitsSet | fruits2Set) # a和b的并集
print(fruits2Set & fruitsSet) # a和b的交集
print(fruitsSet ^ fruits2Set) # a和b中不同时存在的元素




# dictionary
infoDic = {}
infoDic["name"] = "徐文京"
infoDic['age'] = 23
infoDic["height"] = 190
print(infoDic)
print(infoDic["height"])
infoDic["havaGF"] = True
print(infoDic["havaGF"])
infoDic[00] = "描述内容"
print(infoDic[00])
print(infoDic.keys())
print(infoDic.values())

infoDic["name"] = "闫威"
print(infoDic)

# info2Dic = {}
# info2Dic(name = "李祥祯", age = 23, height = 170)
# print(info2Dic)

# Number数据类型
varNumber = 1
varNumber2 = 2
del varNumber
# print(varNumber)
print(varNumber2)

varNumber3 = 0x23489 #十六进制
varNumber4 = 0o7623 #八进制

print(varNumber3)
print(varNumber4)


















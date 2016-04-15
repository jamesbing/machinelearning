#!/usr/bin/env python
# coding=utf-8
print u'这是一段中文字符'
print '这也是一段中文字符'
print '测试格式化输出'
print '我想输出%d个变量，其中第一个变量是π值%f,第二个变量是我的名字%s。' % (2, 3.14159265358979323846, 'james leng')
#列表和元组的概念  list和tuple
#首先是list
names = ['james','yang','zhou','li','wang']
print names
#list是一个可变的有序表，所以可以向list的末尾追加元素。
names.append([u'刘',u'王',u'周',u'白'])
print names
#也可以在某个指定的位置插入
names.insert(3, ['test1','test2','test3','testing'])
print names
#删除末尾的元素用pop(),可在其中指定要删除的数据的位置
print names.pop()
print names.pop(3)
#元组替换直接在想要替换的位置进行替换即可。
names[4]=u'这是替换之后的元素'
print names

#tuple功能与list类似，但是区别是tuple一经赋值不可修改，因此在初始化的时候tuple中的内容就必须要确定下来
#如果要定义一个空的tuple，那么应该这样a=()。
#tuple用的是括号()而list用的是大括号[]其他方面tuple和list是一样的
#tuple不可变因而代码更安全。如果可能，能用tuple存储数据的地方不要用list
#此外tuple还有一个陷阱就是，如果要定义一个只有一个元素的元组，不可以这样：a=(1)
#此时，python会把a当做整数1，而不是元组.因此如果要定义一个只有一个元素的元组时，
#应该加逗号。例如a=(1,)
tupleNames=('test','test1','test2','test3','test4')
tupleOne=(1,)
tupleTwo=("Guess who I am",)
numberOne=(1)
stringOne=("Guess who I am")
print tupleNames
print tupleOne
print numberOne
print tupleTwo
print stringOne

#一个有关tuple的小trick，就是一个貌似可变的tuple
changebleTuple=('a','b',['A','B'])
print changebleTuple
changebleTuple[2][0]='C'
changebleTuple[2][1]='D'
print changebleTuple

sum = 0
for mark in range(101):
    sum += mark
print sum

#从python的raw_input()函数中接收到的内容永远是以字符串的形式接收的。
#所以以下段子也就明了了：
birthdate = raw_input("输入你的生日>>>")
if birthdate < 2000:
    print "你是00前"
else:
    print "你是00后"
#不管你输入多少，上面程序段输出的结果应该都是你是00后。原因时birthdate总是一个字符串，永远是false
#因此如果你想要整数，那么应该先进行强制类型转换
birthdate = int(raw_input("请输入你的生日>>>"))
if birthdate < 2000:
    print "你是00前"
else:
    print "你是00后"

#字典和集合的应用：dict and set
#dict在有些语言中也称作map，使用键值对的方式进行存储，有Hash表的快速查找的优点
#总结：list的定义用['','','']; tuple的定义用(,,,);
#字典的定义用{'':'', '':'', '':''};而set则需要用set关键字
#定义一个字典：
dictA = {'name':'james','age':26,'sex':'male'}
print dictA['name']
#向字典中添加新的键值对
dictA['school'] = "Nankai University"
print dictA['school']
#改变字典中某个键值对的记录
dictA['school'] = "MIT"
print dictA['school']
#如果直接访问字典中不存在的键值对会报错。为了避免报错，可以采用如下的访问方式：
#第一种方法是用get函数，并且在后面指定如果不存在时返回的值
valueDorm = dictA.get('dorm','not exist')
print valueDorm
#第二种方法是先判断某个键值是否存在于字典中：
if 'dorm' in dictA:
    dorm = dictA['dorm']
    print dorm
else:
    print "can not find this key."
#要删除某个键值对，可以用pop函数：
dictA.pop('school')
school = dictA.get('school', 'school has been deleted.')
print school

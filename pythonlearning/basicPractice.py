# coding=utf-8
print u'这是一段中文字符'
print '这也是一段中文字符'
print '测试格式化输出'
print '我想输出%d个变量，其中第一个变量是π值%f,第二个变量是我的名字%s。' % (2, 3.14159265358979323846, 'james leng')
print '''
#列表和元组的概念  list和tuple
#首先是list
'''
names = ['james','yang','zhou','li','wang']
print names
print 'list是一个可变的有序表，所以可以向list的末尾追加元素。'
names.append([u'刘',u'王',u'周',u'白'])
print names
print '也可以在某个指定的位置插入'
names.insert(3, ['test1','test2','test3','testing'])
print names
print '删除末尾的元素用pop(),可在其中指定要删除的数据的位置'
print names.pop()
print names.pop(3)
print '元组替换直接在想要替换的位置进行替换即可。'
names[4]=u'这是替换之后的元素'
print names
print '''
#tuple功能与list类似，但是区别是tuple一经赋值不可修改，因此在初始化的时候tuple中的内容就必须要确定下来
#如果要定义一个空的tuple，那么应该这样a=()。
#tuple用的是括号()而list用的是大括号[]其他方面tuple和list是一样的
#tuple不可变因而代码更安全。如果可能，能用tuple存储数据的地方不要用list
#此外tuple还有一个陷阱就是，如果要定义一个只有一个元素的元组，不可以这样：a=(1)
#此时，python会把a当做整数1，而不是元组.因此如果要定义一个只有一个元素的元组时，
#应该加逗号。例如a=(1,)
'''
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

print '''
一个有关tuple的小trick，就是一个貌似可变的tuple
changebleTuple=('a','b',['A','B'])
print changebleTuple
changebleTuple[2][0]='C'
changebleTuple[2][1]='D'
print changebleTuple的结果是：
'''

changebleTuple=('a','b',['A','B'])
print changebleTuple
changebleTuple[2][0]='C'
changebleTuple[2][1]='D'
print changebleTuple
sum = 0
for mark in range(101):
    sum += mark
print sum

print '#从python的raw_input()函数中接收到的内容永远是以字符串的形式接收的。'
print '#所以以下段子也就明了了：'
'''
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
#接访问字典中不存在的键值对会报错。为了避免报错，可以采用如下的访问方式：
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
'''

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

print '''
有关dict的几个总结：
① 相比list，字典：速度快，占用内存大
② key值必须是不可变对象，因此字符串、整数等python的不可变对象都可以用来当做key、
    但是list这种可变对象就不可以用来当做key。
'''
testDic={1:'james',2:'bing'}
print testDic[1]
print testDic[1.0]
print '''
从上面的三行代码可以看出，在字典中，1和1.0索引的是同一个位置的数据
'''
print '''
字典有以下几种定义方式，它们的结果是相同的：
a = dict(one = 1, two = 2, three = 3
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two', 2),('one'. 1),('three', 3)])
e = dict({'three':3, 'one':1, 'two':2})
f = {'three':3, 'two':2, 'one':1}
那么 a == b == c == d == e == f的值应该为true：
'''
a = dict(one = 1, two = 2, three = 3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two', 2),('one', 1),('three', 3)])
e = dict({'three':3, 'one':1, 'two':2})
f = {'three':3, 'two':2, 'one':1}
print a == b == c == d == e == f
print '''
字典的长度用len来求
'''
print "字典a为：", a
print "字典a、b等的长度是",len(a)

del a['one']
print "删除字典中的元素除了用pop还可以用del函数， 例如del a['one']之后的a为：", a

print "iter()以及iterkeys()函数返回的是这个字典的迭代器", a.iterkeys()

print "items()函数将整个字典返回：",a.items()

print "viewitems()函数返回的是：",a.viewitems()

print "keys()函数返回所有的key值，values()函数返回所有的value值", a.keys(), a.values()

#TODO python的字典用法有待继续补充，此处先继续进行set的练习

print '''
set跟dict一样都是一组集合，
但是set相当于一个dict但是不存储value，只存储key，而且set中存储的
key值是一定不能重复的
set其实可以看作是数学意义上的无序和无重复元素的集合，因此两个set可以做数学意义上的
交并补等运算。set与dict唯一的区别就在于set不存在value，其他原理同dict一样
因此set中也不可以放入可变对象。
创建set时需要将一个list作为输入集合，例如
s = set([1,2,2,1,2,1l,3,4,23,1,2,1,2])
print s的结果如下:
'''
s = set([1,2,2,1,2,1l,3,4,23,1,2,1,2])
print s
print '''
set中不能有可变对象，比如将一个嵌套list丢进去：
s = set([1,2,3,2,1,3,1,2,[3,2,4,5],4,3,2])
print s的结果为：
'''

#s = set([1,2,3,2,1,3,1,2,[3,2,4,5],4,3,2])
#print s

print '''
python中有一个很重要的功能叫做推倒式。推导式包含列表推导式，字典推导式和集合推导式，分别对应三种不同的python容器
列表推导式可以用一条语句构造一个新列表，代码可以写成：
[expr for value in collection ifcondition]
它相当于下面一段代码：
result = []
for value in collection:
	if condition:
	result.append(expression)
实际应用：过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
[name.uper() for name in names if len(name)>3]
返回的应该是['ALICE','JERRY','WENDY','SMITH']
'''

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']

result = [name.upper() for name in names if len(name)>3]

print result

print '''
第二个例子是：求（x,y）其中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
代码应该是：
'''
result = [(x,y) for x in range(5) if x%2 == 0 for y in range(5) if y%2 == 1]
print result

print '''
M = [[1,2,3],[4,5,6],[7,8,9]]
将M的每个子列表的第三个元素组成一个新的列表：
可得到结果：
result = [row[3] for row in M]
'''
M = [[1,2,3],[4,5,6],[7,8,9]]
result = [row[2] for row in M]
print result

print '''
将M对应的矩阵的斜对角线上的元素重新组成一个新的列表：
result = [M[i][i] for i in range(len(M))]
'''
result = [M[i][i] for i in range(len(M))]
print result

print '''
现在有两个列表，除了M,还有N，M用的是上面的定义：
'''
print M
print '''
N的定义为：
'''
N = [[2,2,2],[3,3,3],[4,4,4]]
print N
print '''
现在要做的事情是用这两个矩阵中的元素做一些运算：
首先：得到如下矩阵：
[2,4,6,12,15,18,28,32,36]
result = [M[x][y] * N[x][y] for x in range(3) for y in range(3)]
运算结果为：
'''
result = [M[x][y] * N[x][y] for x in range(3) for y in range(3)]
print result

print '''
然后要求得到如下结果：
[2,4,6],[12,15,18],[28,32,36]
应该这样：
result = [[M[x][y] * N[x][y] for x in range(3)] for y in range(3)]
最终结果应该是：
'''
result = [[M[x][y] * N[x][y] for x in range(3)] for y in range(3)]
print result
result = [[M[y][x] * N[y][x] for x in range(3)] for y in range(3)]

print '''
上面的x y掉个个就成了：
result = [[M[y][x] * N[y][x] for x in range(3)] for y in range(3)]
结果为：
'''
print result

print '''
字典中的推导式：
字典推导式和列表推导式差不多，只不过结果产生的是字典和集合；
{key_expr:value_expr for value in collection if condition}

'''

print '''
在python中，有三个与循环相关的函数，分别是range(),enumerate()和zip()
以下代码：
S = 'abcdefghijk'
for i in range(0, len(S), 2)
	print S[i]
的输出为：
'''
S = 'abcdefghijk'
for i in range(0, len(S), 2):
	print S[i]

print '''
上面range中的变量分别是：起点，重点，步长
enumerate（）函数的作用是：在每次循环中同时得到元素的下标以及元素本身。
下面的代码：
S仍然用上面的S
for (index, char) in enumerate(S):
	print index
	print char
输出结果为：
'''
for (index, char) in enumerate(S):
	print index,char

print '''
此处可以联系前面的推导式中的东西。
enumerate（）在每次循环时返回的是一个包含两个元素的元组tuple，两个元组分别赋给
index和char两个变量。
而zip（）函数则可以在应对多个等长序列时，每次循环都各从各个序列中分别取出一个元素
此时可以用zip（）方便实现。
下面的代码：
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
	print(a,b,c)
这样每次循环的时候，都会从各个序列中分别从左到右取出一个元素，并合并成一个tuple，然后
将tuple中的元素赋给a,b,c。就像其名字一样，zip起到聚合数据的作用。
故上面的代码的输出应该是：
'''
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
	print(a,b,c)
print '''
此外，对于上面的ta,tb，下面的代码：
zipped = zip(ta,tb)
print (zipped)
#而加上表示指针的符号*之后则起到解压的作用
suba, subb = zip(*zipped)
print (na, nb)
这段代码的输出是：
'''

zipped = zip(ta,tb)
print (zipped)
#而加上表示指针的符号*之后则起到解压的作用
suba, subb = zip(*zipped)
print (suba, subb)

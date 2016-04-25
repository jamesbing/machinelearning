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
下面的代码：（有关enumerate的知识在后面）
strings = ['i','am','very','glad','to','see','you','here']
D = [key:value for value,key in enumerate(strings)]
print D
的结果应该是：
'''
strings = ['i','am','very','glad','to','see','you','here']
D = {key:value for value,key in enumerate(strings)}
print D
print '''
代码段：
test = {len(S) for S in strings}
print test
的结果是：
'''
test = {len(S) for S in strings}
print test
print '''
现在有一个嵌套列表，分别包含两个子列表，其内容分别为男人和女人的姓名。
现在要求，将男人和女人的名字中所有包含两个e及以上的名字拿出来，组成一个列表。
names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana','Wendy','Tenee','Sheery','Eva']]
可以用两种方法实现：
第一种方法，简单的循环嵌套：
temp = []
for list in names:
	for name in list:
		if name.count('e') >= 2:
			temp.append(name)
print temp
第二种方法用推导式：
temp2 = [name for list in names for name in list if name.count('e)>=2]
print temp2
'''
names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana','Wendy','Tenee','Sheery','Eva']]
temp = []
for list in names:
	for name in list:
		if name.count('e') >= 2:
			temp.append(name)
temp2 = [name for list in names for name in list if name.count('e')>=2]
print '第一种方式的结果：',temp,'第二种方式的结果',temp2
print '可见两种结果是否相等：', temp == temp2
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
print '''
一些常用的python系统函数：
abs（）求绝对值
cmp（x,y）比较两个数的大小，如果x<y返回-1，如果x>y返回1，如果x==y返回0
数据类型转换相关函数：
int强制转换成整形
float强制转换成浮点型
str强制转换成字符串string
unicode强制转换成Unicode编码，可以查看一个字符所对应的Unicode编码
bool强制转换成布尔类型
有个小例子：
a=abs
a(-1)应该得到的是1，因为a相当于abs这个函数
'''
a=abs
print a(-1)
print '''
如果暂时一个函数什么都不做，可以用pass来告诉编译器，否则会报错
例如：
def testing_doing_nothing():
这样是会报错的，但是如果写成：
def testing_doing_nothing():
	pass
就不会出错
'''
def testing_doing_nothing():
	pass
print '''
此外pass还可以放在其他的地方，一般来说是任何冒号的后面，这样就意味着这一块
执行到冒号之后该干嘛还没想好，例如可以放在if语句中：
if age >= 18:
	pass
同样如果没有这个pass也是会报错的。
下一个问题是怎样在自己的函数中自己定义一些错误呢？
即怎样定义类似于java中的exception呢？
可以这么搞：
def my_testing_function(x):
	if not isinstance(x,(int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
然后调用：my_testing_function('测试')会出现以下结果：
'''
def my_testing_function(x):
	if not isinstance(x,(int, float)):
		raise TypeError('输入的值的类型有误！')
	if x >= 0:
		return x
	else:
		return -x
#my_testing_function('测试')
print '显然这样就把错误给唤出来了'
print '''
python的函数可以‘返回多个值’，其实这只是一个假象，真相是：
python把多个要返回的值打包成一个tuple扔了回来，然后后面的
调用函数的地方，接收方再把这个tuple解压出来。例如：
def test_multiple_return():
	a = 1
	b = 9
	b *= b
	return a, b
m = test_multiple_return()
m[0] = 9
执行到这儿应该会报错，就是尝试修改tuple不可变对象的错误。
然后可以看一下instanceof(m)是：
'''
def test_multiple_return():
	a = 1
	b = 9
	b *= b
	return a, b
m = test_multiple_return()
a, b = m
#m[0] = 9
print type(m)
print '得到的值分别是：', a, b
print '''
函数的默认参数设置：直接在参数列表中让这个值等于某个值即可。
如果不加这个默认参数，那么调用时参数列表必须对其赋值否则会报错。
例如：
def testing_default_parameter(a = 1, b = 3):
	return a + b
那么如果不加参数调用这个函数会得到：
'''
def testing_default_parameter(a = 1, b = 3):
	return a + b
print testing_default_parameter()
print '''
默认参数的好处就是可以降低函数的设计和调用难度。例如：
def sign_up(name, age, country = 'China', city = 'Beijing'):
	print 'name is :', name
	print 'age is :', age
	print 'country is:', country
	print 'city is :', city
在调用上述函数的时候，如果想指定某个参数的值，那么在调用时传参列表中
加上这个参数的具体指定即可，例如sign_up('james', 26, city = 'Tianjin')，那么
不加指定的就会使用默认参数。调用的结果为：
'''
def sign_up(name, age, country = 'China', city = 'Beijing'):
	print 'name is :', name
	print 'age is :', age
	print 'country is:', country
	print 'city is :', city
sign_up('james', 26, city = 'Tianjin')
print '''
默认参数的一个坑：且看下面的例子(用list作默认参数—)
def test_link_parameter(L=[]):
	L.append('END')
	print L
那么当这样使用的时候：
test_link_parameter(['a'])
test_link_parameter(['1','2','3'])
这样结果都不会出错。
但是，如果继续这样调用：
test_link_parameter()
test_link_parameter()
这样调用两次以后会得到错误的结果，如下所示：
'''
def test_link_parameter(L=[]):
	L.append('END')
	print L
test_link_parameter(['a'])
test_link_parameter(['1','2','3'])
test_link_parameter()
test_link_parameter()
print '''
这是因为list是可变的变量，最后两次调用由于都是用了一个默认的变量L
而这个L是在第一次默认调用时就已经创建好了的，所以：第二次默认调用以后
这个值就变成了在第一次创建的L后面继续加东西的过程。
为了避免这样的尴尬，可以这么写：
test_link_parameter_sub(L = None):
	if L is None:
		L = []
	L.append('END')
	print L
这样的话，L就指向了一个不可变对象None,无论默认调用多少次都不会出错了，
这个地方很容易产生bug，一定要注意。
测试一下：
连续三次调用:
test_link_parameter_sub()
的结果如下：
'''
def test_link_parameter_sub(L = None):
	if L is None:
		L = []
	L.append('END')
	print L
test_link_parameter_sub()
test_link_parameter_sub()
test_link_parameter_sub()
print '''
python可变参数：参数列表中的参数个数是可变的。这种情况下，无法实现预知
一个函数到底可以接受多少参数，此时可以用tuple或者list将参数包起来传过去
例如：
def my_add(numbers):
	sum = 0
	for number in numbers:
		sum += number
	print sum
	return sum
使用时可以这样：
my_add([1,2,3,4,5])
my_add([5,6,7,8,9,0,3])
结果如下：
'''
def my_add(numbers):
	sum = 0
	for number in numbers:
		sum += number
	print sum
	return sum
my_add([1,2,3,4,5])
my_add([5,6,7,8,9,0,3])
print '''
但是这样有个缺点，就是每次调用之前都需要组装一个数组或者tuple
如果改一下函数定义，将参数列表改成类似于C中的指针形式，就 不需要这样调用了
def my_add_sub(*numbers):
	sum = 0
	for number in numbers:
		sum += number
	print sum
	return sum
这样调用的时候直接往里面写数字即可：
my_add_sub(1,2,4,5,6)
my_add_sub(3,4,1,2,2,1,2,3,4,5,6)
'''
def my_add_sub(*numbers):
	sum = 0
	for number in numbers:
		sum += number
	print sum
	return sum
my_add_sub(1,2,4,5,6)
my_add_sub(3,4,1,2,2,1,2,3,4,5,6)
print '''
这样有个问题，就是如果已经有了一个列表或者是tuple，要传给他怎么办呢？
假设有个numbers = [1,2,3,4]那么应该这样传递：
my_add_sub(numbers[0],numbers[1],numbers[2],numbers[3])
这样很麻烦，可以采用类似于C语言中的穿指针的方法，直接把numbers整个扔进去就可以了：
即这样：
my_add_sub(*numbers),也可以得到结果：
'''
numbers = [1,2,3,4]
my_add_sub(*numbers)
print '''
组合起来讲，可以写一个例子：
def person(name, age, country = 'China', **otherInfo):
    print 'name:',name,'age:',age,'country:', country, otherInfo
    print 'major:',otherInfo.get('major')
person('james',26,country = 'USA', sex = 'male')
person('james',26,{'major':'engineer','address':'A str, B number'})
'''
def person(name, age, country = 'China', **otherInfo):
    print 'name:',name,'age:',age,'country:', country, otherInfo
    print 'major:',otherInfo.get('major')
person('james',26,country = 'USA', city='Tianjin')
otherInfo = {'city':'Tianjin','major':'student','sex':'male'}
person('james',26,country = 'USA',**otherInfo)
print '上面的代码段中，参数列表用了两个**来表示可变参数。'
print '''
python在定义函数的时候可以用四种类型的参数，他们可以混合使用：这四种参数为：
必选参数，默认参数，可变参数以及关键字参数。参数定义的顺序必须是：
必选参数、默认参数、可变参数以及关键字参数。上面一段代码的例子就是关键字参数。
例如：
def my_func(a,b,c=0,*args,**key):
    print 'a:',a,'b:',b,'c:',c,'args:',args,'key parameters:', key
在调用的时候，python解释器会按照参数位置和参数名把对应的参数穿进去。
例如：
my_func(1,2)
my_func(1,2,c=3)
my_func(1,2,3,'a','b')
my_func(1,2,3,'a','b','c',test='testing funny')
这些调用产生的结果分别如下：
'''
def my_func(a,b,c=0,*args,**key):
    print 'a:',a,'b:',b,'c:',c,'args:',args,'key parameters:', key
my_func(1,2)
my_func(1,2,c=3)
my_func(1,2,3,'a','b')
my_func(1,2,3,'a','b','c',test='testing funny')
print '''
对于任意函数，都可以通过类似func(*args, **kw)的形式来调用它，
无论它的参数列表是怎样定义的。
例如可以这样调用上述函数：
args = (1,2,3,4,5,6,'testing value')
kw = {'alpha':'a','basic':'haha','age':26}
my_func(*args, **kw)
'''
args = (1,2,3,4)
kw = {'alpha':'a','basic':'haha','age':26}
my_func(*args, **kw)
print '使用*arg和**kw是python的习惯用法。'

print '''
递归函数定义简单逻辑清晰，但是应该防止栈溢出。函数调用利用的是栈这种数据结构
来实现的，每当进入一个函数调用，栈就会自动增加一层，每当函数返回的时候
栈就会减少一层。所以当递归调用次数太多时，就会由于缺少足够的存储空间来
放置这个栈而引起栈溢出。例如：
def my_stack_test(n):
    if n == 1:
        return 1
    return n * my_stack_test(n - 1)
my_stack_test(1000)
会看到堆栈溢出的信息。
解决栈溢出的方法是尾递归优化，尾递归和循环的效果其实是一样的，不过
具有递归的逻辑清晰的有点。因此递归可以看成是一种特殊的尾递归函数。
尾递归指的是：
在函数返回的时候，调用自身本身，而且return语句不能包含表达式。这样编译器
会自动进行尾递归优化，这样无论递归调用多少次，都只占用一个栈空间，不会出现溢出。
上面的函数改成尾递归后应该这么写
def my_stack_good(n):
    return my_stack_inter(n,1)

def my_stack_inter(num, product):
    if num == 1:
        return product
    return my_stack_inter(num - 1, num * product)
这样尝试调用my_stack_good(1000)就不会在出错了：
'''
print '''
def my_stack_test(n):
    if n == 1:
        return 1
    return n * my_stack_test(n - 1)
#my_stack_test(1000)

def my_stack_good(n):
    return my_stack_inter(n,1)

def my_stack_inter(num, product):
    if num == 1:
        return product
    return my_stack_inter(num - 1, num * product)
my_stack_good(1000)
print '''

print '''
高级特性：
Python中，代码不是越多越好，而是越少越好。一些高级特性有助于用更少的代码量来实现同样的功能。
一行代码能够实现的功能，绝不用五行代码实现。
这里要学习四个高级特性：
①切片***Slice
②迭代***Interation
③列表生成式，也就是前面的列表推导***Comprehensions
④生成器***Generator
现在进行该部分学习
'''
print '''
①切片，Slice。这一特性主要是为了应对list或tuple的部分元素的操作。
如果是少量的元素，用循环append还好办，但是如果元素的数量较多，比如100000个元素去前8888个，那就傻了
于是可以用python的切片功能。
其实很简单，就是[x:y]就表示取从x到y的元素，包括x但不包括y。如果是正数，则是从前往后取，如果是负数，
则表示从后往前取值数数。例如，L[-2:]表示从倒数第二个往前取值，一直取到第一个。（如果冒号前后不写东西
在冒号前就意味着是开头，如果冒号后面，表示末尾。
例如：
L = range(10000)
#则L[0:777]表示取777个值，如果是L[-1000:]表示取后1000个数字。结果分别是：
print L[0:777], L[-1000:]
#TODO以后可以用python的计时工具来计算一下用切片和用循环分别用的时间。
'''
L = range(10000)
#则L[0:777]表示取777个值，如果是L[-1000:]表示取后1000个数字。结果分别是：
print L[0:777], L[-1000:]
#TODO以后可以用python的计时工具来计算一下用切片和用循环分别用的时间。

print '''
切片一些其他用法：
①例如：前一百个数字，每隔五个数字取一个：
print L[:100:5]
'''
#print L[:100:5]

print '''
②原样复制一个list：
M = L[:]
#print M
'''
M = L[:]
print M

print '''
③对tuple的操作：
print (0,1,2,3,4,5)[:5]
'''
print (0,1,2,3,4,5)[:5]

print '''
字符串'xxx'或者Unicode字符串u'xxx'也可以看做是一种list，每个元素就是一个字符
print 'guess who am i！'[0:5]
print 'guess who am i!'[::2]
'''
print 'guess who am i！'[0:5]
print 'guess who am i!'[::2]

print '''
②第二个高级特性是迭代：Iteration
'''

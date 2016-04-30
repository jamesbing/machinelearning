#!/usr/bin/env python
# coding=utf-8

'define people class'

__author__ = 'James Leng'

class People(object):

    #强制绑定需要初始化的参数
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        #属性前面加上两个下划线__就表示这个属性不可以被外部访问的，它是私有的。
        self.__age = age

    def getInfo(self):
        print 'Name:',self.name
        print 'sex:', self.sex
        print 'age:', self.__age

    def get_info(self):
        print '''
        两个与代码书写规范有关的问题：
        ①函数名要改一下java中的驼峰准则，一般在单词之间用_相连接。
        ②类中的函数与正常的函数只有一点差别：那就是类中的函数
        至少接受一个参数就是self，这在类的定义时必须写上，但是真正
        调用的时候，无需写self这个参数。self这个东西相当于java中的this。
        '''

people = People('James', 'male', 26)

people.getInfo()

xiaohong = People('xiaohong', 'male',20)
xiaohua = People('xiaohua','female',22)
xiaohong.height = 8
print xiaohong.height
try:
    print xiaohua.height
except AttributeError:
    print '''
    小红能打印出age这个属性是8，但是小花就没有这个属性，
    打印的是AttributeError，找不到age这个属性。
    同一个模板生成的实例还可以不相同。而且还可以动态添加新的属性。
    所以python真的是种动态语言。
    '''

try:
    print xiaohua.__age
except AttributeError:
    print '''
    不能访问__age变量，因为变量名称前面加了两个下划线__，因此它
    是类内部的私有变量，不能被外面访问，只有类中的函数可以调用它
    这样就增加了封装性，提高了安全性。
    '''
print '''
但是如果我真要访问类里面的私有变量也是可以的。
比如上面的__age，编译器其实是把它封装成_People__age了，如果直接这么访问
还是可以访问到的：但是处于健壮性考虑，不应该这么做。python并没有一种死的机制
来确保这件事情，全靠程序员的把控。
print xiaohong._People__age
'''
print xiaohong._People__age
xiaohong.get_info()

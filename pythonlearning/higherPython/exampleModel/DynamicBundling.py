#!/usr/bin/env python
# coding=utf-8
#python可以动态绑定方法

from types import MethodType

class Student(object):
    pass

s = Student()

print 'Student类中本来没有name属性。在运行时可以动态绑定。'
s.name = 'James'

print s.name


print '动态绑定属性比较简单。方法，也是可以动态绑定的。'
print '''
现在新定义一个方法，然后把该方法绑定给这个实例
def set_age(self, age):
    self.age = age

from types import MethodType'
s.set_age = MethodType(set_age, s, Student)
上面三个参数的意思是：将set_age这个方法绑定至属于Student类的实例s上。
s.set_age(29)
s.age

t = Student()
t.set_age(29)
t.age
'''


def set_age(self, age):
    self.age = age
s.set_age = MethodType(set_age, s, Student)
s.set_age(29)
print s.age

    

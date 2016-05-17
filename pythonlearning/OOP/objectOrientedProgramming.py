#!/usr/bin/env python
# coding=utf-8

print '''
封装、继承、多态是python面向对象的基础内容。还有一些高级内容，例如：
多重继承、定制类、元类等等。通过MethodType可以动态的为实例化了的类
绑定新的方法。绑定属性相比来说简单一些
'''
from types import MethodType
def set_age(self, age):
    self.age = age

class student(object):
    pass

xiaoming = student()

xiaoming.set_age = MethodType(set_age, xiaoming, student)             

xiaoming.set_age(7)

print xiaoming.age

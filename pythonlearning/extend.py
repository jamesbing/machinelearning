#!/usr/bin/env python
# coding=utf-8
# @author james. lengjiabing@gmail.com
# this code block is used to show how the class concept works in python
# there are two main extend styles included in this file.

class Parent(object):
    def overide(self):
        print "Parent ovrride testing function, overide()"

    def implicit(self):
        print "Parent implicit function"

    def alter(self):
        print "Parent alter function"

# the style clas A(B), in which B is another class, this means, the class A extends class B.
class Child(Parent):
    def overide(self):
        print "Child overide testing function, voeride()"

    def alter(self):
        print "first show the Child's alter fucntion. Before CHILD alter fucntion"
        super(Child,self).alter()
        print "first show the Child's alter function. After CHILD alter function"


dad = Parent()
son = Child()
# we didn't do anyting to the implicit function in Parent class, so the son class is exactly the same
dad.implicit()
son.implicit()

# this is override. totally not the same.
dad.overide()
son.overide()

#this is the use of super key word.
dad.alter()
son.alter()


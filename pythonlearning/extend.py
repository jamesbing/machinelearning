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


class Other(object):
    def overide(self):
        print "Other ovrride testing function, overide()"

    def implicit(self):
        print "Other implicit function"

    def alter(self):
        print "Other alter function"



# the style clas A(B), in which B is another class, this means, the class A extends class B.
class Child(Parent):

    def __init__(self,stuff):
        self.stuff = stuff
        super(Child, self).__init__()
        self.other = Other()

    def overide(self):
        print "Child overide testing function, voeride()"
        #be careful that we should use self.other.overide() to call other or the other variables.
        #or you will be encounter an issue called global variable not defined stuff.
        #other.overide()
        self.other.overide()
        print "The stuff you give is:",self.stuff

    def alter(self):
        print "first show the Child's alter fucntion. Before CHILD alter fucntion"
        super(Child,self).alter()
        print "first show the Child's alter function. After CHILD alter function"
        self.other.alter()


dad = Parent()
son = Child("testing")
# we didn't do anyting to the implicit function in Parent class, so the son class is exactly the same
dad.implicit()
son.implicit()

# this is override. totally not the same.
dad.overide()
son.overide()

#this is the use of super key word.
dad.alter()
son.alter()


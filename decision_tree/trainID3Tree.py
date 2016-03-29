#!/usr/bin/env python
# coding=utf-8
from numpy import *
from ID3DTree import *

dtree = ID3DTree()
dtree.loadDataSet("dataset.dat",["age","revenue","student","credit"])
dtree.train()
print dtree.tree

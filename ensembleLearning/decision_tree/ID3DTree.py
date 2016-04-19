#!/usr/bin/env python
# coding=utf-8
# @author james.
# This file is the core algorightm of ID3, which is a decision tree in machinelearning algorightme
# 在决策树算法中，最核心的工作就是在一个数据集上，不断寻找对划分数据分类起关键作用的特征。
# 其基本方式是：
'''
    检测数据集中的每个子项是否属于统一分类：
    if so return class label
    else:
        寻找划分数据集的最好特征
        划分数据集
        创建分支节点
            for 每个划分的子集
                迭代调用这个算法病增加返回结果到分支节点中
        return 分支节点
'''
#数据集划分时要遵循的核心原则是：将无序的数据变得更加有序。而组织无序数据的一种有效方式就是
#使用信息论度量信息。可以在划分数据之前或者之后使用信息论度量。
#数据划分之前和之后，信息所发生的变化成为信息增益，因此，计算信息增益的方法是划分数据方法衡量的重要依据。
#这样，决策树就转换成在一个无序的数据集上，找到使划分前后的数据集的信息增益最高的方法。这个度量就是信息熵。

#信息增益：information gain
#信息熵：information entropy



from numpy import *
import math
import copy
import cPickle as pickle

class ID3DTree(object):
    # the init function of the ID3 tree
    def __init__(self):
        self.tree = {}
        self.dataSet = []
        self.labels = []

    # to load data from specific file place and transform it to a one dimention table
    def loadDataSet(self,path,labels):
        recordlist = []
        fp = open(path,"rb")
        content = fp.read()
        fp.close()
        rowlist = content.splitlines()
        recordlist = [row.split("\t") for row in rowlist if row.strip()]
        self.dataSet = recordlist
        self.labels = labels

    
    # to execute the decision function
    def train(self):
        labels = copy.deepcopy(self.labels)
        self.tree = self.buildTree(self.dataSet,labels)

    # build tree
    def buildTree(self,dataSet,labels):
        cateList = [data[-1] for data in dataSet]
        if cateList.count(cateList[0] == len(cateList)):
            return cateList
        if len(dataSet[0]) == 1:
            return self.maxCate(cateList)
        # the core of ID3 algorightm
        bestFeat = self.getBestFeat(dataSet)
        bestFeatLabel = labels[bestFeat]
        tree = {bestFeatLabel:{}}
        del(labels[bestFeat])
        uniqueVals = set([data[bestFeat] for data in dataSet])
        for value in uniqueVals:
            subLabels = labels[:]
            splitDataset = self.splitDataSet(dataSet, bestFeat, value)
            subTree = self.buildTree(splitDataset,subLabels)
            tree[bestFeatLabel][value] = subTree
        return tree

    def maxCate(self,cateList):
        items = dict([(cateList.count(i), i) for i in cateList])
        return items[max(items.keys())]

    def getBestFeature(self,dataSet):
        numFeatures = len(dataSet[0]) - 1
        baseEntropy = self.computeEntropy(dataSet)
        bestInfoGain = 0.0
        bestFeature = -1
        for i in xrange(numFeatures):
            uniqueVals = set([data[i] for data in dataSet])
            newEntropy = 0.0
            for value in uniqueVals:
                subDataSet = self.splitDataSet(dataSet, i, value)
                prob = len(subDataSet)/float(len(dataSet))
                newEntropy += prob * self.computeEntropy(subDataSet)
            infoGain = baseEntropy - newEntropy
            if (infoGain > bestInfoGain):
                bestInfoGain = infoGain
                bestFeature = i
        return bestFeature

    '''
    这里其实计算的是香农熵
    符号xi的信息定义为：l(xi) = - log2(xi)
    所有类别中所有可能值包含的信息期望值可以用来计算香农信息熵
    公式为:H = -∑p(xi)log2(xi)   求和范围时从1到n， n为个数
    '''
    def computeEntropy(self,dataSet):
        datalen = float(len(dataSet))
        cateList = [data[-1] for data in dataSet]
        items = dict([(i,cateList.count(i)) for i in cateList])
        infoEntropy = 0.0
        for key in items:
            prob = float(items[key])/datalen
            infoEntropy -= prob * math.log(prob,2)
        return infoEntropy
    
    #
    def splitDataSet(self, dataSet, axis, value):
        rtnList = []
        for featVec in dataSet:
            if featVec[axis] == value:
                rFeatVec = featVec[:axis]
                rFeatVec.extend(featVec[axis + 1:])
                rtnList.append(rFeatVec)
        return rtnList

    
    #testing purpose
    def createDataSet():
        dataSet = [[1,1,'yes'],
            [1,1,'yes'],
            [1,0,'no'],
            [0,1,'no']
            [0,1,'no']
        ]
        labels = ['no surfacing', 'flippers']
        return dataSet, labels 

#!/usr/bin/env python
# coding=utf-8
# @author james.
# This file is the core algorightm of ID3, which is a decision tree in machinelearning algorightme
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

    def getBestFeat(self,dataSet):
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

    def computeEntropy(self,dataSet):
        datalen = float(len(dataSet))
        cateList = [data[-1] for data in dataSet]
        items = dict([(i,cateList.count(i)) for i in cateList])
        infoEntropy = 0.0
        for key in items:
            prob = float(items[key])/datalen
            infoEntropy -= prob * math.log(prob,2)
        return infoEntropy

    def splitDataSet(self, dataSet, axis, value):
        rtnList = []
        for featVec in dataSet:
            if featVec[axis] == value:
                rFeatVec = featVec[:axis]
                rFeatVec.extend(featVec[axis + 1:])
                rtnList.append(rFeatVec)
        return rtnList

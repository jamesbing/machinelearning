#!/usr/bin/env python
# coding=utf-8
# this file is the core algorithm of KNN
# @author james::lengjiabing@gmail.com
from numpy import *
import operator

# the core algorithm calculation code of KNN
# inX: the input vector;
# dataSet: traing sample set;
# labels: label vector;
# k: need to be setted by user.
def kNNClassify0(inX, dataSet, labels, k):
    # calculate the distance
    dataSetSize = dataSet.shape[0]
    # 由于采用欧氏距离来计算输入待分类向量与训练及矩阵中每一个特征向量之间的欧式距离
    # 所以可以采用将待分类矩阵生成一个与训练样本集矩阵大小相同的矩阵然后求差的操作
    difMat = tile(inX, (dataSetSize, 1)) - dataSet
    sortedDistanceMatrix = ((difMat ** 2).sum(axis = 1) ** 0.5).argsort()

    # choose k nearast neighbor points
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistanceMatrix[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # order the k points from little to large
    sortedClassCount = sorted(classCount.iteritems(),
                            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

#!/usr/bin/env python
# coding=utf-8
# this file is the core algorithm of KNN
# @author james::lengjiabing@gmail.com
from numpy import *
import operator
import file2matrix

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

# normalization dataSet to let the dataset's value varies from 0 to 1
# this function can also be extracted out for general purpose
# the principle is: newValue = (oldValue - min)/(max - min)
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet, ranges, minVals

# testing the KNN algorithm's performance on dating's dataSet
def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix.file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0
    
    for i in range(numTestVecs):
        classifierResult = kNNClassify0(normMat[i,:], normMat[numTestVecs,:],
                                        datingLabels[numTestVecs:m], 3)
        print "The classifier came back with : %d, the real answer is : %d" % (
            classifierResult, datingLabels[i]
        )
        if (classifierResult != datingLabels[i]):
            errorCount +- 1

    print "The Total error rate is : %f" % (errorCount/float(numTestVecs))

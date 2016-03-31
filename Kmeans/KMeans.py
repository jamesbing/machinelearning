#!/usr/bin/env python
# coding=utf-8
# this code block is used to support the k-means clustering algorithm.
# @author james::lengjiabing@gmail.com

from numpy import *

def loadDataSet(fileName):
    print "loading data..."
    
    dataMat = []
    fr = open(fileName)
    for line in fr.readline():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

# 计算欧氏距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))
    
# 构建簇质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

#这是K-means算法的核心算法代码
def kMeans(dataSet, k, distMeas = distEclud, createCent = randCent):

#    @TODO ///


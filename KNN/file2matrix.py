#!/usr/bin/env python
# coding=utf-8
# this code segment is used to transform the data in a txt file in to a numpy supported matrix.
# @author james::lengjiabing@gmail.com

from numpy import *

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        tempValue = listFromLine[-1]
        if tempValue == 'didntLike':
            classLabelVector.append(1)
        elif tempValue == 'smallDoes':
            classLabelVector.append(2)
        else:
            classLabelVector.append(3)
        # classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat,classLabelVector


#!/usr/bin/env python
# coding=utf-8
#集成模型方法通常会取得比单个分类器更为精确的结果。
#其中主要思路是采用某种策略从训练数据集中提出或整合出
#多个不同的有或大或小的子数据集，并且用这些数据集
#训练出多个存在差异的若分类器，然后将这些分类器整合成
#一个完整的集成模型，当要进行一个分类任务时，采用
#投票或者权值的方法综合考虑所有的这些不同的分类器的决策
#最终整合成一个分类决策。有点类似民主集中制。
#对于单个的分类器的要求很简单，只要它们的决策效果
#比瞎蒙略好一点就行。因此这是一个典型的由若分类器
#构建成强分类器的思想。此处联想到KK的失控一书中
#有关蜂群的描述。可以深入了解，体会两者之间的联系。
#根据有差异的训练子集的生成方式，概括有两种方法
#可以实现上述思想，一个是bagging，一个是boosting。
#这个python文件实现bagging方法。
@TODO


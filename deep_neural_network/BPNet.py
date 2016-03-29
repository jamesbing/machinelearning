#!/usr/bin/env python
# coding=utf-8
# this is a model of BPNet, in which BP means back propogation.
# @author james :: lengjiabing@gmail.com

# define BPNet model
class BPNet(object):
    # the construction function
    # if you use *argv, then it means argv can receive changeble variables, and if you use **argv,
    #then it means that this is a dictorary type of data.
    def __init__(self, *argv):
        #@TODO
        ''' the following code block should be extracted out as a seperate block
            which will enable user constrct his own network due to specific purpose.
        '''
        #@ODOT
        settings = argv
        '''以下参数的含义分别作如下对应：
            eb:误差容限，既设置算法停止迭代的标志位
            iterator:用于存储算法收敛时的迭代次数，既算法的迭代器
            eta:算法变量调整的学习步长
            mc:动量因子，做调优之用
            maxiter:最大迭代次数
            nHidden:隐藏层神经元个数
            nOut:输出层个数，可视为特征个数
            以下变量可由系统自动随机生成，作为网络随机初始化参数
            errlist:误差列表，用于对收敛性的评估
            dataMat:训练数据集
            classLabels:分类标签集
            nSampNum:样本集行数
            nSampDim:样本集列数
        '''
        print "The BP Network been initiated, and the initiation variables are:\n", settings
        self.eb = settings["eb"]
        self.iterator = settings["iterator"]
        self.eta = settings["eta"]
        self.mc = settings["mc"]
        self.maxiter = settings["maxiter"]
        self.nHidden = settings["nHidden"]
        self.nOut = settings["nOut"]
        #以下参数可以由系统随机生成
        self.errlist = []
        self.dataMat = 0
        self.classLabels = 0
        self.nSampNum = 0
        self.SampDim = 0

        # 修正隐含层的权重计算公式
        # self.hi_wb = self.hi_wb + (1.0 - self.mac) * self.eta * dhi_wb + self.mc * dhi_wbOld

    # the active function
    def logistic(self, net):
        print "Logistic function been called..."

    # the derivation of the active function
    def dlogit(self, net):
        pass

    # 矩阵各元素的平方之和,用于计算惩罚因素，在反向传播时作为参数修改的依据
    def errorfunc(self, inX):
        pass

    # 数据归一化函数
    def normalize(self, dataMat):
        pass

    # load data
    def loadDataSet(self, fileName):
        pass

    # add a new colume
    def addcol(self, matrix1, matrix2):
        pass

    # initiate the hidden layer
    def init_hiddenWB(self):
        pass

    # train the network with back propogation protocol
    def bpTrain(self):
        pass

    # define the classifier of the BP network
    def BPClassfier(self, start, end, steps = 30):
        pass

    # draw the classify line after the network been trained
    def classifyLine(self, plt, x, z):
        pass

    # draw the tendency line with the ability to adjust the colors
    def TrendLine(self, plt, color = 'r'):
        pass

    # draw the classify points
    def drawClassScatter(self, plt):
        pass

# testing code block, should be removed after the network been finished.
test = BPNet({
    "test1":"test1",
    "test2":"test2",
    "test3":"test3"
})

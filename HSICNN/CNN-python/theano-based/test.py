import random
import copy
import numpy
import scipy.io as sio
import theano
import theano.tensor as T
import layer
import tool

def buildMode(inputNodes, outputNodes, params_fileName='params.mat', structure_fileName='structure.txt'):
    rng = numpy.random.RandomState(23455)

    params = tool.loadParams(params_fileName)
    convDims, convNodes, convKernels, convFilters, convPools, convLayers, fullNodes, fullLayers = tool.loadStructure(structure_fileName)

    x = T.matrix('x')
    y = T.ivector('y')

    layeri = None
    kernels = 1
    inputNodes = convNodes
    print inputNodes
    input = x.reshape((1, kernels, inputNodes, convDims == 2 and inputNodes or 1))
    for i in xrange(len(convLayers)):
        layeri = convLayers[i](rng=rng, input=input, 
                               image_shape=(1, kernels, inputNodes, convDims == 2 and inputNodes or 1), 
                               filter_shape=(convKernels[i], kernels, convFilters[i], convDims == 2 and convFilters[i] or 1), 
                               pool_shape=(convPools[i], convDims == 2 and convPools[i] or 1), 
                               W=params[2*i], b=params[2*i+1][0,:])
        kernels = convKernels[i]
        inputNodes = (inputNodes - convFilters[i] + 1) / convPools[i]
        print inputNodes
        input = layeri.output

    inputNodes = kernels * inputNodes * (convDims == 2 and inputNodes or 1)
    print inputNodes
    input = input.flatten(2)

    for i in xrange(len(fullLayers)):
        layeri = fullLayers[i](rng=rng, input=input, 
                               n_in=inputNodes, n_out=fullNodes[i], 
                               W=params[2*(len(convLayers)+i)], b=params[2*(len(convLayers)+i)+1][0,:])
        inputNodes = fullNodes[i]
        print inputNodes
        input = layeri.output

    return theano.function([x], [layeri.y_pred[0], layeri.output[0].max()])

def loadData(dataFile, typeId = -1):
    data = sio.loadmat(dataFile)

    DataTest = data['DataTest']
    test_set_x = tool.normalizeNdarray(DataTest)
    test_set_x = numpy.asarray(test_set_x, dtype=theano.config.floatX)
    CTest = data['CTest'][0,:]
    test_set_y = numpy.ndarray(0)
    for i in xrange(CTest.shape[0]):
        temp = numpy.ndarray(CTest[i])
        for j in xrange(CTest[i]):
            if typeId == -1:
                temp[j] = i
            elif typeId == i:
                temp[j] = 0
            else:
                temp[j] = 1
        test_set_y = numpy.hstack((test_set_y, temp))
    test_set_y = numpy.asarray(test_set_y, dtype='int32')
    return test_set_x, test_set_y

if __name__ == '__main__':
    #'U_PaviaReducedData1960_10.mat', 'VegetationReducedData1500_10.mat', 'Indian_pines_ReducedData_200_9.mat', 'Salinas_ReducedData_200_16.mat', 'Salinas_ReducedData_600_16.mat'
    test_set_x, test_set_y = loadData('Indian_pines_ReducedData.mat', -1)
    inputNodes = test_set_x.shape[1]
    outputNodes = test_set_y.max()+1
    Detect_model = buildMode(inputNodes, outputNodes)

    ok = 0
    sum = 0
    typeOk = numpy.zeros((outputNodes, outputNodes), dtype='int32')
    typeSum = numpy.zeros(outputNodes, dtype='int32')
    datas = [[] for i in xrange(outputNodes)]
    for i in xrange(outputNodes):
        for j in xrange(test_set_x.shape[0]):
            if test_set_y[j] == i:
                [label, prob] = Detect_model(test_set_x[j:j+1])
                typeOk[i][label] = typeOk[i][label] + 1
                typeSum[i] = typeSum[i] + 1
                datas[label].append(test_set_x[j])
        ok = ok + typeOk[i][i]
        sum = sum + typeSum[i]
    #for i in xrange(outputNodes):
    #    tool.showData(datas[i], i)
    for i in xrange(outputNodes):
        for j in xrange(outputNodes):
            print '%8.4f' %(100.0 * typeOk[i][j] / typeSum[i]),
        print ''
    print 'rate: %8.4f' %(100.0 * ok / sum)

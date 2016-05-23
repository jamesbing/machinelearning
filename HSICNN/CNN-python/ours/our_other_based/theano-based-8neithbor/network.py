import os
import sys
import time
import copy
import numpy
import theano
import theano.tensor as T
import tool
import layer
import Keyboard

def buildMode(train_set_x, train_set_y, valid_set_x, valid_set_y, test_set_x, test_set_y, 
              batch_size, bcontinue_train=False, previous_params=None, 
              convDims=None, convNodes=None, convKernels=None, convFilters=None, convPools=None, convLayers=None, 
              fullNodes=None, fullLayers=None):
    assert convDims == 1 or convDims == 2

    rng = numpy.random.RandomState(23455)

    index = T.lscalar()
    rate = T.fscalar()
    x = T.matrix('x')
    y = T.ivector('y')

    layeri = None
    kernels = 1
    inputNodes = convNodes
    print inputNodes
    input = x.reshape((batch_size, kernels, inputNodes, convDims == 2 and inputNodes or 1))
    params = []
    for i in xrange(len(convLayers)):
        if bcontinue_train:
            layeri = convLayers[i](rng=rng, input=input, 
                                   image_shape=(batch_size, kernels, inputNodes, convDims == 2 and inputNodes or 1), 
                                   filter_shape=(convKernels[i], kernels, convFilters[i], convDims == 2 and convFilters[i] or 1), 
                                   pool_shape=(convPools[i], convDims == 2 and convPools[i] or 1), 
                                   W=previous_params[2*i], b=previous_params[2*i+1][0,:])
        else:
            layeri = convLayers[i](rng=rng, input=input, 
                               image_shape=(batch_size, kernels, inputNodes, convDims == 2 and inputNodes or 1), 
                               filter_shape=(convKernels[i], kernels, convFilters[i], convDims == 2 and convFilters[i] or 1), 
                               pool_shape=(convPools[i], convDims == 2 and convPools[i] or 1))
        kernels = convKernels[i]
        inputNodes = (inputNodes - convFilters[i] + 1) / convPools[i]
        print inputNodes
        input = layeri.output
        params += layeri.params

    inputNodes = kernels * inputNodes * (convDims == 2 and inputNodes or 1)
    print inputNodes
    input = input.flatten(2)

    for i in xrange(len(fullLayers)):
        if bcontinue_train:
            layeri = fullLayers[i](rng=rng, input=input, 
                                   n_in=inputNodes, n_out=fullNodes[i], 
                                   W=previous_params[2*(len(convLayers)+i)], b=previous_params[2*(len(convLayers)+i)+1][0,:])
        else:
            layeri = fullLayers[i](rng=rng, input=input, 
                                   n_in=inputNodes, n_out=fullNodes[i])
        inputNodes = fullNodes[i]
        print inputNodes
        input = layeri.output
        params += layeri.params

    cost = layeri.negative_log_likelihood(y)
    grads = T.grad(cost, params)
    updates = []
    for param_i, grad_i in zip(params, grads):
        updates.append((param_i, param_i - rate * grad_i))

    test_model = theano.function(inputs=[index], 
                                 outputs=layeri.errors(y), 
                                 givens={x: test_set_x[index * batch_size: (index + 1) * batch_size], 
                                         y: test_set_y[index * batch_size: (index + 1) * batch_size]})
    validate_model = theano.function(inputs=[index], 
                                     outputs=layeri.errors(y),
                                     givens={x: valid_set_x[index * batch_size: (index + 1) * batch_size],
                                             y: valid_set_y[index * batch_size: (index + 1) * batch_size]})
    train_model = theano.function(inputs=[index, rate], 
                                  outputs=cost, 
                                  updates=updates,
                                  givens={x: train_set_x[index * batch_size: (index + 1) * batch_size],
                                          y: train_set_y[index * batch_size: (index + 1) * batch_size]},
                                  allow_input_downcast=True)

    return train_model, validate_model, test_model, params

def train(bcontinue_train=False, params_fileName='params.mat', structure_fileName='structure.txt', learning_rate=0.01, batch_size=9, n_epochs=1000000):#8*11*17 = 1496, 3*12*41 = 1476
    #'U_PaviaReducedData1960_10.mat', 'VegetationReducedData1500_10.mat', 'PaviaU_ReducedData.mat', 'Indian_pines_ReducedData_200_9.mat', 'Salinas_ReducedData_200_16.mat', 'Salinas_ReducedData_600_16.mat'
    #'U_PaviaReducedData1960_10.mat', 'PaviaU_ReducedData.mat', 'Salinas_ReducedData_200_16.mat'
    datasets = tool.loadData('newKSC1N8.mat', -1, False)
    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]

    n_train_batches = train_set_x.get_value(borrow=True).shape[0] / batch_size
    n_valid_batches = valid_set_x.get_value(borrow=True).shape[0] / batch_size
    n_test_batches = test_set_x.get_value(borrow=True).shape[0] / batch_size

    print '... building the model'
    if bcontinue_train:
        previous_params = tool.loadParams(params_fileName)
        convDims, convNodes, convKernels, convFilters, convPools, convLayers, fullNodes, fullLayers = tool.loadStructure(structure_fileName)
    else:
        previous_params = None
        convDims = len(train_set_x.get_value(borrow=True).shape) - 1
        convNodes = train_set_x.get_value(borrow=True).shape[1]
        convKernels = [30]
        convFilters = [21]
        convPools = [5]
        convLayers = [layer.ConvPoolLayer]
        fullNodes = [100, train_set_y.get_value(borrow=True).max()+1]
        fullLayers = [layer.FullLayer, layer.SoftmaxLayer]
        '''convKernels = [30]
        convFilters = [14]
        convPools = [3]
        convLayers = [layer.ConvPoolLayer]
        fullNodes = [100, train_set_y.get_value(borrow=True).max()+1]
        fullLayers = [layer.FullLayer, layer.SoftmaxLayer]'''
        # ok NN
        # deepCNN
        # ok class accuracy in column figure
        # dataRateDistribution all in Pavia
        # area cluster image
        # testing time
        '''convKernels = []
        convFilters = []
        convPools = []
        convLayers = []
        fullNodes = [100, 50, train_set_y.get_value(borrow=True).max()+1]
        fullLayers = [layer.FullLayer, layer.FullLayer, layer.SoftmaxLayer]'''
        '''convKernels = [20, 30]
        convFilters = [9, 5]
        convPools = [2, 2]
        convLayers = [layer.ConvPoolLayer, layer.ConvPoolLayer]
        fullNodes = [100, train_set_y.get_value(borrow=True).max()+1]
        fullLayers = [layer.FullLayer, layer.SoftmaxLayer]'''

    train_model, validate_model, test_model, params = buildMode(train_set_x, train_set_y, valid_set_x, valid_set_y, test_set_x, test_set_y, 
                                                                batch_size, bcontinue_train, previous_params, 
                                                                convDims, convNodes, convKernels, convFilters, convPools, convLayers, 
                                                                fullNodes, fullLayers)

    print '... training the model'
    times = [0.0]
    accus = [0.0]
    costs = [0.0]
    epoch = 0
    cost = 1.0
    test_score = 0.0
    best_validation_loss = numpy.inf
    b_save_best_params = False
    best_params = None
    show_valid = False
    start_time = time.clock()
    Keyboard.StartKeyboardListener()
    while (epoch < n_epochs) and (cost > 0.0001):
        epoch = epoch + 1
        show_valid = False
        key = Keyboard.KeyDown()
        if key == 'q':
            break
        elif key == '+':
            learning_rate = learning_rate * 1.2
        elif key == '-':
            learning_rate = learning_rate / 1.2
        elif key == 'c':
            b_save_best_params = not b_save_best_params
            print 'b_save_best_params: ', b_save_best_params
        elif key == 'x':
            tool.saveParams(params_fileName, params)
            tool.saveStructure(structure_fileName, convDims, convNodes, convKernels, convFilters, convPools, convLayers, fullNodes, fullLayers)
            print 'save_cur_params'
        elif key == 's':
            tool.saveParams(params_fileName, best_params)
            tool.saveStructure(structure_fileName, convDims, convNodes, convKernels, convFilters, convPools, convLayers, fullNodes, fullLayers)
            print('test best error: %f %%' %(test_score * 100.))
            show_valid = True

        cost = 0
        for minibatch_index in xrange(n_train_batches):
            cost += train_model(minibatch_index, learning_rate)
        cost /= n_train_batches

        if epoch % 100 != 1 and not show_valid:
            print('epoch %i, batches %i, rate %.4f, cost %.4f' %(epoch, n_train_batches, learning_rate, cost))
            continue

        validation_losses = [validate_model(i)
                             for i in xrange(n_valid_batches)]
        this_validation_loss = numpy.mean(validation_losses)

        print('epoch %i, batches %i, rate %.4f, cost %.4f, validation error %.4f %%' % \
              (epoch, n_train_batches, learning_rate, cost, this_validation_loss * 100.))

        if this_validation_loss < best_validation_loss:
            best_validation_loss = this_validation_loss
            #test_losses = [test_model(i)
            #               for i in xrange(n_test_batches)]
            #test_score = numpy.mean(test_losses)
            test_losses = validation_losses
            test_score = this_validation_loss
            best_params = copy.deepcopy(params)
            times.append((time.clock() - start_time) / 60.0)
            accus.append(100.0 * (1.0 - test_score))
            costs.append(cost)
            if b_save_best_params:
                tool.saveParams(params_fileName, best_params)
                tool.saveStructure(structure_fileName, convDims, convNodes, convKernels, convFilters, convPools, convLayers, fullNodes, fullLayers)

            print(('     epoch %i, batches %i, time %.2f, test error of best'
                   ' model %.4f %%') %
                   (epoch, n_train_batches, time.clock() - start_time, 
                   test_score * 100.))
    Keyboard.StopKeyboardListener()
    end_time = time.clock()

    print(('Optimization complete with best validation score of %f %%,'
           'with test performance %f %%') %
                 (best_validation_loss * 100., test_score * 100.))
    print 'The code run for %d epochs, with %f epochs/sec' % (
        epoch, 1. * epoch / (end_time - start_time))
    print >> sys.stderr, ('The code for file ' +
                          os.path.split(__file__)[1] +
                          ' ran for %.1fs' % ((end_time - start_time)))

    tool.saveParams(params_fileName, best_params)
    tool.saveStructure(structure_fileName, convDims, convNodes, convKernels, convFilters, convPools, convLayers, fullNodes, fullLayers)

    tool.saveList('./times.txt', times)
    tool.saveList('./accus.txt', accus)
    tool.saveList('./costs.txt', costs)
    times = tool.loadList('./times.txt')
    accus = tool.loadList('./accus.txt')
    costs = tool.loadList('./costs.txt')

#!/usr/bin/env python
# coding=utf-8

import scipy.io as sio
import numpy

import theano
import theano.tensor as T

###################
#Used to load data#
###################
def load_data(dataset_path):
    data = sio.loadmat(dataset_path)
#    train_data = np.array(data['DataTr'],dtype = 'float32')
    train_data = data['DataTr']
    train_label = data['CIdTr']
    
    train_set = (train_data, train_label)

#   valid_data = np.array(data['DataVa'],dtype = 'float32')
    valid_data = data['DataVa']
    valid_label = data['CIdVa']
    
    valid_set = (valid_data, valid_label)

#   test_data = np.array(data['DataTe'],dtype = 'float32')
    test_data = data['DataTe']
    test_label = data['CIdTe']
    
    test_set = (test_data, test_label)

    ######################################################
    #define a sub function to prepare for the GPU purpose#
    ######################################################
    def shared_dataset(data_xy, borrow = True):
        data_x, data_y = data_xy
#        print (data_x)
#        print (data_y)
        shared_x = theano.shared(value = numpy.asarray(data_x,
                                              dtype=theano.config.floatX),
                                borrow = borrow)
        shared_y = theano.shared(value = numpy.asarray(data_y,
                                              dtype='int32'),
                                borrow = borrow)
        return shared_x, shared_y
    #the end of the defination of inside fucntion

    test_set_x, test_set_y = shared_dataset(test_set)
    valid_set_x, valid_set_y = shared_dataset(valid_set)
    train_set_x, train_set_y = shared_dataset(train_set)
    
    result_data_sets = [(train_set_x, train_set_y),
                        (valid_set_x, valid_set_y),
                        (test_set_x, test_set_y)]

    return result_data_sets
#    return train_set, valid_set, test_set

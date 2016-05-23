import cPickle
import gzip
import os
import sys
import time
import copy
import scipy.io as sio
import numpy
import random
import theano
import theano.tensor as T
from theano.tensor.signal import downsample
from theano.tensor.nnet import conv

class ConvPoolLayer(object):

    def __init__(self, rng, input, image_shape, filter_shape, pool_shape, W=None, b=None):
#        assert image_shape[1] == filter_shape[1]
        filter_shape = 5
        fan_in = numpy.prod(filter_shape[1:])
        fan_out = (filter_shape[0] * numpy.prod(filter_shape[2:]) / numpy.prod(pool_shape))
        if W == None:
            self.W = theano.shared(numpy.asarray(rng.uniform(low=-numpy.sqrt(6. / (fan_in + fan_out)), 
                                                             high=+numpy.sqrt(6. / (fan_in + fan_out)), 
                                                             size=filter_shape),
                                                dtype=theano.config.floatX),
                                   name='W', borrow=True)
        else:
            self.W = theano.shared(W, name='W', borrow=False)
        if b == None:
            self.b = theano.shared(value=numpy.zeros((filter_shape[0],), 
                                                     dtype=theano.config.floatX), 
                                   name='b', borrow=True)
        else:
            self.b = theano.shared(b, name='b', borrow=False)

        conv_out = conv.conv2d(input=input, filters=self.W, 
                               image_shape=image_shape, filter_shape=filter_shape)
        pool_out = downsample.max_pool_2d(input=conv_out, 
                                          ds=pool_shape, ignore_border=True)
        self.output = T.tanh(pool_out + self.b.dimshuffle('x', 0, 'x', 'x'))
        self.params = [self.W, self.b]

class FullLayer(object):

    def __init__(self, rng, input, n_in, n_out, W=None, b=None):
        if W == None:
            self.W = theano.shared(value=numpy.asarray(rng.uniform(low =-numpy.sqrt(6. / (n_in + n_out)), 
                                                                   high=+numpy.sqrt(6. / (n_in + n_out)), 
                                                                   size=(n_in, n_out)), 
                                                       dtype=theano.config.floatX), 
                                   name='W', borrow=True)
        else:
            self.W = theano.shared(W, name='W', borrow=False)
        if b == None:
            self.b = theano.shared(value=numpy.zeros((n_out,), 
                                                     dtype=theano.config.floatX), 
                                   name='b', borrow=True)
        else:
            self.b = theano.shared(b, name='b', borrow=False)

        self.output = T.tanh(T.dot(input, self.W) + self.b)
        self.params = [self.W, self.b]

class SoftmaxLayer(object):

    def __init__(self, rng, input, n_in, n_out, W=None, b=None):
        if W == None:
            self.W = theano.shared(value=numpy.asarray(rng.uniform(low =-numpy.sqrt(6. / (n_in + n_out)), 
                                                                   high=+numpy.sqrt(6. / (n_in + n_out)), 
                                                                   size=(n_in, n_out)), 
                                                       dtype=theano.config.floatX), 
                                   name='W', borrow=True)
        else:
            self.W = theano.shared(W, name='W', borrow=False)
        if b == None:
            self.b = theano.shared(value=numpy.zeros((n_out,),
                                                     dtype=theano.config.floatX),
                                   name='b', borrow=True)
        else:
            self.b = theano.shared(b, name='b', borrow=False)
        self.output = T.nnet.softmax(T.dot(input, self.W) + self.b)
        self.y_pred = T.argmax(self.output, axis=1)
        self.params = [self.W, self.b]

    def negative_log_likelihood(self, y):
        return -T.mean(T.log(self.output)[T.arange(y.shape[0]), y]) # + lambda / 2.0 * T.dot(self.W, self.W) / self.W.shape[0] / self.W.shape[1]

    def errors(self, y):
        if y.ndim != self.y_pred.ndim:
            raise TypeError('y should have the same shape as self.y_pred',
                ('y', target.type, 'y_pred', self.y_pred.type))
        if y.dtype.startswith('int'):
            return T.mean(T.neq(self.y_pred, y))
        else:
            raise NotImplementedError()

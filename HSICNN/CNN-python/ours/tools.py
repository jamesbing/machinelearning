#!/usr/bin/env python
# coding=utf-8

import scipy.io as sio
import numpy as np

###################
#Used to load data#
###################
def load_data(dataset_path):
    data = sio.loadmat(dataset_path)
    train_data = np.array(data['DataTr'],dtype = 'float32')
    train_label = data['CIdTr']
    train_set = (train_data, train_label)

    valid_data = np.array(data['DataVa'],dtype = 'float32')
    valid_label = data['CIdVa']
    valid_set = (valid_data, valid_label)

    test_data = np.array(data['DataTe'],dtype = 'float32')
    test_label = data['CIdTe']
    test_set = (test_data, test_label)

    return train_set, valid_set, test_set

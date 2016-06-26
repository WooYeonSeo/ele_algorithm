"""
"""
import os
import sys
import timeit
import cPickle

import numpy

import theano
import call as c
import theano.tensor as T
from theano.sandbox.rng_mrg import MRG_RandomStreams

from logistic_sgd import LogisticRegression, load_data
#from mlp import HiddenLayer
#from rbm import RBM



def predict(call):
    """
    An example of how to load a trained model and use it
    to predict labels.
    """

    # load the saved model
    classifier = cPickle.load(open('best_model.pkl'))

    # compile a predictor function
    predict_model = theano.function(
        inputs=[classifier.input],
        outputs=classifier.y_pred)



    # We can test it on some examples from test test
    """
    dataset='sevenLast.csv.pkl.gz'
    datasets = load_data(dataset)
    test_set_x, test_set_y = datasets[2]
    test_set_x = test_set_x.get_value(borrow=True)


    print test_set_x[:1]
    """

    value =[]
    value.append(float(call.dbn_register_time))
    value.append(float(call.destination))
    value.append(float(call.day_of_week))
    value.append(float(call.iserror))

    value.append(float(call.isup))
    value.append(float(call.weekend))
    value.append(float(call.register_time_15min))

    print [value]
    predicted_values = predict_model([value])

    print ("Predicted values for the first 10 examples in test set:")
    print predicted_values[0]
    return predicted_values[0]


if __name__ == '__main__':
    #test_DBN()
    #def __init__(self, register_time, departure_floor,destination_floor, isup, passenger, dbn_register_time, day_of_week, iserror, weekend, register15min):
    new_call = c.Call('2015-11-18 05:02:19.2',1,3,1,3,'18139','4','5',0,0)
    predict(new_call)

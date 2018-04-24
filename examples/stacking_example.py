# -*- coding:utf-8 -*-

from simple_ml.classify_data import *
from simple_ml.ensemble import Stacking
from simple_ml.data_handle import train_test_split
from simple_ml import *

def wine_example():
    x, y = get_wine()
    x = x[(y == 0) | (y == 1)]
    y = y[(y == 0) | (y == 1)]

    model_list = [LogisticRegression(), NaiveBayes()]

    stack = Stacking(model_list, k_folder=3)
    stack.fit(x, y)
    print(stack.predict(x))
    stack.classify_plot(x, y)

if __name__ == '__main__':
    wine_example()
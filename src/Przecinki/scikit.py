#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cross_validation import cross_val_predict
from sklearn import linear_model
from sklearn import datasets

X = []
Y = []
for line in sys.stdin:
    line = line.rstrip()
    X.append([len(line.split())])
    Y.append(line.count(","))

lr = linear_model.LinearRegression()

predicted = cross_val_predict(lr, X, Y)

FILE = open(sys.argv[1], "r")
X_TEST = []
Y_TEST = []
for line in FILE:
    line = line.rstrip()
    Y_TEST.append(line.count(","))
    line = line.replace(",", "")
    X_TEST.append([len(line.split())])
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print "Coefficients: ", regr.coef_
print "Residual sum of squares: %.2f" % np.mean((regr.predict(X_TEST) - Y_TEST) ** 2)
print "Variance score: %.2f" % regr.score(X_TEST, Y_TEST)
plt.scatter(X_TEST, Y_TEST,  color='black')
plt.plot(X_TEST, regr.predict(X_TEST), color='green', linewidth=2)
plt.xticks(())
plt.yticks(())
plt.show()

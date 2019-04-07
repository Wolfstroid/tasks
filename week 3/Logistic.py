import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


def cac_h(X, theta):
    z = np.dot(X, theta)
    h = 1/(1+math.pow(math.e, z[0]))
    return h


def logisticRegression(test_X, train_X, train_y, alpha, times):
    theta = np.array(train_X.shape[1]*[[0.]])

    n = 0
    while n < times:
        theta_cac = theta
        m = 0
        while m < train_X.shape[1]:
            temp = 0
            i = 0
            while i < train_X.shape[0]:
                temp += (cac_h(train_X[i], theta)-train_y[i])*train_X[i][m]
                i += 1
            theta_cac[m][0] = temp*alpha
            m += 1
        theta = theta + theta_cac
        n += 1
    

    predict_y = np.array(test_X.shape[0]*[[0.]])
    n = 0
    while n < test_X.shape[0]:
        predict_y[n] = cac_h(test_X[n], theta)
        n += 1
    return predict_y


def get_recall(y_predict, y_test):
    positive = 0
    true_positive = 0
    for m, n in zip(y_predict, y_test):
        if n == 1:
            positive += 1
            if m == 1:
                true_positive += 1
    recall = true_positive/positive
    return recall


def get_acurracy(y_predict, y_test):
    true_number = 0
    for m, n in zip(y_predict, y_test):
        if m == n:
            true_number += 1
    acurracy = true_number / len(y_test)
    return acurracy


diabete = pd.read_csv("/home/zhoupu/tasks/week 3/diabetes.csv").values
X = diabete[:, :diabete.shape[1]-1]
y = diabete[:, -1:]
X = preprocessing.scale(X)
train_X, test_X, train_y, test_y = train_test_split(X, y.astype(int), test_size = 0.3)

predict_y = logisticRegression(test_X, train_X, train_y, 0.001, 500)
predict_y = (predict_y + 0.5).astype(int)
print(predict_y.T-test_y.T)
print(get_acurracy(predict_y, test_y), get_recall(predict_y, test_y))

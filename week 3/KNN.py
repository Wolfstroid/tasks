import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


def predict(arr, train_X, train_y, k):
    dist = np.array(train_X.shape[0]*[[0.]])
    n = 0
    while n < train_X.shape[0]:
        dist[n] = np.linalg.norm(train_X[n]-arr)
        n += 1
    sortedDistIndices = np.argsort(dist.transpose())
    classCount = {}
    for i in range(k):
        classCount[train_y.astype(int)[sortedDistIndices[0][i]][0]] = classCount.get(train_y.astype(int)[sortedDistIndices[0][i]][0],0) + 1
    maxValue, maxKey = 0, 0
    for i in classCount:
        if classCount[i] > maxValue:
            maxValue = classCount[i]
            maxKey = i
    return maxKey


def knn(test_X, train_X, train_y, k):
    predict_y = np.array(test_X.shape[0]*[[0]])
    n = 0
    while n < test_X.shape[0]:
        predict_y[n] = predict(test_X[n], train_X, train_y, k)
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
train_X, test_X, train_y, test_y = train_test_split(X, y.astype(int), test_size=0.3)
for k in range(1, 51):
    predict_y = knn(test_X, train_X, train_y, k)
    print(k, ":", get_acurracy(predict_y, test_y), get_recall(predict_y, test_y))

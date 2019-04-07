import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


def cac(X_train, y_train, theta, n):
    j = 0
    h = np.dot(X_train[0], theta)
    j += (h-y_train[0])*X_train[i][n]
    j = - j / X_train.shape[0]
    return j

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3)

A = np.array(X_train.shape[0]*[[1]])
X_train = np.hstack((A, X_train))
theta = np.array(X_train.shape[1]*[[1]])
j = 0
for i in range(X_train.shape[0]):
    h = np.dot(X_train[i], theta)
    j += (h-y_train[i])*(h-y_train[i])
j = j / 2 / X_train.shape[0]
print(j)

for i in range(10):
    theta_cac = np.array(X_train.shape[1]*[[0.]])
    for n in range(X_train.shape[1]):
        theta_cac[n][0] = cac(X_train, y_train, theta, n)*0.00001
    theta = theta + theta_cac

j = 0
for i in range(X_train.shape[0]):
    h = np.dot(X_train[i], theta)
    j += (h-y_train[i])*(h-y_train[i])
j = j / 2 / X_train.shape[0]
print(j)


for i in range(20):
    theta_cac = np.array(X_train.shape[1]*[[0.]])
    for n in range(X_train.shape[1]):
        theta_cac[n][0] = cac(X_train, y_train, theta, n)*0.00001
    theta = theta + theta_cac

j = 0
for i in range(X_train.shape[0]):
    h = np.dot(X_train[i], theta)
    j += (h-y_train[i])*(h-y_train[i])
j = j / 2 / X_train.shape[0]
print(j)

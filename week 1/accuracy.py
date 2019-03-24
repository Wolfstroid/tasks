import numpy
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def get_acurracy(y_predict,y_test):
    true_number = 0
    for m,n in zip(y_predict,y_test):
        if m == n:
            true_number += 1
    acurracy = true_number / len(y_test)
    return acurracy

iris = load_iris()
X_train,X_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.3)
model = KNeighborsClassifier()
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
acurracy = get_acurracy(y_predict,y_test)
print(acurracy)
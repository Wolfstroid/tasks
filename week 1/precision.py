import numpy
from sklearn.datasets import load_breast_cancer
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def get_precison(y_predict,y_test):
    true_positive = 0
    predict_positive = 0
    for m,n in zip(y_predict,y_test):
        if m == 1:
            predict_positive += 1
            if n == 1:
                true_positive +=1
    precision = true_positive/predict_positive
    return precision

cancer_std = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer_std.data,cancer_std.target,test_size=0.3)
model = KNeighborsClassifier()
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
print(get_precison(y_predict,y_test))
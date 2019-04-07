import numpy
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

def get_recall(y_predict,y_test):
    positive = 0
    true_positive = 0
    for m,n in zip(y_predict,y_test):
        if n == 1:
            positive += 1
            if m == 1:
                true_positive +=1
    recall = true_positive/positive
    return recall

cancer_std = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer_std.data,cancer_std.target,test_size=0.3)
model = KNeighborsClassifier()
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
print(get_recall(y_predict,y_test))

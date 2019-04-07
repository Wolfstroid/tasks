import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
#part of feature works
titan = pd.read_csv('/home/zhoupu/tasks/week 2/train.csv')
titan.loc[titan['Sex']=='male','Sex']=0
titan.loc[titan['Sex']=='female','Sex']=1
titan['Embarked']=titan['Embarked'].fillna('S')
titan.loc[titan['Embarked']=='S','Embarked']=0
titan.loc[titan['Embarked']=='C','Embarked']=1
titan.loc[titan['Embarked']=='Q','Embarked']=2
titan.loc[titan['Cabin'].isnull(),'Cabin']=0
titan.loc[titan['Cabin']!=0,'Cabin']=1
predictors=titan[['Age','Pclass','Sex','SibSp','Parch','Fare','Embarked']]

known_age = predictors[predictors.Age.notnull()].values
unknown_age = predictors[predictors.Age.isnull()].values

X_train = known_age[:,1:]
X_train = preprocessing.scale(X_train)
y_train = known_age[:,0]

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train.astype(np.int32))

predictedAges = knn.predict(unknown_age[:,1::])

titan.loc[titan['Age'].isnull(),'Age']=predictedAges
print(titan)

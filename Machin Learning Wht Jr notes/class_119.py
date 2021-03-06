# -*- coding: utf-8 -*-
"""class-119.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19PmR5qSPTjJVDNfJYr-nkO5zu8wGL-cQ
"""

from google.colab import files
a = files.upload()

import pandas as pd

col_names = ['pregnant', 'glucose','bp','skin','insulin','bmi','pedigree','age','label']

df = pd.read_csv("class-119.csv", names=col_names).iloc[1:]
print(df.head())

features = ['pregnant', 'glucose','bp','insulin','bmi','pedigree','age']
X = df[features]
Y = df.label

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3, random_state=1)
 

clf = DecisionTreeClassifier()

clf = clf.fit(X_train,Y_train)

y_pred = clf.predict(X_test)
print("Accuracy: ",metrics.accuracy_score(Y_test, y_pred))

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()

export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names=features, class_names=['0','1'])
print(dot_data.getvalue())

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('dianetes.png')
Image(graph.create_png())

clf = DecisionTreeClassifier(max_depth=3)

clf = clf.fit(X_train,Y_train)

y_pred = clf.predict(X_test)
print("Accuracy: ",metrics.accuracy_score(Y_test, y_pred))

dot_data = StringIO()

export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names=features, class_names=['0','1'])

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('dianetes.png')
Image(graph.create_png())
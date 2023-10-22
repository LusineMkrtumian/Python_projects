from sklearn import preprocessing
import numpy as np

X_train = np.array([[1., -1., 2.],
                    [2., 0., 0.],
                    [0., 1., -1.]])
scaler = preprocessing.StandardScaler().fit(X_train)
scaler.mean_  # array([1. ..., 0. ..., 0.33...])
scaler.scale_  # array([0.81..., 0.81..., 1.24...])
X_scaled = scaler.transform(X_train)
'''array([[ 0.  ..., -1.22...,  1.33...],
       [ 1.22...,  0.  ..., -0.26...],
       [-1.22...,  1.22..., -1.06...]])'''
X_scaled.mean(axis=0)  # array([0., 0., 0.])
X_scaled.std(axis=0)  # array([1., 1., 1.])

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(X_train, y_train)  # apply scaling on training data
'''Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression())])'''

pipe.score(X_test, y_test)  # 0.96, apply scaling on testing data, without leaking training data.

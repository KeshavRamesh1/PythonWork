import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from tpot import TPOTClassifier

df = pd.read_csv('yygsdata.csv')
target_column = ['extentcapitalism']
predictors = list(set(list(df.columns))-set(target_column))
X = df[predictors].values
y = df[target_column].values.ravel()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
print(X_train.shape)
print(X_test.shape)

pipeline_optimizer = TPOTClassifier(generations=100, population_size=100, cv=5, random_state=42, verbosity=2, early_stop=10)
print(y_train)
pipeline_optimizer.fit(X_train, y_train)
print(pipeline_optimizer.score(X_test, y_test))
pipeline_optimizer.export('yale_data.py')
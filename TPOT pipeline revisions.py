#example using my extenthumanities optimized pipeline

import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectPercentile, f_regression
from sklearn.linear_model import LassoLarsCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from tpot.export_utils import set_param_recursive

#ADD THESE 2 LINES!
from sklearn import metrics
import math

#Fill in same CSV as before. Remove the "SEPARATOR" line so that your line is identical to this one.
tpot_data = pd.read_csv('assessmentexthumanities.csv', dtype=np.float64)

#Put in the target variable in place of "target"
features = tpot_data.drop('extenthumanities', axis=1)

#Put in the target variable in place of "target"
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['extenthumanities'], random_state=42)

exported_pipeline = make_pipeline(
    SelectPercentile(score_func=f_regression, percentile=2),
    LassoLarsCV(normalize=True)
)
set_param_recursive(exported_pipeline.steps, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
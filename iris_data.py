from sklearn.datasets import load_iris
import pandas as pd

#loading iris dataset
iris_data = load_iris()

#variable names
keys = iris_data.keys()
features = iris_data['data']
features_shape = iris_data['data'].shape
target = iris_data['target']
target_shape = iris_data['target'].shape
target_names = iris_data['target_names']
features_names = iris_data['feature_names']
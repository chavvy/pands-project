#loading iris dataset
from sklearn.datasets import load_iris

def load_iris_data():
    iris_data = load_iris()
    return {
        "data": iris_data.data,
        "target": iris_data.target,
        "target_names": iris_data.target_names,
        "feature_names": iris_data.feature_names
    }
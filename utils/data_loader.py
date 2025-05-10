#loading dataset
from sklearn.datasets import load_iris

def load_data():
    dataset = load_iris()
    return {
        "data": dataset.data,
        "target": dataset.target,
        "target_names": dataset.target_names,
        "feature_names": dataset.feature_names
    }
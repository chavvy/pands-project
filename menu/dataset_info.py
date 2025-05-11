from utils.data_loader import load_data
from utils.data_functions import data_info

iris_data = load_data()
features_names = iris_data["feature_names"]
features = iris_data["data"]
features_shape = iris_data["data"].shape
target = iris_data['target']
target_shape = iris_data['target'].shape
target_names = iris_data['target_names']


#menu for the user to choose info
def show_summary_menu():
    print("\nDataset Information\n====")
    print("1. Features")
    print("2. Features Shape")
    print("3. Features Names")
    print("4. Target")
    print("5. Target Shape")
    print("6. Target Names")
    print("x. Return to menu")


data_info("Features", features)
data_info("Features Shape", features_shape)
data_info("Features Names", features_names)
data_info("Target", target)
data_info("Target Shapes", target_shape)
data_info("Target Names", target_names)
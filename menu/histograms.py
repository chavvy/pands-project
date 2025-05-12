#for the histograms menu, the plan will be to have it dynamically generated based on the dataset being used
#the goal for this is that it can be used with various datasets and not just the iris dataset
from utils import load_data, plot_histogram

dataset = load_data()
features_names = dataset["feature_names"]
features = dataset["data"]
features_shape = dataset["data"].shape
target = dataset['target']
target_shape = dataset['target'].shape
target_names = dataset['target_names']

def show_histogram_menu():

    while True:
        print("\nChoose a feature to display the histogram:")
        
        #dynamically generating the menu based on the features names
        #similar to the data summary function but only getting the names this time
        for i, feature in enumerate(features_names, 1):
            print(f"{i}. {feature}")
        
        print("x. Return to menu")

        choice = input("Enter the number of your choice: ").strip()
        
        if choice == 'x':
            print("Exiting histogram menu...")
            break
        
        #ensure the choice is valid
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(features_names):
                selected_feature = features_names[choice - 1]
                plot_histogram(features, features_names, selected_feature)
            else:
                print("Invalid choice, please try again.")
        else:
            print("Error: Please select a valid option.")

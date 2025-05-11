from utils import load_data, data_features_summary

dataset = load_data()
features = dataset['data']
features_name = dataset['feature_names']

#menu for the user to choose a summary
def show_summary_menu():
    print("\nSummarise Data\n====")
    print("1. Mean")
    print("2. Minimum")
    print("3. Maximum")
    print("4. Median")
    print("5. Standard Deviation")
    print("6. Show all summaries")
    print("x. Return to menu")

def summarise_data():
    while True:
        show_summary_menu()  #display the menu
        choice = input("Enter the number of your choice: ").strip().lower()  #get user's choice
        
        if choice == '1':
            data_features_summary(features, features_name, "mean")
        elif choice == '2':
            data_features_summary(features, features_name, "min")
        elif choice == '3':
            data_features_summary(features, features_name, "max")
        elif choice == '4':
            data_features_summary(features, features_name, "median")
        elif choice == '5':
            data_features_summary(features, features_name, "std")
        elif choice == '6':
            data_features_summary(features, features_name, "mean")
            data_features_summary(features, features_name, "min")
            data_features_summary(features, features_name, "max")
            data_features_summary(features, features_name, "max")
            data_features_summary(features, features_name, "median")
            data_features_summary(features, features_name, "std")
        elif choice == 'x':
            print("Returning to menu...")
            return  #exit the loop and return to menu
        else:
            print("Error: Please select a valid option.")
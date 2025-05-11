from utils import load_data, data_info

iris_data = load_data()
features_names = iris_data["feature_names"]
features = iris_data["data"]
features_shape = iris_data["data"].shape
target = iris_data['target']
target_shape = iris_data['target'].shape
target_names = iris_data['target_names']

#menu for the user to choose info
def show_info_menu():
    print("\nDataset Information\n====")
    print("1. Features")
    print("2. Features Shape")
    print("3. Features Names")
    print("4. Target")
    print("5. Target Shape")
    print("6. Target Names")
    print("x. Return to menu")

def show_data_info():
    while True:
        show_info_menu()  #display the menu
        choice = input("Enter the number of your choice: ").strip().lower()  #get user's choice
        
        if choice == '1':
            data_info("Features", features)
        elif choice == '2':
            data_info("Features Shape", features_shape)
        elif choice == '3':
            data_info("Features Names", features_names)
        elif choice == '4':
            data_info("Target", target)
        elif choice == '5':
            data_info("Target Shapes", target_shape)
        elif choice == '6':
            data_info("Target Names", target_names)
        elif choice == 'x':
            print("Returning to menu...")
            return  #exit the loop and return to menu
        else:
            print("Error: Please select a valid option.")
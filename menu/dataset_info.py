import os
from utils import load_data, data_info, save_output

dataset = load_data()
features_names = dataset["feature_names"]
features = dataset["data"]
features_shape = dataset["data"].shape
target = dataset['target']
target_shape = dataset['target'].shape
target_names = dataset['target_names']

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
            dataset_info = data_info("Features", features)
            dataset_info_type = "features"
        elif choice == '2':
            dataset_info = data_info("Features Shape", features_shape)
            dataset_info_type = "features_shape"
        elif choice == '3':
            dataset_info = data_info("Features Names", features_names)
            dataset_info_type = "features_names"
        elif choice == '4':
            dataset_info = data_info("Target", target)
            dataset_info_type = "target"
        elif choice == '5':
            dataset_info = data_info("Target Shapes", target_shape)
            dataset_info_type = "target_shapes"
        elif choice == '6':
            dataset_info = data_info("Target Names", target_names)
            dataset_info_type = "target_names"
        elif choice == 'x':
            print("Returning to menu...")
            return  #exit the loop and return to menu
        else:
            print("Error: Please select a valid option.")
                
        #filename based on the user's choice
        filename = f"{dataset_info_type}.txt"

        #giving the user the option to save the dataset info or not
        save_choice = input(f"\nDo you want to save the {dataset_info_type} information? (yes/no): ").strip().lower()

        if save_choice == "yes":
            #checking if the file exists in the output folder
            filepath = os.path.join("output", filename)

            if os.path.exists(filepath):
                #if the file exists, prompt the user if they want to overwrite it
                overwrite = input(f"\nThe file '{filename}' already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
                if overwrite == "yes":
                    save_output(dataset_info, filename, folder="output")
                else:
                    input("\nSave cancelled, press enter to return to menu...")
            #otherwise, just save the file anyways
            else:
                save_output(dataset_info, filename, folder="output")

        else:
            print(f"\n{dataset_info_type.capitalize()} information not saved.")
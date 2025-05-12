from utils import load_data, data_features_summary, data_features_summary_all, save_output

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
        #turning the function into a variable, and adding another variable to handle saving
        #the extra variable summary_type is for naming the file
        if choice == '1':
            summary = data_features_summary(features, features_name, "mean")
            summary_type = "mean"
        elif choice == '2':
            summary = data_features_summary(features, features_name, "min")
            summary_type = "min"
        elif choice == '3':
            summary = data_features_summary(features, features_name, "max")
            summary_type = "max"
        elif choice == '4':
            summary = data_features_summary(features, features_name, "median")
            summary_type = "median"
        elif choice == '5':
            summary = data_features_summary(features, features_name, "std")
            summary_type = "std"
        elif choice == '6':
            summary = data_features_summary_all(features, features_name)
            summary_type = "all_in_one"
        elif choice == 'x':
            print("Returning to menu...")
            return  #exit the loop and return to menu
        else:
            print("\nError: Please select a valid option.")

        #filename based on the user's choice
        filename = f"{summary_type}_summary.txt"
        
        #giving the user the option to save the summary or not
        save_choice = input(f"\nDo you want to save the {summary_type} summary? (yes/no): ").strip().lower()
        
        if save_choice == "yes":
            save_output(summary, filename, folder="output")
        else:
            print(f"\n{summary_type.capitalize()} summary not saved.")
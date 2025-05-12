#for the histograms menu, the plan will be to have it dynamically generated based on the dataset being used
#the goal for this is that it can be used with various datasets and not just the iris dataset
from utils import load_data, plot_histogram, save_hist_output

dataset = load_data()
features_names = dataset["feature_names"]
features = dataset["data"]

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
            print("Returning to menu...")
            break
        
        #ensure the choice is valid
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(features_names): #assigning a number to each feature
                feature_name = features_names[choice - 1]

                plot_histogram(features, features_names, feature_name)

                #prompting if the user wants to save the histogram
                save_choice = input(f"Do you want to save the histogram for {feature_name}? (yes/no): ").strip().lower()
                if save_choice == "yes":
                    save_hist_output(features, features_names, feature_name, folder="output") #save the histogram
                else:
                    input("\nSave cancelled, press enter to return to menu...")
            else:
                print("Error: Please select a valid option.")
        else:
            print("Error: Please select a valid option.")

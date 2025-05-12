#the scatterplot menu will work pretty much the exact same as the histogram menu
#except this time the user will be prompted for 2 inputs to compare data in a scatterplot
from utils import load_data, plot_scatterplot, save_scatter_output

dataset = load_data()
features_names = dataset["feature_names"]
features = dataset["data"]

def show_scatterplot_menu():

    while True:
        print("\nChoose two features to display the scatterplot:")
        
        #dynamically generating the menu based on the features names
        #similar to the data summary function but only getting the names this time
        for i, feature in enumerate(features_names, 1):
            print(f"{i}. {feature}")
        
        print("x. Return to menu")
        
        #user inputs for x and y
        x_choice = input("Enter the number of your choice for the x-axis: ").strip()
        if x_choice == 'x':
            print("Returning to menu...")
            break
            
        y_choice = input("Enter the number of your choice for the y-axis: ").strip()
        if y_choice == 'x':
            print("Returning to menu...")
            break

        #ensure the choice is valid
        if x_choice.isdigit() and y_choice.isdigit():
            x_choice = int(x_choice)
            y_choice = int(y_choice)
            if 1 <= x_choice <= len(features_names) and 1 <= y_choice <= len(features_names): #assigning a number to each feature
                x_feature = (x_choice - 1)
                y_feature = (x_choice - 1)
                x_feature_name = features_names[x_choice - 1]
                y_feature_name = features_names[y_choice - 1]

                plot_scatterplot(features, x_feature, y_feature, x_feature_name, y_feature_name)

                #prompting if the user wants to save the scatterplot
                save_choice = input(f"Do you want to save the histogram of {x_feature_name}? and {y_feature_name} (yes/no): ").strip().lower()
                if save_choice == "yes":
                    save_scatter_output(features, x_feature, y_feature, x_feature_name, y_feature_name, folder="output") #save the scatterplot
                else:
                    input("\nSave cancelled, press enter to return to menu...")
            else:
                print("Error: Please select a valid option.")
        else:
            print("Error: Please select a valid option.")
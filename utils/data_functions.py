import numpy as np
import matplotlib.pyplot as plt
#made these functions for use with the principles of data analytics module
#reusing them for this project

#Functions for printing information on the iris dataset just for easier reading
#originally there was a function for every variable, which can be seen in the example_functions.py
def data_info(name, var):
    lines = [] #list to store the information
    lines.append(f"{name} of the data:\n")
    lines.append(str(var))

    #printing the final output
    print("".join(lines))

    input("\nPress Enter to continue...")
    return lines

#functions for summarizing the iris dataset
def data_features_summary(features, features_names, stat="", pause=True):
    #making a dictiononary to pair each numpy function
    #wanted this to have similar functionality to the iris_info function
    #where one function can be used for a similar purpose by calling different arguments
    stat_function = {

        "mean" : np.mean,
        "min" : np.min,
        "max" : np.max,
        "std" : np.std,
        "median" : np.median

    }

    function = stat_function[stat]
    #adjusting code to fit with file_saver function
    #makes it easier to save the output
    header = f"{stat.capitalize()} of each feature:"
    lines = []
   
    #adding a line of spacing with .append so it also appears in the saved output
    print("\n")
    lines.append(header)
    lines.append("\n")

    for r, name in enumerate(features_names):
        answer = function(features[:, r])
        #gets the summary of a feature, prints the summary, and then saves that to the lines list
        line = f"{name}: {answer:.2f}\n" 
        lines.append(line)

    #printing the whole summary
    print("".join(lines))

    if pause:
        input("Press Enter to continue...")
    
    return lines #stores the information to be used with other functions or whatever else

def data_features_summary_all(features, features_names):

    all_lines = []

    for stat in ["mean", "min", "max", "median", "std"]:

        lines = data_features_summary(features, features_names, stat, pause=False)
        all_lines.extend(lines)

    input("\nPress Enter to continue...")

    return all_lines

def plot_histogram(features, features_names, feature_name):
    #find the index of the feature
    feature_index = features_names.index(feature_name)
    
    #get the specific feature data (column) by index
    feature_data = features[:, feature_index]

    #plotting the histogram
    plt.hist(feature_data, bins=15, color="lightgreen", edgecolor="black", label=f"{feature_name} Feature")

    #adding labels, title, and legend
    plt.title(f"Histogram of {feature_name}")
    plt.xlabel(feature_name)
    plt.ylabel("Frequency")
    plt.legend()

    #display the histogram
    plt.show()
    
    input("\nPress Enter to continue...")

def plot_scatterplot(features, x_feature, y_feature, x_feature_name, y_feature_name):
    #plotting the scatterplot
    plt.scatter(features[:, x_feature], features[:, y_feature], color='skyblue')

    #adding labels, and title
    plt.title(f"Scatterplot: {x_feature_name} and {y_feature_name}")
    plt.xlabel(x_feature_name)
    plt.ylabel(y_feature_name)
    plt.grid(True)

    #displaying the scatterplot
    plt.show()

    input("\nPress Enter to continue...")
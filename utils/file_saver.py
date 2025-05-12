import os
import matplotlib.pyplot as plt

#a function that handles saving outputs to a file
def save_output(lines, filename="", folder="output"):

    #get absolute path to the directory of this script
    #__file__ holds path to current script
    #this doesnt seem to be needed since the script only works if run from the correct directory anyways
    #might be worth doing something similar for running the script though
    base_directory = os.path.dirname(os.path.abspath(__file__))

    #create full path to output folder
    output_directory = os.path.join(base_directory, "..", folder)

    #ensure the output directory exists, creates one if it does not
    os.makedirs(output_directory, exist_ok=True)

    #create full path to output file
    filepath = os.path.join(output_directory, filename)

    #write the lines to the file
    with open(filepath, 'w') as f:
        for line in lines:
            f.write(line + '\n')

    print(f"\nOutput saved to: {filepath}")

#a function to save histogram plots, similar to the one above
#it generates the plot again but this time will save the png and then close the plot
def save_hist_output(features, features_names, feature_name, folder="output"):
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

    #get absolute path to the directory of this script
    base_directory = os.path.dirname(os.path.abspath(__file__))

    #create full path to output folder
    output_directory = os.path.join(base_directory, "..", folder)

    #ensure the output directory exists, creates one if it does not
    os.makedirs(output_directory, exist_ok=True)

    #create full path to output file
    filepath = os.path.join(output_directory, feature_name)

    #setting filename and saving the png
    feature_name = f"{feature_name}_histogram.png"
    plt.savefig(filepath)

    print(f"\nHistogram saved to: {filepath}")

    #closing the plot
    plt.close()

#function to save the scatterplot output, similar to the ones above
def save_scatter_output(features, x_feature, y_feature, x_feature_name, y_feature_name, folder="output"):
    #plotting the scatterplot
    plt.scatter(features[:, x_feature], features[:, y_feature], color='skyblue')

    #adding labels, and title
    plt.title(f"Scatterplot: {x_feature_name} and {y_feature_name}")
    plt.xlabel(x_feature_name)
    plt.ylabel(y_feature_name)
    plt.grid(True)

    #get absolute path to the directory of this script
    base_directory = os.path.dirname(os.path.abspath(__file__))

    #create full path to output folder
    output_directory = os.path.join(base_directory, "..", folder)

    #ensure the output directory exists, creates one if it does not
    os.makedirs(output_directory, exist_ok=True)

    #create full path to output file
    filepath = os.path.join(output_directory, filename)

    #setting filename and saving the png
    #using .replace to replace any spaces in the feature names with "_" for neater file names
    filename = f"{x_feature_name.replace(' ', '_')}_and_{y_feature_name.replace(' ', '_')}_scatterplot.png"
    plt.savefig(filepath)

    print(f"\nScattorplot saved to: {filepath}")

    #closing the plot 
    plt.close()
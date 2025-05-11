import numpy as np
#made these functions for use with the principles of data analytics module
#reusing them for this project

#Functions for printing information on the iris dataset just for easier reading
#originally there was a function for every variable, which can be seen in the example_functions.py
def data_info(name, var):
    print(f"\n{name} of the data:")
    print(var)

#functions for getting the first and last rows of a dataset
#using variable n in case there's a need to get first or last 'n' number of rows instead of 5
def firstrow_data(array, n=5):
    print(f"\nFirst {n} rows of data:")
    print(array[:n])

def lastrow_data(array, n=5):
    print(f"\nLast {n} rows of data:")
    print(array[-n:])

#functions for summarizing the iris dataset
def data_features_summary(features, features_names, stat=""):
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
    print(f"\n{stat.capitalize()} of each feature:\n")
    
    for r, name in enumerate(features_names):
        answer = function(features[:, r])
        print(f"{name}: {answer:.2f}")
    
    input("\nPress Enter to continue...")
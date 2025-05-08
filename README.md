# pands-project

App functionality:
The user is presented with a menu in which they can choose various options to interact with the iris dataset.

Option 1:
Summarising the data: 
    Allows the user to get the mean, min, max, median and std of each feature.
    The user can choose between either summary option, or all of them.
    After the user chooses an option, the summary will be output to a .txt file called summary.txt.
    If summary.txt already exists, it will be overwritten (maybe add an option to confirm this before doing it)

Option 2:
Histograms:
    Allows the user to get a histogram png of any chosen feature or all features.
    Potentially add the option of getting a histogram for a chosen species.
    The png will be saved and named according to the feature chosen (e.g. petal_length_hist.png, sepal_length_hist.png)

Option 3:
Scatterplots:
    The user can choose between two features and have them compared against each other in a scatterplot.
    Potentially add the option to include a regression line.
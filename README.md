# pands-project

Dataset Analysis Application

File structure
    pands-project
        The root folder
    utils folder
        Contains general use functions that are used throughout
    menu folder
        Contains the menu functions for user interaction
    output folder
        Where generated .txt and .png files are stored
    analysis.py
        Main script to run the application
    README.md
        This file

This is a python application designed to interactively explore and analyze datasets. The program provides functionality for data inspection, statistical summaries, and visualisations via histograms and scatterplots.

The dataset used is the Iris dataset, which contains measurements for 150 iris flowers from three species:

    Features (columns):

        Sepal length (cm)

        Sepal width (cm)

        Petal length (cm)

        Petal width (cm)

    Target (class):

        Iris Setosa

        Iris Versicolour

        Iris Virginica

In order to run the application, python must be installed (atleast 3.x or higher), and the command must be run from the from the folder in which the script is located.
Running the script:
    python analysis.py

Application Menu Options
    Option 1: Dataset Information

        View basic details about the features and target data.

        Option to save to .txt file.

    Option 2: Summarise Data

        View statistics such as mean, min, max, median, standard deviation for each feature.

        Option to save results to .txt file.

    Option 3: Generate Histogram

        Choose a feature to visualize its distribution.

        Option to save the figure as .png.

    Option 4: Generate Scatterplot

        Choose any two features to compare via scatterplot.

        Option to save the figure as .png.

    Generated output files will be saved to the /output/ folder
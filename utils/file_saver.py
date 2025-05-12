import os

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
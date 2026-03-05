
import ast
import os
import glob
# Constants
DIRECTORY = 'data'
def task_func(directory):
    # Get all text files in the directory
    files = glob.glob(DIRECTORY + '/*.txt')
    # Initialize the list of dictionaries
    dictionaries = []
    # Loop through each file
    for file in files:
        # Open the file
        with open(file, 'r') as f:
            # Read the contents of the file
            contents = f.read()
            # Try to convert the contents to a dictionary
            try:
                dictionary = ast.literal_eval(contents)
                # Add the dictionary to the list
                dictionaries.append(dictionary)
            except ValueError:
                # If the contents are not a valid dictionary, raise a ValueError
                raise ValueError(f'Invalid dictionary representation in file {file}')
    # Return the list of dictionaries
    return dictionaries
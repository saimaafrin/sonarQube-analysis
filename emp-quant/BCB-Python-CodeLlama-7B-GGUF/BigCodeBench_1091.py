
import ast
import os
import glob
# Constants
DIRECTORY = 'data'
def task_func(directory):
    # Get all text files in the directory
    files = glob.glob(os.path.join(directory, '*.txt'))
    # Initialize an empty list to store the dictionaries
    dictionaries = []
    # Iterate over the files
    for file in files:
        # Read the file contents
        with open(file, 'r') as f:
            contents = f.read()
        # Try to convert the contents to a dictionary
        try:
            dictionary = ast.literal_eval(contents)
        # If the contents are not a valid dictionary representation, raise a ValueError
        except ValueError:
            raise ValueError(f'Invalid dictionary representation in file {file}')
        # Add the dictionary to the list
        dictionaries.append(dictionary)
    # Return the list of dictionaries
    return dictionaries

import ast
import os
import glob

# Constants
DIRECTORY = 'data'

def task_func(directory):
    # Create a list to store the dictionaries
    dictionaries = []

    # Iterate over all text files in the directory
    for filename in glob.glob(os.path.join(directory, '*.txt')):
        # Open the file and read its contents
        with open(filename, 'r') as f:
            contents = f.read()

        # Try to convert the contents to a dictionary using ast.literal_eval
        try:
            dictionary = ast.literal_eval(contents)
        except ValueError:
            # If the contents are not a valid dictionary representation, raise a ValueError
            raise ValueError(f'Invalid dictionary representation in file {filename}')

        # Add the dictionary to the list
        dictionaries.append(dictionary)

    # Return the list of dictionaries
    return dictionaries

# Call the function with the directory path
dictionaries = task_func(DIRECTORY)

# Print the list of dictionaries
print(dictionaries)
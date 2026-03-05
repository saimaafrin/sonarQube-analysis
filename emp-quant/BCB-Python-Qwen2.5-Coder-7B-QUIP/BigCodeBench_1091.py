
import ast
import os
import glob
# Constants
DIRECTORY = 'data'

def task_func(directory):
    # Initialize an empty list to store the dictionaries
    dictionaries = []
    
    # Get a list of all .txt files in the specified directory
    files = glob.glob(os.path.join(directory, '*.txt'))
    
    # Iterate over the files
    for file in files:
        # Open the file and read its contents
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse the content as a dictionary
        try:
            # Use ast.literal_eval to safely evaluate the string as a dictionary
            dictionary = ast.literal_eval(content)
            # Append the dictionary to the list
            dictionaries.append(dictionary)
        except (SyntaxError, ValueError):
            # If there is an error, raise a ValueError
            raise ValueError(f"Invalid dictionary representation in file: {file}")
    
    # Return the list of dictionaries
    return dictionaries
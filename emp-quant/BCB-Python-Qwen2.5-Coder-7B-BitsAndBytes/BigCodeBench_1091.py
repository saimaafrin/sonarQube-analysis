
import ast
import os
import glob

# Constants
DIRECTORY = 'data'

def task_func(directory):
    """
    Converts all Unicode string representations of dictionaries in all text files 
    in the specified directory to Python dictionaries.

    Args:
        directory (str): The path to the directory containing text files.

    Returns:
        list: A list of dictionaries extracted from the text files.

    Raises:
        ValueError: If any text file contains an invalid dictionary representation.
    """
    # Initialize an empty list to store the dictionaries
    dictionaries = []

    # Use glob to find all .txt files in the specified directory
    file_paths = glob.glob(os.path.join(directory, '*.txt'))

    for file_path in file_paths:
        try:
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Convert the Unicode string representation to a Python dictionary
            dictionary = ast.literal_eval(content)
            
            # Append the dictionary to the list
            dictionaries.append(dictionary)
        
        except (SyntaxError, ValueError) as e:
            # Raise an error if the content is not a valid dictionary representation
            raise ValueError(f"Invalid dictionary representation in file {file_path}: {e}")

    return dictionaries
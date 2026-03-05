import ast
import os
import glob
def task_func(directory):
    """
    Convert all Unicode string representations of dictionaries in all text files in the specified directory to Python dictionaries.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        raise ValueError(f"Directory '{directory}' does not exist.")

    # Get all text files in the directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))

    # Initialize an empty list to store the dictionaries
    dictionaries = []

    # Iterate over the text files
    for text_file in text_files:
        # Read the text file
        with open(text_file, 'r') as f:
            text = f.read()

        # Try to convert the text to a dictionary
        try:
            dictionary = ast.literal_eval(text)
        except ValueError:
            raise ValueError(f"Invalid dictionary representation in file '{text_file}'.")

        # Add the dictionary to the list
        dictionaries.append(dictionary)

    # Return the list of dictionaries
    return dictionaries
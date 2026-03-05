
import re
import os
import glob

def task_func(dir_path):
    # Check if the directory exists
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist")

    # Initialize a dictionary to store the results
    result = {}

    # Search for text files in the directory and its subdirectories
    for file_path in glob.glob(os.path.join(dir_path, '**/*.txt'), recursive=True):
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()  # Convert to lowercase to make the search case-insensitive

        # Use regular expression to find occurrences of the word "error"
        count = len(re.findall(r'\berror\b', content))

        # Store the count in the dictionary with the relative file path as the key
        relative_path = os.path.relpath(file_path, dir_path)
        result[relative_path] = count

    return result
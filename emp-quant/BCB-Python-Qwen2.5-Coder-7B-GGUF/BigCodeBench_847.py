
import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Split the input string into separate strings
    lines = input_string.split('\n')

    # Initialize a list to store file paths
    file_paths = []

    # Iterate over each line
    for i, line in enumerate(lines):
        # Remove special characters using regex
        cleaned_line = re.sub(r'[^\w\s]', '', line)

        # Create a unique filename
        filename = f'file_{random.randint(1, 1000)}.txt'
        filepath = os.path.join(directory, filename)

        # Write the cleaned line to the file
        with open(filepath, 'w') as file:
            file.write(cleaned_line)

        # Append the file path to the list
        file_paths.append(filepath)

    return file_paths
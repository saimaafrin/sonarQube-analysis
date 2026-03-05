
import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Split the input string into separate strings
    lines = input_string.split('\n')

    # Define a function to clean the string
    def clean_string(s):
        # Remove special characters and numbers
        return ''.join(c for c in s if c.isalpha() or c.isspace())

    # Create and save each string as a separate text file
    file_paths = []
    for line in lines:
        if line.strip():  # Ignore empty lines
            # Clean the line
            cleaned_line = clean_string(line)
            # Generate a random filename
            filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.txt'
            # Save the cleaned line to the file
            with open(os.path.join(directory, filename), 'w') as file:
                file.write(cleaned_line)
            # Add the file path to the list
            file_paths.append(os.path.join(directory, filename))

    return file_paths
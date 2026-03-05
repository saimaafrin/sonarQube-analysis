
import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    # Split the input string into individual lines
    lines = input_string.splitlines()

    # Remove special characters from each line
    clean_lines = [re.sub(r'[^a-zA-Z0-9\s]', '', line) for line in lines]

    # Create a random file name for each line
    file_names = [f'{random.randint(1000, 9999)}.txt' for line in clean_lines]

    # Save each line as a separate text file
    file_paths = [os.path.join(directory, file_name) for file_name in file_names]
    for line, file_path in zip(clean_lines, file_paths):
        with open(file_path, 'w') as f:
            f.write(line)

    return file_paths
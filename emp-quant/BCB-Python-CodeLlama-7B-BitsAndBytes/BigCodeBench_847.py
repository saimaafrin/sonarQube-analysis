
import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    # Split the input string into separate lines
    lines = input_string.splitlines()

    # Remove special characters from each line
    clean_lines = [re.sub(r'[^a-zA-Z0-9\s]', '', line) for line in lines]

    # Create a random file name for each line
    file_names = [random.randint(100000, 999999) for _ in range(len(clean_lines))]

    # Save each line as a separate text file
    file_paths = []
    for line, file_name in zip(clean_lines, file_names):
        file_path = os.path.join(directory, f'{file_name}.txt')
        with open(file_path, 'w') as f:
            f.write(line)
        file_paths.append(file_path)

    return file_paths

file_paths = task_func(input_string)
print(file_paths)
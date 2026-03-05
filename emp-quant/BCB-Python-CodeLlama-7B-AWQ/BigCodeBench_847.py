import re
import os
import string
import random
def task_func(input_string, directory='./text_files'):
    """
    Split a multi-line string into separate strings, remove special characters, and save each string as a separate text file.
    """
    # Remove special characters
    input_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    # Split into separate strings
    input_strings = input_string.split()
    # Create a random file name
    file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    # Create a directory to save the files
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Save each string as a separate text file
    file_paths = []
    for input_string in input_strings:
        file_path = os.path.join(directory, file_name + '.txt')
        with open(file_path, 'w') as f:
            f.write(input_string)
        file_paths.append(file_path)
    return file_paths
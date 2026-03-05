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

    # Split the string into separate lines
    lines = input_string.splitlines()

    # Create a random file name
    file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

    # Save each line as a separate text file
    file_paths = []
    for line in lines:
        file_path = os.path.join(directory, file_name + '.txt')
        with open(file_path, 'w') as f:
            f.write(line)
        file_paths.append(file_path)

    return file_paths
input_string = """
This is a multi-line string.
It has special characters like !@#$%^&*()_+-=[]{}|;':"\\,./<>?
"""
directory = './text_files'
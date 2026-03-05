
import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    file_paths = []
    for line in input_string.splitlines():
        line = re.sub(r'[^a-zA-Z0-9\s]', '', line)
        file_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as f:
            f.write(line)
        file_paths.append(file_path)
    return file_paths
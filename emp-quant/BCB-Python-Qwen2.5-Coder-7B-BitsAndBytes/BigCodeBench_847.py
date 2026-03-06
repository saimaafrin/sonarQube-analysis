
import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Split the input string into lines
    lines = input_string.split('\n')
    
    file_paths = []
    
    for line in lines:
        # Remove special characters using regex
        cleaned_line = re.sub(r'[^\w\s]', '', line)
        
        # Generate a random filename to avoid conflicts
        filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.txt'
        filepath = os.path.join(directory, filename)
        
        # Write the cleaned line to the file
        with open(filepath, 'w') as file:
            file.write(cleaned_line)
        
        file_paths.append(filepath)
    
    return file_paths
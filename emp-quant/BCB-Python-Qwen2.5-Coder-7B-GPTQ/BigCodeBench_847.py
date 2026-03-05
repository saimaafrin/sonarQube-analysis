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
    for line in lines:
        # Remove special characters using regex
        cleaned_line = re.sub(r'[^\w\s]', '', line)
        
        # Generate a random filename
        filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.txt'
        file_path = os.path.join(directory, filename)
        
        # Write the cleaned line to the file
        with open(file_path, 'w') as file:
            file.write(cleaned_line)
        
        # Append the file path to the list
        file_paths.append(file_path)
    
    return file_paths
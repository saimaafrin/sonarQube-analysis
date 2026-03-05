import re
import os
import glob
def task_func(dir_path):
    # Check if the directory exists
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist")
    
    # Initialize an empty dictionary to store the results
    result = {}
    
    # Use glob to find all .txt files in the directory and its subdirectories
    for file_path in glob.glob(os.path.join(dir_path, '**', '*.txt'), recursive=True):
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Use regular expression to find all occurrences of the word "error" (case-insensitive)
        error_count = len(re.findall(r'\berror\b', content, re.IGNORECASE))
        
        # Store the result in the dictionary with the relative file path as the key
        result[os.path.relpath(file_path, dir_path)] = error_count
    
    return result
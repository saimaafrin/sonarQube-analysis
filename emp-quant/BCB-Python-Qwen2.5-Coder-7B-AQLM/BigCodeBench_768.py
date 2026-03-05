
import re
import os
import glob

def task_func(dir_path):
    if not os.path.exists(dir_path):
        raise ValueError("The directory does not exist.")
    
    error_count_dict = {}
    
    # Use glob to find all .txt files in the directory and its subdirectories
    for file_path in glob.glob(os.path.join(dir_path, '**/*.txt'), recursive=True):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()  # Convert content to lowercase to make the search case-insensitive
            error_count = len(re.findall(r'\berror\b', content))  # Find all occurrences of the word "error"
            relative_path = os.path.relpath(file_path, dir_path)  # Get the relative path of the file
            error_count_dict[relative_path] = error_count
    
    return error_count_dict
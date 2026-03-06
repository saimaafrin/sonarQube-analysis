
import re
import os
from pathlib import Path
import glob

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    # Initialize an empty dictionary to store the results
    results = {}
    
    # Use glob to find all text files in the specified directory
    text_files = glob.glob(os.path.join(directory_path, '*.txt'))
    
    for file_path in text_files:
        # Extract the file name without the path
        file_name = Path(file_path).name
        
        # Open the file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find all matches using the provided regex pattern
        matches = re.findall(regex_pattern, content)
        
        # Store the matches in the dictionary
        results[file_name] = matches
    
    return results
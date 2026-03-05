
import re
import os
from pathlib import Path
import glob

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    # Initialize a dictionary to store the results
    results = {}
    
    # Get a list of all files in the directory
    files = glob.glob(os.path.join(directory_path, '*.txt'))
    
    # Iterate over each file
    for file in files:
        # Open the file and read its contents
        with open(file, 'r') as f:
            content = f.read()
        
        # Find all matches in the content
        matches = re.findall(regex_pattern, content)
        
        # Add the matches to the dictionary with the file name as the key
        results[os.path.basename(file)] = matches
    
    return results
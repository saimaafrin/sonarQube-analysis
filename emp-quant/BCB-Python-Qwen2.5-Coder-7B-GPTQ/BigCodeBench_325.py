import re
import os
from pathlib import Path
import glob
def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    # Initialize an empty dictionary to store the results
    results = {}
    
    # Use glob to find all text files in the specified directory
    text_files = glob.glob(os.path.join(directory_path, '*.txt'))
    
    # Iterate over each file in the directory
    for file_path in text_files:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Use re.findall to extract matches based on the regex pattern
        matches = re.findall(regex_pattern, content)
        
        # Extract the file name without the path and store the matches in the dictionary
        file_name = Path(file_path).name
        results[file_name] = matches
    
    return results
import re
import os
from pathlib import Path
import glob
def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    # Initialize an empty dictionary to store the results
    results = {}
    
    # Use glob to find all text files in the specified directory
    text_files = glob.glob(os.path.join(directory_path, '*.txt'))
    
    # Iterate over each text file
    for file_path in text_files:
        # Open the file and read its content
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Find all matches in the content using the provided regex pattern
        matches = re.findall(regex_pattern, content)
        
        # Extract the file name without the path
        file_name = Path(file_path).name
        
        # Store the matches in the dictionary with the file name as the key
        results[file_name] = matches
    
    # Return the dictionary containing file names and their matches
    return results

import re
import os
from pathlib import Path
import glob

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    """
    Extracts matches from all text files in a specified directory based on a regular expression pattern.
    
    Parameters:
    - directory_path: str, the path to the directory containing text files.
    - regex_pattern: str, the regular expression pattern to use for matching.
    
    Returns:
    - dict: A dictionary where keys are file names (without path) and values are lists of matches extracted from the files.
    """
    # Initialize the dictionary to store the results
    results = {}
    
    # Use glob to find all text files in the directory
    text_files = glob.glob(os.path.join(directory_path, '*.txt'))
    
    # Iterate over each text file
    for file_path in text_files:
        # Extract the file name without the path
        file_name = Path(file_path).name
        
        # Open the file and read its content
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Find all matches using the regex pattern
        matches = re.findall(regex_pattern, content)
        
        # Store the matches in the dictionary
        results[file_name] = matches
    
    return results
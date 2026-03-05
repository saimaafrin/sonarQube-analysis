
import re
import os
from pathlib import Path
import glob

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    matches_dict = {}
    # Compile the regex pattern
    pattern = re.compile(regex_pattern)
    
    # Iterate over all files in the specified directory
    for file_path in glob.glob(os.path.join(directory_path, '*.txt')):
        # Extract the file name without the path
        file_name = Path(file_path).name
        matches = []
        
        # Open and read the file
        with open(file_path, 'r') as file:
            for line in file:
                # Find all matches in the line
                line_matches = pattern.findall(line)
                matches.extend(line_matches)
        
        # Add the matches to the dictionary
        matches_dict[file_name] = matches
    
    return matches_dict
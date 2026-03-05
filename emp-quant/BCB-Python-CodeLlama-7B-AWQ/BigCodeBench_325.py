import re
import os
from pathlib import Path
import glob
def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    """
    Extracts matches from all text files in a specified directory based on a regular expression pattern.
    It captures whatever is between parentheses as a single match, and any character outside the parentheses as individual matches in the string.
    The function should output with:
        dict: A dictionary where keys are file names (without path) and values are lists of matches extracted from the files.
    """
    matches = {}
    for file in glob.glob(os.path.join(directory_path, '*.txt')):
        with open(file, 'r') as f:
            text = f.read()
            matches[os.path.basename(file)] = re.findall(regex_pattern, text)
    return matches
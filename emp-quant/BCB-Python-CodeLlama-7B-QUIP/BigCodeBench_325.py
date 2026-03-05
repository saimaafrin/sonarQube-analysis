
import re
import os
from pathlib import Path
import glob

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    matches = {}
    for file_path in glob.glob(directory_path + '/*'):
        with open(file_path, 'r') as file:
            for line in file:
                for match in re.findall(regex_pattern, line):
                    if match not in matches:
                        matches[file_path] = []
                    matches[file_path].append(match)
    return matches
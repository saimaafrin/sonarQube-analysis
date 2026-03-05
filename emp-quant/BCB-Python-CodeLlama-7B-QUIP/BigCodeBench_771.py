
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    new_files = []
    for file in os.listdir(directory):
        if re.match(pattern, file):
            new_file = re.sub(r'\d+', str(1 + int(re.search(r'\d+', file).group(0))), file)
            new_files.append(new_file)
    return new_files
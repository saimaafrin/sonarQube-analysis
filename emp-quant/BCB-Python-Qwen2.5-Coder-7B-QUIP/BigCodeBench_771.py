
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    new_files = []
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            match = re.match(pattern, file)
            if match:
                base_name = match.group(1)
                new_name = f"{base_name}_new.csv"
                new_path = Path(directory) / new_name
                new_files.append(new_name)
                with open(new_path, 'w', newline='') as f:
                    f.write('')  # Write an empty string to create an empty file
    return new_files
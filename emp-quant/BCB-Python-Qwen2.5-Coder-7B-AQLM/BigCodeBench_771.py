
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    new_files = []
    directory_path = Path(directory)
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Iterate over all files in the directory
    for file_path in directory_path.iterdir():
        if file_path.is_file() and file_path.suffix == '.csv':
            # Match the filename against the pattern
            match = regex.match(file_path.stem)
            if match:
                # Extract the base name from the match
                base_name = match.group(1)
                # Create the new filename
                new_filename = f"{base_name}.csv"
                new_file_path = directory_path / new_filename
                
                # Copy the content of the original file to the new file
                with open(file_path, 'r') as infile, open(new_file_path, 'w', newline='') as outfile:
                    reader = csv.reader(infile)
                    writer = csv.writer(outfile)
                    for row in reader:
                        writer.writerow(row)
                
                # Append the new filename to the list
                new_files.append(new_filename)
    
    return new_files
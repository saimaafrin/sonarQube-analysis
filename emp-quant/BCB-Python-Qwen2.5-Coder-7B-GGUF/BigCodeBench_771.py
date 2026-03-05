
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    new_files = []
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file matches the pattern
        match = regex.match(filename)
        if match:
            # Extract the base name without the number and extension
            base_name = match.group(1)
            # Create the new filename by appending '_new' before the extension
            new_filename = f"{base_name}_new.csv"
            # Construct full file paths
            old_file_path = Path(directory) / filename
            new_file_path = Path(directory) / new_filename
            # Copy the content from the old file to the new file
            with old_file_path.open('r') as old_file, new_file_path.open('w', newline='') as new_file:
                csv_reader = csv.reader(old_file)
                csv_writer = csv.writer(new_file)
                for row in csv_reader:
                    csv_writer.writerow(row)
            # Append the new filename to the list
            new_files.append(new_filename)
    
    return new_files
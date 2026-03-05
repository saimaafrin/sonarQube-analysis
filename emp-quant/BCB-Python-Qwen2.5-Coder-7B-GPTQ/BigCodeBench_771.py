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
            # Create the new filename
            new_filename = f"{base_name}.csv"
            # Construct full file paths
            old_file_path = Path(directory) / filename
            new_file_path = Path(directory) / new_filename
            # Copy the content from the old file to the new file
            with open(old_file_path, 'r') as old_file, open(new_file_path, 'w', newline='') as new_file:
                reader = csv.reader(old_file)
                writer = csv.writer(new_file)
                for row in reader:
                    writer.writerow(row)
            # Append the new filename to the list
            new_files.append(new_filename)
    
    return new_files
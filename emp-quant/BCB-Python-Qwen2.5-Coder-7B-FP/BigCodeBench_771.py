import re
import os
from pathlib import Path
import csv
def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    new_files = []
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file matches the specified pattern
        match = regex.match(filename)
        if match:
            # Extract the base name from the matched pattern
            base_name = match.group(1)
            # Create a new filename by appending '_new' before the extension
            new_filename = f"{base_name}_new.csv"
            # Construct full paths for the old and new files
            old_file_path = Path(directory) / filename
            new_file_path = Path(directory) / new_filename
            
            # Copy the content of the old file to the new file
            with open(old_file_path, mode='r', newline='') as infile, \
                 open(new_file_path, mode='w', newline='') as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile)
                for row in reader:
                    writer.writerow(row)
            
            # Append the new filename to the list
            new_files.append(new_filename)
    
    return new_files
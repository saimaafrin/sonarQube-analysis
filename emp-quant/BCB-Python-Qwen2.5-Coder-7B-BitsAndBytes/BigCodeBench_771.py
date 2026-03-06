
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    # Ensure the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Initialize a list to store the names of the new files
    new_files = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # Check if the filename matches the pattern
            match = re.match(pattern, filename)
            if match:
                # Extract the base name without the number and extension
                base_name = match.group(1)
                
                # Create a new filename with a different extension or format
                new_filename = f"{base_name}_new.csv"
                
                # Construct full paths for old and new files
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                
                # Copy the content from the old file to the new file
                with open(old_file_path, mode='r', newline='') as infile, \
                     open(new_file_path, mode='w', newline='') as outfile:
                    reader = csv.reader(infile)
                    writer = csv.writer(outfile)
                    for row in reader:
                        writer.writerow(row)
                
                # Append the new filename to the list
                new_files.append(new_filename)
    
    return new_files
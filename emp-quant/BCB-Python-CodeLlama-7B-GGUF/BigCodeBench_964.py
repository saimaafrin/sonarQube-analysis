
import os
from pathlib import Path
import pandas as pd
import docx

def task_func(source_directory: str, target_directory: str) -> int:
    # Check if source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist")

    # Get list of files in source directory
    file_list = os.listdir(source_directory)

    # Initialize counter for number of files successfully converted
    num_files_converted = 0

    # Iterate over files in source directory
    for file in file_list:
        # Get full path of file
        file_path = os.path.join(source_directory, file)

        # Check if file has a supported extension
        if file.endswith((".txt", ".docx", ".xlsx", ".csv")):
            # Convert file to CSV
            df = pd.read_csv(file_path)

            # Save CSV to target directory
            df.to_csv(os.path.join(target_directory, file), index=False)

            # Increment counter
            num_files_converted += 1

    # Return number of files successfully converted
    return num_files_converted

import os
from pathlib import Path
import pandas as pd
import docx

def task_func(source_directory: str, target_directory: str) -> int:
    # Check if source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError("Source directory does not exist")

    # Get a list of files in the source directory
    files = os.listdir(source_directory)

    # Initialize the number of files successfully converted to CSV
    num_converted = 0

    # Loop through each file in the source directory
    for file in files:
        # Check if the file has a supported extension
        if file.endswith((".txt", ".docx", ".xlsx", ".csv")):
            # Convert the file to CSV
            df = pd.read_csv(file, index_col=None)
            df.to_csv(target_directory + "/" + file, index=False)
            num_converted += 1

    # Return the number of files successfully converted to CSV
    return num_converted
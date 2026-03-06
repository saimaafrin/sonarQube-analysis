
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

    # Initialize counter for number of files successfully converted to CSV
    num_files_converted = 0

    # Iterate over files in source directory
    for file in file_list:
        # Get file path and extension
        file_path = os.path.join(source_directory, file)
        file_ext = os.path.splitext(file_path)[1]

        # Convert file to CSV if it is a supported file type
        if file_ext in [".txt", ".docx", ".xlsx", ".csv"]:
            # Read file content and store in a Pandas DataFrame
            if file_ext == ".txt":
                df = pd.read_csv(file_path, sep="\t")
            elif file_ext == ".docx":
                df = docx.read_docx(file_path)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file_path)
            else:
                df = pd.read_csv(file_path)

            # Save DataFrame to CSV file
            csv_file_path = os.path.join(target_directory, file + ".csv")
            df.to_csv(csv_file_path, index=False)

            # Increment counter
            num_files_converted += 1

    # Return number of files successfully converted to CSV
    return num_files_converted
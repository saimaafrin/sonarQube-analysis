import os
from pathlib import Path
import pandas as pd
import docx
def task_func(source_directory: str, target_directory: str) -> int:
    """
    Converts files with specific extensions (.txt, .docx, .xlsx, .csv) from a source directory to CSV files and saves them in a target directory.
    """
    # Check if source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist.")

    # Create target directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Get list of files in source directory
    files = os.listdir(source_directory)

    # Initialize counter for number of files successfully converted to CSV
    num_files_converted = 0

    # Iterate over files in source directory
    for file in files:
        # Get file path and extension
        file_path = os.path.join(source_directory, file)
        file_ext = os.path.splitext(file_path)[1]

        # Check if file extension is supported
        if file_ext in [".txt", ".docx", ".xlsx", ".csv"]:
            # Convert file to CSV
            if file_ext == ".txt":
                # Read text file and store in CSV
                with open(file_path, "r") as f:
                    text = f.read()
                df = pd.DataFrame({"Text": [text]})
                df.to_csv(os.path.join(target_directory, file), index=False)
            elif file_ext == ".docx":
                # Read Word document and store in CSV
                doc = docx.Document(file_path)
                text = doc.get_text()
                df = pd.DataFrame({"Text": [text]})
                df.to_csv(os.path.join(target_directory, file), index=False)
            elif file_ext == ".xlsx":
                # Read Excel spreadsheet and store in CSV
                df = pd.read_excel(file_path)
                df.to_csv(os.path.join(target_directory, file), index=False)
            elif file_ext == ".csv":
                # Read CSV file and store in CSV
                df = pd.read_csv(file_path)
                df.to_csv(os.path.join(target_directory, file), index=False)

            # Increment counter for number of files successfully converted to CSV
            num_files_converted += 1

    # Return number of files successfully converted to CSV
    return num_files_converted
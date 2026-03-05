import os
from pathlib import Path
import pandas as pd
import docx
def task_func(source_directory: str, target_directory: str) -> int:
    """
    Converts files with specific extensions (.txt, .docx, .xlsx, .csv) from a source directory to CSV files and saves them in a target directory.
    Notes:
        - Each file's text content is captured and stored in a CSV with a single 'Text' column and no row indices.
        - This function will overwrite existing files in the target directory if they have the same names as the converted files.
    Args:
        source_directory (str): The source directory containing the files to be converted.
        target_directory (str): The target directory where the converted files will be saved.
    Returns:
        int: The number of files successfully converted to CSV.
    Raises:
        FileNotFoundError: If the source directory does not exist.
    """
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory '{source_directory}' does not exist.")

    # Create the target directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Initialize the number of successfully converted files
    num_converted = 0

    # Iterate over the files in the source directory
    for file in os.listdir(source_directory):
        # Get the file path and extension
        file_path = os.path.join(source_directory, file)
        extension = os.path.splitext(file_path)[1]

        # Convert the file to CSV if it is a supported extension
        if extension in [".txt", ".docx", ".xlsx", ".csv"]:
            # Read the file content
            if extension == ".txt":
                with open(file_path, "r") as f:
                    text = f.read()
            elif extension == ".docx":
                text = docx.Document(file_path).text
            elif extension == ".xlsx":
                text = pd.read_excel(file_path).to_csv(index=False)
            else:
                text = pd.read_csv(file_path).to_csv(index=False)

            # Write the text to a CSV file in the target directory
            with open(os.path.join(target_directory, file), "w") as f:
                f.write(text)

            # Increment the number of successfully converted files
            num_converted += 1

    # Return the number of successfully converted files
    return num_converted
source_directory = "path/to/source/directory"
target_directory = "path/to/target/directory"
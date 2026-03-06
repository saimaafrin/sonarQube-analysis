
import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Find all matching files
    matching_files = [f for f in Path(directory).rglob(file_pattern)]
    
    if not matching_files:
        return "No matching files found."
    
    # Create a tar file
    tar_file_path = Path(directory) / "matched_files.tar.gz"
    with tarfile.open(tar_file_path, "w:gz") as tar:
        for file in matching_files:
            tar.add(file, arcname=file.name)
    
    return str(tar_file_path)
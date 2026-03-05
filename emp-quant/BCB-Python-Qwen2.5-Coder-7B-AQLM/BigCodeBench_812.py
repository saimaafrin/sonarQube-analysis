
import re
from pathlib import Path
import tarfile
# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"
def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Create a Path object for the directory
    dir_path = Path(directory)
    
    # Find all files that match the pattern
    matching_files = [file for file in dir_path.glob("**/*") if re.match(file_pattern, file.name)]
    
    # If no files are found, return None
    if not matching_files:
        return None
    
    # Create a tar file with a unique name
    tar_file_path = dir_path / "AcroTray_files.tar"
    with tarfile.open(tar_file_path, "w") as tar:
        for file in matching_files:
            tar.add(file, arcname=file.name)
    
    # Return the path to the created tar file
    return str(tar_file_path)
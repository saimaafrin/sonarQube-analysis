import re
from pathlib import Path
import tarfile
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"
def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Find files matching the pattern
    matching_files = [f for f in Path(directory).rglob(file_pattern)]
    
    if not matching_files:
        return None  # No files found
    
    # Create a tar file with the matching files
    tar_filename = Path(directory) / "AcroTray_files.tar"
    with tarfile.open(tar_filename, "w") as tar:
        for file in matching_files:
            tar.add(file, arcname=file.name)
    
    return str(tar_filename)

import re
from pathlib import Path
import tarfile
# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"
def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Find files that match the pattern
    matching_files = [f for f in Path(directory).rglob('*') if re.match(file_pattern, f.as_posix())]
    
    # If no matching files are found, return None
    if not matching_files:
        return None
    
    # Create a tar file with the matching files
    tar_file = Path(directory) / "matched_files.tar"
    with tarfile.open(tar_file, 'w') as tar:
        for file in matching_files:
            tar.add(file, arcname=file.relative_to(directory))
    
    # Return the path to the created tar file
    return str(tar_file)
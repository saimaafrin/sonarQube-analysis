import re
from pathlib import Path
import tarfile
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"
def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Find files matching the pattern
    matching_files = [f for f in Path(directory).glob("**/*") if re.search(file_pattern, str(f))]
    
    if not matching_files:
        return "No files found matching the pattern."
    
    # Create a tar file to archive the matching files
    tar_file_path = Path(directory) / "archived_files.tar"
    with tarfile.open(tar_file_path, "w") as tar:
        for file in matching_files:
            tar.add(file, arcname=file.name)
    
    return str(tar_file_path)
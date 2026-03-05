
import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Create a tar file
    tar_file = Path(directory) / "archived_files.tar"
    with tarfile.open(tar_file, "w:gz") as tar:
        # Iterate over files in the directory
        for file in Path(directory).glob("**/*"):
            # Check if the file matches the pattern
            if re.search(file_pattern, file.name):
                # Add the file to the tar file
                tar.add(file, arcname=file.name)

    return tar_file

# Call the function
task_func()
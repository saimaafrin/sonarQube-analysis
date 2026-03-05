
import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Find files that match the pattern
    files = [file for file in Path(directory).iterdir() if re.match(file_pattern, file.name)]

    # Create a tar file
    with tarfile.open("archive.tar", "w:") as tar:
        for file in files:
            tar.add(file, arcname=file.name)

    return "archive.tar"
import re
from pathlib import Path
import tarfile
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"
def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    """
    Find files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, archive these files in a tar file.
    """
    # Create a tar file
    tar_file = Path(directory) / "archived_files.tar"
    with tarfile.open(tar_file, "w") as tar:
        # Find files that match the pattern
        for file in Path(directory).glob("**/*"):
            if re.search(file_pattern, file.name):
                tar.add(file, arcname=file.name)
    return tar_file
import re
from pathlib import Path
import tarfile
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"
def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, archive these files in a tar file.
    """
    # Create a tar file
    tar = tarfile.open(f"{directory}/archive.tar", "w:gz")

    # Iterate over files in the directory
    for file in Path(directory).glob("**/*"):
        # Check if the file matches the pattern
        if re.search(file_pattern, file.name):
            # Add the file to the tar file
            tar.add(file, arcname=file.name)

    # Close the tar file
    tar.close()

    # Return the path to the created tar file
    return f"{directory}/archive.tar"
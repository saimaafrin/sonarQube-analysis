
import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Create a tar file
    tar = tarfile.open("output.tar", "w:gz")

    # Iterate over the files in the directory
    for file in Path(directory).iterdir():
        # Check if the file matches the pattern
        if re.search(file_pattern, file.name):
            # Add the file to the tar file
            tar.add(file, arcname=file.name)

    # Close the tar file
    tar.close()

    # Return the path to the created tar file
    return "output.tar"

# Call the function
print(task_func())
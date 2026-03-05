
import os
import shutil
import string
# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace
def task_func(directory_path):
    # Create the directories if they don't exist
    os.makedirs(os.path.join(directory_path, "Invalid"), exist_ok=True)
    os.makedirs(os.path.join(directory_path, "Valid"), exist_ok=True)
    # Scan the directory and move files with invalid characters to the "Invalid" directory
    for file in os.listdir(directory_path):
        if any(char in file for char in INVALID_CHARACTERS):
            shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, "Invalid", file))
        else:
            shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, "Valid", file))
    # Return a summary of the files moved
    summary = {
        "Invalid": 0,
        "Valid": 0
    }
    for file in os.listdir(directory_path):
        if file in os.path.join(directory_path, "Invalid"):
            summary["Invalid"] += 1
        else:
            summary["Valid"] += 1
    return summary
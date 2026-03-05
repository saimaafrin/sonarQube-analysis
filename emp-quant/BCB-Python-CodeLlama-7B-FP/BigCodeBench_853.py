import os
import shutil
import string
INVALID_CHARACTERS = string.punctuation + string.whitespace
def task_func(directory_path):
    """
    Scan a directory and organize the files according to their endings.
    Files with invalid characters in the name will be moved to a new directory called "Invalid."
    The invalid characters are defined by the constant INVALID_CHARACTERS, which includes all punctuation and whitespace characters.
    The function should output with:
        summary (dict): A summary dictionary containing the count of files moved to each directory.
    """
    summary = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(char in INVALID_CHARACTERS for char in file):
                shutil.move(os.path.join(root, file), "Invalid")
                if "Invalid" not in summary:
                    summary["Invalid"] = 0
                summary["Invalid"] += 1
            else:
                extension = os.path.splitext(file)[1]
                if extension not in summary:
                    summary[extension] = 0
                summary[extension] += 1
    return summary
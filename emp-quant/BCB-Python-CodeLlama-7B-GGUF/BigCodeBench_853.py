
import os
import shutil
import string

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
    # Create a dictionary to store the summary
    summary = {}

    # Iterate over the files in the directory
    for file in os.listdir(directory_path):
        # Get the file name and extension
        file_name, file_extension = os.path.splitext(file)

        # Check if the file name contains any invalid characters
        if any(char in INVALID_CHARACTERS for char in file_name):
            # Move the file to the "Invalid" directory
            shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, "Invalid", file))

            # Increment the count of files moved to the "Invalid" directory
            if "Invalid" not in summary:
                summary["Invalid"] = 0
            summary["Invalid"] += 1
        else:
            # Move the file to the directory based on its extension
            shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, file_extension[1:]))

            # Increment the count of files moved to the directory based on its extension
            if file_extension[1:] not in summary:
                summary[file_extension[1:]] = 0
            summary[file_extension[1:]] += 1

    # Return the summary dictionary
    return summary
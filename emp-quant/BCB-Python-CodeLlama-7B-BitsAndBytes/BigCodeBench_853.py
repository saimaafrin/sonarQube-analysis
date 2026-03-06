
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

            # Increment the count for the "Invalid" directory
            if "Invalid" not in summary:
                summary["Invalid"] = 0
            summary["Invalid"] += 1
        else:
            # Move the file to the directory based on the file extension
            dest_dir = file_extension[1:]
            if dest_dir not in summary:
                summary[dest_dir] = 0
            summary[dest_dir] += 1
            shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, dest_dir, file))

    return summary
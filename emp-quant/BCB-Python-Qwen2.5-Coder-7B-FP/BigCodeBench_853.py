import os
import shutil
import string
INVALID_CHARACTERS = string.punctuation + string.whitespace
def task_func(directory_path):
    summary = {}
    invalid_dir = os.path.join(directory_path, "Invalid")
    
    # Create the Invalid directory if it doesn't exist
    if not os.path.exists(invalid_dir):
        os.makedirs(invalid_dir)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check for invalid characters in the file name
            if any(char in INVALID_CHARACTERS for char in file):
                # Move the file to the Invalid directory
                src_path = os.path.join(root, file)
                dst_path = os.path.join(invalid_dir, file)
                shutil.move(src_path, dst_path)
                # Update the summary
                summary[invalid_dir] = summary.get(invalid_dir, 0) + 1
    
    return summary

import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            # Check if the file name matches the pattern
            if re.match(pattern, filename):
                # Construct the new file name
                new_filename = re.sub(pattern, replacement, filename)
                # Construct full old and new file paths
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
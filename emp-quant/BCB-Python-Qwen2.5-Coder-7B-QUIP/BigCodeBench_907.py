
import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            # Check if the file matches the pattern
            if re.match(pattern, filename):
                # Create the new filename with the replacement string
                new_filename = re.sub(pattern, replacement, filename)
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
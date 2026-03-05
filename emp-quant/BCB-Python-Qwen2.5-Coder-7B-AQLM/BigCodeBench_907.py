
import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        # Compile the regular expression pattern
        regex = re.compile(pattern)
        
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            # Check if the filename matches the pattern
            if regex.search(filename):
                # Create the new filename by replacing the matched pattern
                new_filename = regex.sub(replacement, filename)
                # Construct the full old and new file paths
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f'Renamed "{filename}" to "{new_filename}"')
        
        return True
    except Exception as e:
        print(f'An error occurred: {e}')
        return False
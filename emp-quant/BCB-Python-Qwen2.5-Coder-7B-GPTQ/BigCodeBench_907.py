import os
import re
def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        # Compile the regular expression pattern
        regex = re.compile(pattern)
        
        # List all files in the directory
        files = os.listdir(directory)
        
        for filename in files:
            # Check if the filename matches the pattern
            if regex.match(filename):
                # Create the new filename by replacing the matched pattern
                new_filename = regex.sub(replacement, filename)
                
                # Construct full file paths
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(old_file_path, new_file_path)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
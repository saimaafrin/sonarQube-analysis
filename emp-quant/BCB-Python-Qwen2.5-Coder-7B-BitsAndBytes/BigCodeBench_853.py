
import os
import shutil
import string

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
    summary = {}
    
    # Create a directory for invalid files if it doesn't exist
    invalid_dir = os.path.join(directory_path, 'Invalid')
    if not os.path.exists(invalid_dir):
        os.makedirs(invalid_dir)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check if the file has any invalid characters in its name
            if any(char in INVALID_CHARACTERS for char in file):
                # Move the file to the Invalid directory
                src_file = os.path.join(root, file)
                dst_file = os.path.join(invalid_dir, file)
                shutil.move(src_file, dst_file)
                
                # Update the summary
                if 'Invalid' in summary:
                    summary['Invalid'] += 1
                else:
                    summary['Invalid'] = 1
    
    return summary
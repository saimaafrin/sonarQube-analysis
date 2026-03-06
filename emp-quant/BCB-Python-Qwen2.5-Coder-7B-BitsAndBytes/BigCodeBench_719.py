
import re
import os
import glob

def task_func(directory, word):
    """
    Count the number of files in a directory that contain a specific word.

    Args:
        directory (str): The path to the directory to search.
        word (str): The word to search for in the files.

    Returns:
        int: The number of files that contain the given word.
    """
    # Initialize the count of files containing the word
    count = 0
    
    # Use glob to get all files in the directory
    file_paths = glob.glob(os.path.join(directory, '*'))
    
    # Iterate over each file path
    for file_path in file_paths:
        # Check if the path is a file and not a directory
        if os.path.isfile(file_path):
            try:
                # Open the file and read its contents
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    # Use regular expression to find occurrences of the word
                    matches = re.findall(r'\b' + re.escape(word) + r'\b', content)
                    
                    # If any matches are found, increment the count
                    if matches:
                        count += 1
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    
    return count
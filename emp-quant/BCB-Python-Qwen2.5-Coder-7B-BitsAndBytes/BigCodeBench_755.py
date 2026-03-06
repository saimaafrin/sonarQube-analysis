
import os
import glob

def task_func(directory_path):
    # Get a list of all files in the directory
    file_paths = glob.glob(os.path.join(directory_path, '*'))
    
    new_filenames = []
    
    for file_path in file_paths:
        # Extract the filename from the full path
        filename = os.path.basename(file_path)
        
        # Split the filename into words based on periods
        words = filename.split('.')
        
        # Reverse the order of words
        reversed_words = words[::-1]
        
        # Join the reversed words back into a single string
        new_filename = '.'.join(reversed_words)
        
        # Construct the new full path
        new_file_path = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(file_path, new_file_path)
        
        # Append the new filename to the list
        new_filenames.append(new_filename)
    
    return new_filenames
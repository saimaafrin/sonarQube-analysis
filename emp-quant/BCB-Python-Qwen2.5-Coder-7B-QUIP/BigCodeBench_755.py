
import os
import glob

def task_func(directory_path):
    # Get all filenames in the directory
    filenames = glob.glob(os.path.join(directory_path, '*.*'))
    
    # Reverse the order of words in each filename
    new_filenames = [os.path.splitext(filename)[0][::-1] + os.path.splitext(filename)[1] for filename in filenames]
    
    return new_filenames
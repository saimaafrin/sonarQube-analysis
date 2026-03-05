import os
import glob
import zipfile
def task_func(directory):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Find all files in the directory (not including subdirectories)
    files = glob.glob(os.path.join(directory, '*'))
    files = [f for f in files if os.path.isfile(f)]
    
    # If no files are found, return None
    if not files:
        return None
    
    # Create a zip file named 'files.zip' in the same directory
    zip_path = os.path.join(directory, 'files.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    
    # Return the path to the created zip file
    return zip_path
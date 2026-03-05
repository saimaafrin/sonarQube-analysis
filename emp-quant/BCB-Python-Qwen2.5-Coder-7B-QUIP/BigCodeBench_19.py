
import os
import glob
import zipfile
def task_func(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist")
    
    # Get a list of all files in the directory
    files = glob.glob(os.path.join(directory, '*'))
    
    # Check if there are any files in the directory
    if not files:
        return None
    
    # Create a zip file
    zip_path = os.path.join(directory, 'files.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            if os.path.isfile(file):
                zipf.write(file, os.path.basename(file))
    
    return zip_path
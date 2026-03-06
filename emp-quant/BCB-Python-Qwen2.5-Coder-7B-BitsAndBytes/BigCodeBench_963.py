
import os
import glob
from pathlib import Path
import zipfile

def task_func(source_directory, target_directory, zip_name):
    # Define valid extensions
    valid_extensions = ['.txt', '.docx', '.xlsx', '.csv']
    
    # Check if source directory exists
    if not os.path.exists(source_directory):
        raise OSError(f"The source directory {source_directory} does not exist.")
    
    # Create target directory if it doesn't exist
    Path(target_directory).mkdir(parents=True, exist_ok=True)
    
    # Construct the full path for the zip file
    zip_path = Path(target_directory) / f"{zip_name}.zip"
    
    # Find all files with valid extensions in the source directory
    files_to_zip = []
    for ext in valid_extensions:
        files_to_zip.extend(glob.glob(os.path.join(source_directory, f"*{ext}")))
    
    # Create a zip file and add the found files
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files_to_zip:
            zipf.write(file, arcname=os.path.basename(file))
    
    # Return the full path to the created zip file
    return str(zip_path)

import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    """
    Unzip all zip files in a directory whose name matches a certain pattern by splitting the filename the last time "-" occurs 
    and using the prefix part of the filename as the directory to extract.

    Args:
        directory (str): The directory containing the zip files.
        pattern (str): The regex pattern to match the filenames.

    Returns:
        list: A list of directories where the files were extracted.
    """
    extracted_dirs = []
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        if re.match(pattern, filename):
            # Split the filename at the last occurrence of "-"
            prefix, _ = filename.rsplit('-', 1)
            
            # Create the extraction directory if it doesn't exist
            extraction_dir = os.path.join(directory, prefix)
            if not os.path.exists(extraction_dir):
                os.makedirs(extraction_dir)
                
            # Extract the zip file to the new directory
            zip_path = os.path.join(directory, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extraction_dir)
                
            # Add the extraction directory to the list
            extracted_dirs.append(extraction_dir)
    
    return extracted_dirs
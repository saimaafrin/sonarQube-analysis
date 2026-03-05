
import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    extracted_directories = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if re.match(pattern, filename):
            # Extract the prefix part of the filename
            prefix = re.match(pattern, filename).group(1)
            # Create the extraction directory
            extract_dir = os.path.join(directory, prefix)
            if not os.path.exists(extract_dir):
                os.makedirs(extract_dir)
            # Extract the zip file
            with zipfile.ZipFile(os.path.join(directory, filename), 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            # Add the extraction directory to the list
            extracted_directories.append(extract_dir)

    return extracted_directories
import re
import os
import zipfile
def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    """
    Unzip all zip files in a directory whose name matches a certain pattern by splitting the filename the last time "-" occurs and using the prefix part of the filename as the directory to extract.
    """
    # Create a list to store the extracted directories
    extracted_dirs = []

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Check if the file name matches the pattern
        if re.match(pattern, file):
            # Split the filename at the last "-"
            prefix, suffix = file.rsplit('-', 1)

            # Create a new directory with the prefix as the name
            new_dir = os.path.join(directory, prefix)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

            # Extract the zip file to the new directory
            with zipfile.ZipFile(os.path.join(directory, file), 'r') as zip_ref:
                zip_ref.extractall(new_dir)

            # Add the new directory to the list of extracted directories
            extracted_dirs.append(new_dir)

    return extracted_dirs
directory = 'path/to/directory'
pattern = r'^(.*?)-\d+\.zip$'
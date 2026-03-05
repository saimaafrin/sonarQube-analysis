import re
import os
import zipfile
def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    """
    Unzip all zip files in a directory whose name matches a certain pattern by splitting the filename the last time "-" occurs and using the prefix part of the filename as the directory to extract.
    """
    # Create a list to store the directories where the files were extracted
    extracted_dirs = []

    # Iterate over all files in the directory
    for file in os.listdir(directory):
        # Check if the file name matches the pattern
        if re.match(pattern, file):
            # Split the filename at the last occurrence of "-"
            prefix, _ = file.rsplit('-', 1)

            # Create a directory with the prefix as the name
            extracted_dir = os.path.join(directory, prefix)
            if not os.path.exists(extracted_dir):
                os.makedirs(extracted_dir)

            # Extract the zip file to the new directory
            with zipfile.ZipFile(os.path.join(directory, file), 'r') as zip_ref:
                zip_ref.extractall(extracted_dir)

            # Add the directory to the list of extracted directories
            extracted_dirs.append(extracted_dir)

    return extracted_dirs
directory = 'path/to/directory'
pattern = r'^(.*?)-\d+\.zip$'
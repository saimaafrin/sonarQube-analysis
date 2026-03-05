
import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    """
    Unzip all zip files in a directory whose name matches a certain pattern by splitting the filename the last time "-" occurs and using the prefix part of the filename as the directory to extract.
    """
    directories = []
    for file in os.listdir(directory):
        if re.match(pattern, file):
            prefix, _ = file.rsplit('-', 1)
            zip_file = os.path.join(directory, file)
            with zipfile.ZipFile(zip_file, 'r') as zf:
                zf.extractall(os.path.join(directory, prefix))
            directories.append(os.path.join(directory, prefix))
    return directories
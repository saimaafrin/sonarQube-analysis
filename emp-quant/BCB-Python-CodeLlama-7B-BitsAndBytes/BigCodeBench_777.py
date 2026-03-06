
import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    """
    Unzip all zip files in a directory whose name matches a certain pattern by splitting the filename the last time "-" occurs and using the prefix part of the filename as the directory to extract.
    """
    directories = []
    for filename in os.listdir(directory):
        if re.match(pattern, filename):
            prefix, _ = filename.rsplit('-', 1)
            with zipfile.ZipFile(os.path.join(directory, filename), 'r') as zip_file:
                zip_file.extractall(os.path.join(directory, prefix))
            directories.append(os.path.join(directory, prefix))
    return directories
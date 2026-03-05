
import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    directories = []
    for file in os.listdir(directory):
        if re.match(pattern, file):
            prefix = re.match(r'^(.*?)-\d+\.zip$', file).group(1)
            directory = os.path.join(directory, prefix)
            if not os.path.exists(directory):
                os.makedirs(directory)
            directories.append(directory)
            with zipfile.ZipFile(os.path.join(directory, file), 'r') as zf:
                zf.extractall(directory)
    return directories
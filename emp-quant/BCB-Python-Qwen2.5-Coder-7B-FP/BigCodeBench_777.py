import re
import os
import zipfile
def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    extracted_dirs = []
    for filename in os.listdir(directory):
        if re.match(pattern, filename):
            prefix, _ = re.match(pattern, filename).groups()
            extract_dir = os.path.join(directory, prefix)
            if not os.path.exists(extract_dir):
                os.makedirs(extract_dir)
            with zipfile.ZipFile(os.path.join(directory, filename), 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            extracted_dirs.append(extract_dir)
    return extracted_dirs
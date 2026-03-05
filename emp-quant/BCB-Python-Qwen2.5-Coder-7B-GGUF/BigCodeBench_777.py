
import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    extracted_directories = []
    for filename in os.listdir(directory):
        if re.match(pattern, filename):
            prefix, _ = re.match(pattern, filename).groups()
            extract_path = os.path.join(directory, prefix)
            if not os.path.exists(extract_path):
                os.makedirs(extract_path)
            with zipfile.ZipFile(os.path.join(directory, filename), 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            extracted_directories.append(extract_path)
    return extracted_directories
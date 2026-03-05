import re
import os
import zipfile
def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    extracted_directories = []
    for filename in os.listdir(directory):
        if re.match(pattern, filename):
            prefix, _ = re.match(pattern, filename).groups()
            extract_dir = os.path.join(directory, prefix)
            if not os.path.exists(extract_dir):
                os.makedirs(extract_dir)
            zip_path = os.path.join(directory, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            extracted_directories.append(extract_dir)
    return extracted_directories

import re
import os
import glob

def task_func(dir_path):
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist")
    
    error_count_dict = {}
    pattern = re.compile(r'\berror\b', re.IGNORECASE)
    
    for file_path in glob.glob(os.path.join(dir_path, '**', '*.txt'), recursive=True):
        with open(file_path, 'r') as file:
            content = file.read()
            count = len(pattern.findall(content))
            relative_path = os.path.relpath(file_path, dir_path)
            error_count_dict[relative_path] = count
    
    return error_count_dict
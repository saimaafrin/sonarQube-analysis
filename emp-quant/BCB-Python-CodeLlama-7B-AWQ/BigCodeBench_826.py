import re
import os
import shutil
def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    moved_files_count = 0
    for file in os.listdir(source_dir):
        if re.search(file_pattern, file):
            shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))
            moved_files_count += 1
    return moved_files_count
source_dir = 'source_dir'
target_dir = 'target_dir'
file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
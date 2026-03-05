
import difflib
import gzip

def task_func(file_path1, file_path2):
    with gzip.open(file_path1, 'rt') as f1, gzip.open(file_path2, 'rt') as f2:
        diff = difflib.unified_diff(f1, f2, lineterm='')
        return '\n'.join(diff)
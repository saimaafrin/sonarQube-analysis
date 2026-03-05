
import difflib
import gzip

def task_func(file_path1, file_path2):
    with gzip.open(file_path1, 'rb') as f1, gzip.open(file_path2, 'rb') as f2:
        contents1 = f1.read()
        contents2 = f2.read()

    diff = difflib.unified_diff(contents1, contents2)
    return ''.join(diff)
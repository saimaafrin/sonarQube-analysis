
import difflib
import gzip

def task_func(file_path1, file_path2):
    with gzip.open(file_path1, 'rb') as file1:
        contents1 = file1.read()
    with gzip.open(file_path2, 'rb') as file2:
        contents2 = file2.read()
    diff = difflib.Difference(contents1, contents2)
    diff_str = ''.join(diff)
    return diff_str
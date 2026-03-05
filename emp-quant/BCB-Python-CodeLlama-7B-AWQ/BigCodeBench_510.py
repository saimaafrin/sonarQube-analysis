import difflib
import gzip
def task_func(file_path1, file_path2):
    """
    Compares the contents of two gzip files and returns a string describing the differences between them.
    """
    with gzip.open(file_path1, 'rb') as file1, gzip.open(file_path2, 'rb') as file2:
        contents1 = file1.read()
        contents2 = file2.read()
    diff = difflib.unified_diff(contents1, contents2)
    return ''.join(diff)
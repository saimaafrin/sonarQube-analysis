import difflib
import gzip
def task_func(file_path1, file_path2):
    """
    Compares the contents of two gzip files and returns a string describing the differences between them.
    """
    with gzip.open(file_path1, 'rb') as file1, gzip.open(file_path2, 'rb') as file2:
        file1_content = file1.read()
        file2_content = file2.read()

    diff = difflib.unified_diff(file1_content, file2_content, fromfile=file_path1, tofile=file_path2)
    diff_string = ''.join(diff)

    if diff_string:
        return diff_string
    else:
        return ''
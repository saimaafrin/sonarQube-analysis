import difflib
import gzip
def task_func(file_path1, file_path2):
    """
    Compares the contents of two gzip files and returns a string describing the differences between them.
    It reads the contents of each file, then uses difflib to compute and return the differences. 
    Only differences are returned, with an empty string indicating no differences.

    Parameters:
    file_path1 (str): The file path of the first gzip file.
    file_path2 (str): The file path of the second gzip file.

    Returns:
    str: A string describing the differences between the two files' contents.

    Requirements:
    - difflib
    - gzip

    Examples:
    Assuming 'file1.gz' and 'file2.gz' contain slightly different text,
    >>> result = task_func('file1.gz', 'file2.gz')
    >>> len(result) > 0
    True

    Assuming 'file1.gz' and 'file1.gz' are identical,
    >>> task_func('file1.gz', 'file1.gz')
    ''
    """
    with gzip.open(file_path1, 'rb') as f1, gzip.open(file_path2, 'rb') as f2:
        contents1 = f1.read().decode('utf-8')
        contents2 = f2.read().decode('utf-8')
        diff = difflib.unified_diff(contents1.splitlines(True), contents2.splitlines(True), fromfile=file_path1, tofile=file_path2)
        return ''.join(diff)
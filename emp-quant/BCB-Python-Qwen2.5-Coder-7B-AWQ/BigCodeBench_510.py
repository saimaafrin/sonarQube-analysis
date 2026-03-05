import difflib
import gzip
def task_func(file_path1, file_path2):
    """
    Compares the contents of two gzip files and returns a string describing the differences between them.
    
    Args:
    file_path1 (str): The path to the first gzip file.
    file_path2 (str): The path to the second gzip file.
    
    Returns:
    str: A string describing the differences between the two files' contents. An empty string indicates no differences.
    """
    with gzip.open(file_path1, 'rt') as file1, gzip.open(file_path2, 'rt') as file2:
        content1 = file1.readlines()
        content2 = file2.readlines()
    
    differ = difflib.Differ()
    diff = list(differ.compare(content1, content2))
    
    # Filter out unchanged lines
    diff = [line for line in diff if line.startswith('-') or line.startswith('+')]
    
    return '\n'.join(diff)
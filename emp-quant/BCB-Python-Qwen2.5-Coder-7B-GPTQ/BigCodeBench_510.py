import difflib
import gzip
def task_func(file_path1, file_path2):
    # Open and read the contents of the first file
    with gzip.open(file_path1, 'rt') as file1:
        content1 = file1.read()
    
    # Open and read the contents of the second file
    with gzip.open(file_path2, 'rt') as file2:
        content2 = file2.read()
    
    # Use difflib to compute the differences between the two files
    diff = difflib.unified_diff(content1.splitlines(), content2.splitlines(), fromfile=file_path1, tofile=file_path2)
    
    # Join the differences into a single string and return
    return '\n'.join(diff)
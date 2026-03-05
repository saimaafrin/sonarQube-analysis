
import difflib
import gzip

def task_func(file_path1, file_path2):
    with gzip.open(file_path1, 'rt') as file1, gzip.open(file_path2, 'rt') as file2:
        content1 = file1.read()
        content2 = file2.read()
    
    differ = difflib.Differ()
    diff = list(differ.compare(content1.splitlines(), content2.splitlines()))
    
    # Filter out unchanged lines
    diff = [line for line in diff if line.startswith('-') or line.startswith('+')]
    
    return '\n'.join(diff) if diff else ''

import difflib
import gzip

def task_func(file_path1, file_path2):
    with gzip.open(file_path1, 'rt') as file1, gzip.open(file_path2, 'rt') as file2:
        content1 = file1.readlines()
        content2 = file2.readlines()
    
    differ = difflib.Differ()
    diff = list(differ.compare(content1, content2))
    
    return '\n'.join(diff)
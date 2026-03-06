
import difflib
import gzip

def task_func(file_path1, file_path2):
    with gzip.open(file_path1, 'rb') as file1, gzip.open(file_path2, 'rb') as file2:
        contents1 = file1.read()
        contents2 = file2.read()
        diff = difflib.ndiff(contents1, contents2)
        differences = ''.join(diff)
        return differences

print(task_func('file1.gz', 'file2.gz'))
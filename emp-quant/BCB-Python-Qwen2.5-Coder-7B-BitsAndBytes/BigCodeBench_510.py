
import difflib
import gzip

def task_func(file_path1, file_path2):
    # Open and read the contents of both gzip files
    with gzip.open(file_path1, 'rt') as file1, gzip.open(file_path2, 'rt') as file2:
        content1 = file1.readlines()
        content2 = file2.readlines()

    # Use difflib to compare the contents of the two files
    diff = difflib.unified_diff(content1, content2, fromfile=file_path1, tofile=file_path2)

    # Join the differences into a single string
    diff_str = '\n'.join(diff)

    # Return the differences or an empty string if there are none
    return diff_str if diff_str else ''
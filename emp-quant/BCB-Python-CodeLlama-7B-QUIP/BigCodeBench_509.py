
import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    # Read the files
    with open(file_path1, 'r') as file1:
        reader1 = csv.reader(file1, delimiter=delimiter, quotechar=quotechar)
        lines1 = [line for line in reader1]
    with open(file_path2, 'r') as file2:
        reader2 = csv.reader(file2, delimiter=delimiter, quotechar=quotechar)
        lines2 = [line for line in reader2]

    # Compare the lines
    diff = ndiff(lines1, lines2)

    # Create the DataFrame
    data = {'Line Number': [], 'Status': [], 'Content': []}
    for line in diff:
        data['Line Number'].append(line.line_num)
        if line.type == 'equal':
            data['Status'].append(' ')
        elif line.type == 'insert':
            data['Status'].append('+')
        elif line.type == 'delete':
            data['Status'].append('-')
        data['Content'].append(line.line_num)

    # Create the DataFrame
    df = pd.DataFrame(data)

    return df
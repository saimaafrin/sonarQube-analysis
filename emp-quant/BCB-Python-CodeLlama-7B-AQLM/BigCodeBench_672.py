import csv
import sys
def task_func(filename):
    """
    Read a CSV file, inverse the order of the lines and write the inverted lines back into the file. Then reset the cursor to the beginning of the file.

    Parameters:
    - filename (str): The name of the CSV file.

    Returns:
    - filename (str): The name of the CSV file.

    Requirements:
    - csv
    - sys

    Example:
    >>> task_func('file.csv')
    'file.csv'
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        lines.reverse()
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
    f.seek(0)
    return filename
import os
import os.path
import csv
import collections
FILE_NAME = 'file_sizes.csv'
def task_func(my_path):
    """
    Create a report on the file size in a directory and write it to a CSV file.

    Parameters:
    my_path (str): The directory path.

    Returns:
    str: The path of the CSV file.

    Requirements:
    - os
    - os.path
    - csv
    - collections

    Example:
    >>> task_func('/usr/my_directory')
    """
    # Create a list of tuples with the file name and size
    file_list = []
    for root, dirs, files in os.walk(my_path):
        for file in files:
            file_list.append((file, os.path.getsize(os.path.join(root, file))))

    # Sort the list by file size
    file_list.sort(key=lambda x: x[1], reverse=True)

    # Create the CSV file
    with open(FILE_NAME, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['File Name', 'Size'])
        for file in file_list:
            writer.writerow(file)

    return os.path.abspath(FILE_NAME)
import collections
import operator
import os
import shutil
def task_func(data_dict, source_directory, backup_directory):
    """
    Modifies a dictionary, sorts it by the frequency of its values, and backs up files from a source directory.
    This function performs three main tasks:
        1. Updates the input dictionary by adding a key 'a' with the value 1.
        2. Sorts the dictionary by the frequency of its values in descending order.
        3. Backs up all files from the specified source directory to a backup directory.
    """
    # Update the input dictionary with the new key and value
    data_dict['a'] = 1

    # Sort the dictionary by the frequency of its values in descending order
    value_frequencies = collections.Counter(data_dict.values()).most_common()

    # Back up all files from the source directory to the backup directory
    backup_status = shutil.copytree(source_directory, backup_directory)

    return data_dict, value_frequencies, backup_status
data_dict = {'avc': '1', 'hello': 'world', 'test': 'world', 'cat': 'meow'}
source_directory = 'to_backup'
backup_directory = 'backup'
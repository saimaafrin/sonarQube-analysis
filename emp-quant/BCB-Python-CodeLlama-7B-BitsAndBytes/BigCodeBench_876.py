
import collections
import operator
import os
import shutil

def task_func(data_dict, source_directory, backup_directory):
    # Update the input dictionary with a new key-value pair
    data_dict['a'] = 1

    # Sort the dictionary by the frequency of its values in descending order
    value_frequencies = collections.Counter(data_dict.values()).most_common()

    # Backup all files from the specified source directory to a backup directory
    backup_status = shutil.copytree(source_directory, backup_directory)

    return data_dict, value_frequencies, backup_status

print(updated_dict)
print(value_frequencies)
print(backup_status)
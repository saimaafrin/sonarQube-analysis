import collections
import operator
import os
import shutil
def task_func(data_dict, source_directory, backup_directory):
    # Task 1: Update the dictionary
    data_dict['a'] = 1
    
    # Task 2: Sort the dictionary by the frequency of its values
    value_counts = collections.Counter(data_dict.values())
    sorted_items = sorted(value_counts.items(), key=operator.itemgetter(1), reverse=True)
    
    # Task 3: Backup files from the source directory
    backup_status = True
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    for filename in os.listdir(source_directory):
        source_file = os.path.join(source_directory, filename)
        backup_file = os.path.join(backup_directory, filename)
        try:
            shutil.copy2(source_file, backup_file)
        except Exception as e:
            print(f"Error backing up {filename}: {e}")
            backup_status = False
    
    return data_dict, sorted_items, backup_status
data_dict = {'avc': '1', 'hello': 'world', 'test': 'world', 'cat': 'meow'}
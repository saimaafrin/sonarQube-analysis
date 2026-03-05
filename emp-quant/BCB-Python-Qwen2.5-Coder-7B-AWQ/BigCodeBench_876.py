import collections
import operator
import os
import shutil
def task_func(data_dict, source_directory, backup_directory):
    # Update the dictionary by adding a key 'a' with the value 1
    data_dict['a'] = 1
    
    # Count the frequency of each value in the dictionary
    value_counts = collections.Counter(data_dict.values())
    
    # Sort the dictionary by the frequency of its values in descending order
    sorted_items = sorted(value_counts.items(), key=operator.itemgetter(1), reverse=True)
    
    # Backup all files from the source directory to the backup directory
    backup_status = True
    try:
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)
        for item in os.listdir(source_directory):
            source_path = os.path.join(source_directory, item)
            backup_path = os.path.join(backup_directory, item)
            if os.path.isfile(source_path):
                shutil.copy2(source_path, backup_path)
    except Exception as e:
        print(f"An error occurred during backup: {e}")
        backup_status = False
    
    return data_dict, sorted_items, backup_status
data_dict = {'avc': '1', 'hello': 'world', 'test': 'world', 'cat': 'meow'}
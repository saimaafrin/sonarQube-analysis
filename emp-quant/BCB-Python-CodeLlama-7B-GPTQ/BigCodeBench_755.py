import os
import glob
def task_func(directory_path):
    """
    Reverse the order of words in all the filenames of a directory, where words are separated by periods.
    """
    new_filenames = []
    for filename in glob.glob(os.path.join(directory_path, '*')):
        new_filename = '.'.join(reversed(filename.split('.')))
        new_filenames.append(new_filename)
    return new_filenames
directory_path = 'path/to/directory'
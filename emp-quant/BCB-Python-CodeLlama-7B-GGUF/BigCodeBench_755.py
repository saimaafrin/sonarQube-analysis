
import os
import glob

def task_func(directory_path):
    filenames = glob.glob(os.path.join(directory_path, '*'))
    new_filenames = []
    for filename in filenames:
        words = filename.split('.')
        new_words = words[::-1]
        new_filename = '.'.join(new_words)
        new_filenames.append(new_filename)
    return new_filenames
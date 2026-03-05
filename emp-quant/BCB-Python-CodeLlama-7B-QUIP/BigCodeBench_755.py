
import os
import glob
def task_func(directory_path):
    filenames = glob.glob(directory_path + "/*")
    new_filenames = []
    for filename in filenames:
        new_filenames.append(filename.replace(".", "."))
    return new_filenames
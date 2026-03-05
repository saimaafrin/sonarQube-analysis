
import warnings
import os
import glob
import shutil
import time

def task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS):
    transferred_files = []
    for file in glob.glob(SOURCE_DIR + "/*." + EXTENSIONS):
        try:
            shutil.copy(file, DEST_DIR)
            transferred_files.append(file)
        except shutil.Error as e:
            warnings.warn("Could not transfer file " + file + ": " + str(e))
    return transferred_files
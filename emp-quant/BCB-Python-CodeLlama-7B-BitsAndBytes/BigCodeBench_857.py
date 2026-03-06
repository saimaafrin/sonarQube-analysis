
import warnings
import os
import glob
import shutil
import time

def task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS):
    transferred_files = []
    for extension in EXTENSIONS:
        for file in glob.glob(os.path.join(SOURCE_DIR, '*.' + extension)):
            try:
                shutil.copy(file, DEST_DIR)
                transferred_files.append(os.path.basename(file))
            except Exception as e:
                warnings.warn(f'Failed to transfer file {file}: {e}')
    return transferred_files

import warnings
import os
import glob
import shutil
import time

def task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS):
    transferred_files = []
    for extension in EXTENSIONS:
        files = glob.glob(f"{SOURCE_DIR}/*.{extension}")
        for file in files:
            try:
                shutil.copy(file, DEST_DIR)
                transferred_files.append(file)
            except Exception as e:
                warnings.warn(f"Failed to transfer file {file}: {e}")
    return transferred_files
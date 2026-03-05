
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    file_names = glob.glob(os.path.join(directory, file_pattern))
    file_types = {}
    for file_name in file_names:
        file_type = mimetypes.guess_type(file_name)[0]
        if file_type is not None:
            file_types[file_name] = file_type
    return file_types
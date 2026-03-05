
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    file_names = []
    file_types = []
    for file_name in glob.glob(os.path.join(directory, file_pattern)):
        if file_name.endswith(suffix):
            file_names.append(file_name)
            file_types.append(mimetypes.guess_type(file_name)[0])
    return {file_names: file_types}
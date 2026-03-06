
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    file_names = []
    for file in glob.glob(os.path.join(directory, file_pattern)):
        if file.endswith(suffix):
            file_names.append(file)

    mime_types = {}
    for file in file_names:
        mime_type = mimetypes.guess_type(file)[0]
        mime_types[file] = mime_type

    return mime_types

mime_types = task_func(directory, file_pattern, suffix)
print(mime_types)
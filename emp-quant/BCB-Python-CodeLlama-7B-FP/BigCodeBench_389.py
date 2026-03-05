import re
import os
import shutil
def task_func(directory):
    """
    Find files with filenames that contain "like" or "what" in a directory,
    create a new subdirectory called "Interesting Files", and move those files to the new subdirectory.
    """
    interesting_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(r"like|what", file):
                interesting_files.append(os.path.join(root, file))
    if not os.path.exists("Interesting Files"):
        os.mkdir("Interesting Files")
    for file in interesting_files:
        shutil.move(file, "Interesting Files")
    return interesting_files
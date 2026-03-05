
import re
import os
import shutil

def task_func(directory):
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

import re
import os
import shutil

def task_func(directory):
    interesting_files = []
    for file in os.listdir(directory):
        if re.search(r"like|what", file):
            interesting_files.append(file)
    if len(interesting_files) > 0:
        shutil.move(directory + "/Interesting Files", directory + "/Interesting Files")
        for file in interesting_files:
            shutil.move(directory + "/" + file, directory + "/Interesting Files/" + file)
    return interesting_files
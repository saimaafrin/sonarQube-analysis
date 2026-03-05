
import os
import logging

def task_func(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    jquery_removal_log = "jquery_removal.log"
    removed_files = []
    num_removed = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if "jquery" in file:
                removed_files.append(os.path.join(root, file))
                num_removed += 1

    with open(jquery_removal_log, "w") as f:
        for file in removed_files:
            f.write(f"{file}\n")

    return num_removed, removed_files
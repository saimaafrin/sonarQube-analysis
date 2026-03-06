
import re
import os
import shutil

def task_func(directory):
    # Create a new subdirectory called "Interesting Files"
    interesting_files_dir = os.path.join(directory, "Interesting Files")
    os.mkdir(interesting_files_dir)

    # Find files with filenames that contain "like" or "what"
    like_what_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(r"like|what", file):
                like_what_files.append(os.path.join(root, file))

    # Move the files to the new subdirectory
    for file in like_what_files:
        shutil.move(file, interesting_files_dir)

    # Output the list of files moved
    print("Moved files:")
    for file in like_what_files:
        print(file)
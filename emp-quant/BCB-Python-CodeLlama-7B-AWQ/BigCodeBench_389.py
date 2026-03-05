import re
import os
import shutil
def task_func(directory):
    """
    Find files with filenames that contain "like" or "what" in a directory,
    create a new subdirectory called "Interesting Files" and move those files to the new subdirectory.
    """
    # Create a list of files with filenames that contain "like" or "what"
    files_to_move = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(r"like|what", file):
                files_to_move.append(os.path.join(root, file))

    # Create a new subdirectory called "Interesting Files"
    interesting_files_dir = os.path.join(directory, "Interesting Files")
    if not os.path.exists(interesting_files_dir):
        os.makedirs(interesting_files_dir)

    # Move the files to the new subdirectory
    for file in files_to_move:
        shutil.move(file, interesting_files_dir)

    # Output the list of files moved
    print("List of files moved:")
    for file in files_to_move:
        print(file)
directory = "path/to/directory"
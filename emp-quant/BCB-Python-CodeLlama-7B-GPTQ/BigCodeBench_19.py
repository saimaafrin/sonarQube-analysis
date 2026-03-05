import os
import glob
import zipfile
def task_func(directory):
    """
    Zips all files (not including subdirectories) located in the specified directory and returns the path to the created zip file.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    files = glob.glob(os.path.join(directory, "**", "*.txt"), recursive=True)
    if not files:
        return None

    with zipfile.ZipFile("files.zip", "w") as zip_file:
        for file in files:
            zip_file.write(file, os.path.basename(file))

    return "files.zip"
directory = "path/to/directory"
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

    zip_file = os.path.join(directory, "files.zip")
    with zipfile.ZipFile(zip_file, "w") as zf:
        for file in files:
            zf.write(file)

    return zip_file
directory = "path/to/directory"
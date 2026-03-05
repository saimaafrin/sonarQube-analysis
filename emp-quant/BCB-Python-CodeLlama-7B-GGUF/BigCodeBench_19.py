
import os
import glob
import zipfile

def task_func(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    file_paths = glob.glob(os.path.join(directory, "*.txt"))
    if not file_paths:
        return None

    zip_file_path = os.path.join(directory, "files.zip")
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        for file_path in file_paths:
            zip_file.write(file_path)

    return zip_file_path
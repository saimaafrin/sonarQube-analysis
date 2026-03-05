
import shutil
import pathlib

def task_func(source_path, destination_path):
    if not pathlib.Path(source_path).exists() or not pathlib.Path(source_path).is_dir():
        raise ValueError("Source path does not exist or is not a directory")

    filenames = [f for f in pathlib.Path(source_path).iterdir() if f.is_file()]
    for filename in filenames:
        shutil.copy(filename, destination_path)

    return (source_path, filenames)
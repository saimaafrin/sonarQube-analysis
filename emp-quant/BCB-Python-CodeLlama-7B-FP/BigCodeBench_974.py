import shutil
import pathlib
def task_func(source_path, destination_path):
    """
    Lists files in the specified source directory without descending into subdirectories and copies them to a destination directory.
    """
    if not pathlib.Path(source_path).exists() or not pathlib.Path(source_path).is_dir():
        raise ValueError("Source path does not exist or is not a directory.")

    source_dir = pathlib.Path(source_path)
    destination_dir = pathlib.Path(destination_path)

    filenames = []
    for file in source_dir.iterdir():
        if file.is_file():
            shutil.copy(file, destination_dir)
            filenames.append(file.name)

    return (source_dir.name, filenames)
source_path = "path/to/source/directory"
destination_path = "path/to/destination/directory"
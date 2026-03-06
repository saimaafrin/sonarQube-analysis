
import shutil
import pathlib

def task_func(source_path, destination_path):
    # Check if source_path exists and is a directory
    if not pathlib.Path(source_path).is_dir():
        raise ValueError(f"{source_path} does not exist or is not a directory")

    # Get a list of filenames in the source directory
    filenames = [pathlib.Path(source_path).joinpath(filename).name for filename in pathlib.Path(source_path).iterdir()]

    # Copy the files to the destination directory
    for filename in filenames:
        shutil.copy(pathlib.Path(source_path).joinpath(filename), pathlib.Path(destination_path).joinpath(filename))

    # Return the name of the source directory and the list of copied filenames
    return (pathlib.Path(source_path).name, filenames)
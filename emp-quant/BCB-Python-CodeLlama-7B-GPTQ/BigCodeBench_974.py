import shutil
import pathlib
def task_func(source_path, destination_path):
    """
    Copies files from the specified source directory to the destination directory without descending into subdirectories.

    Args:
        source_path (str): Path to the source directory.
        destination_path (str): Path to the destination directory.

    Returns:
        Tuple[str, List[str]]: A tuple containing the name of the source directory and a list of filenames (not
        full paths) that were copied.

    Raises:
        ValueError: If source_path does not exist or is not a directory.
    """
    source_path = pathlib.Path(source_path)
    destination_path = pathlib.Path(destination_path)

    if not source_path.exists() or not source_path.is_dir():
        raise ValueError(f"Source path '{source_path}' does not exist or is not a directory.")

    filenames = []
    for file in source_path.iterdir():
        if file.is_file():
            shutil.copy(file, destination_path / file.name)
            filenames.append(file.name)

    return (source_path.name, filenames)
source_path = "source_dir"
destination_path = "destination_dir"
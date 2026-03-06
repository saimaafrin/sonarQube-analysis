import os
from pathlib import Path
import glob
import shutil
def task_func(source_directory: str, target_directory: str):
    """
    Moves files with specific extensions from a source directory to a target directory,
    handling naming conflicts by renaming duplicates.

    Parameters:
    - source_directory (str): The absolute or relative path of the source directory.
    - target_directory (str): The absolute or relative path of the target directory.
                              This function will create it if it does not exist.

    Returns:
    - int: The number of files successfully moved.

    Raises:
    - FileNotFoundError: If source_directory does not exist.

    Requirements:
    - os
    - pathlib
    - glob
    - shutil

    Notes:
    - This function scans the source directory recursively to find files.
    - Files are filtered by the extensions: ".txt", ".docx", ".xlsx", ".csv".
    - Renaming of files due to naming conflicts follows the pattern '<original_name>-n.<extension>'.

    Examples:
    >>> task_func('./source_folder', './target_folder')
    3
    >>> task_func('./empty_folder', './target_folder')
    0
    """
    source_directory = Path(source_directory)
    target_directory = Path(target_directory)

    if not source_directory.exists():
        raise FileNotFoundError(f'Source directory {source_directory} does not exist.')

    if not target_directory.exists():
        target_directory.mkdir(parents=True)

    files_to_move = []
    for file in source_directory.rglob('*'):
        if file.is_file() and file.suffix in ['.txt', '.docx', '.xlsx', '.csv']:
            files_to_move.append(file)

    files_moved = 0
    for file in files_to_move:
        target_file = target_directory / file.name
        if target_file.exists():
            target_file = target_file.with_name(f'{file.stem}-{files_moved}{file.suffix}')
        shutil.move(file, target_file)
        files_moved += 1

    return files_moved
import shutil
from pathlib import Path
from typing import List
def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    """
    Move all files with certain extensions from one directory to another.

    Args:
        source_dir (str): The source directory.
        target_dir (str): The target directory.
        extensions (List[str]): The extensions of the files to move.

    Returns:
        int: The number of moved files.

    Raises:
        ValueError: If source_dir or target_dir does not exist.
    """
    if not Path(source_dir).exists():
        raise ValueError(f"Source directory {source_dir} does not exist.")
    if not Path(target_dir).exists():
        raise ValueError(f"Target directory {target_dir} does not exist.")

    moved_files = 0
    for extension in extensions:
        for file in Path(source_dir).glob(f"**/*.{extension}"):
            shutil.move(file, target_dir)
            moved_files += 1

    return moved_files
source_dir = "source"
target_dir = "target"
extensions = [".txt"]
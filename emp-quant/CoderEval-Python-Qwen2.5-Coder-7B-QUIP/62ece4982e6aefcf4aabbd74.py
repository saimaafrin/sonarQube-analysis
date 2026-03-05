import os
import shutil
from pathlib import Path
from typing import Optional, Union

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[Path, str] = "/tmp",
) -> str:
    """
    Given an existing archive_path, uncompress it.
    Returns a file repo url which can be used as origin url.

    This does not deal with the case where the archive passed along does not exist.
    @param archive_path : archive file path
    @param filename: File name
    @param tmp_path: Temporary file path
    @return Repo URL
    """
    # Ensure the archive exists
    if not os.path.exists(archive_path):
        raise FileNotFoundError(f"Archive not found: {archive_path}")

    # Extract the archive to a temporary directory
    temp_dir = Path(tmp_path) / "repo_temp"
    temp_dir.mkdir(exist_ok=True)

    shutil.unpack_archive(archive_path, temp_dir)

    # Get the repository URL
    repo_url = temp_dir / filename

    # Clean up the temporary directory
    shutil.rmtree(temp_dir)

    return str(repo_url)
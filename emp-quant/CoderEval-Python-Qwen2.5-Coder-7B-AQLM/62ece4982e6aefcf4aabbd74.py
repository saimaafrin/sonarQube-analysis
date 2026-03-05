import os
import shutil
import tempfile
from pathlib import Path
from typing import Optional, Union

def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
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
    if filename is None:
        filename = os.path.basename(archive_path)

    temp_dir = Path(tmp_path) / tempfile.mkdtemp()
    temp_file = temp_dir / filename

    shutil.copy(archive_path, temp_file)

    if filename.endswith('.zip'):
        import zipfile
        with zipfile.ZipFile(temp_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    elif filename.endswith('.tar.gz') or filename.endswith('.tgz'):
        import tarfile
        with tarfile.open(temp_file, 'r:gz') as tar_ref:
            tar_ref.extractall(temp_dir)
    elif filename.endswith('.tar.bz2'):
        import tarfile
        with tarfile.open(temp_file, 'r:bz2') as tar_ref:
            tar_ref.extractall(temp_dir)
    else:
        raise ValueError(f"Unsupported archive format: {filename}")

    repo_url = f"file://{temp_dir}"
    return repo_url
import requests
import tarfile
from pathlib import Path

def get_repo_archive(url: str, destination_path: Path) -> Path:
    """
    Given an url and a destination path, retrieve and extract .tar.gz archive which contains 'desc' file for each package

    Args:
        url: url of the .tar.gz archive to download
        destination_path: the path on disk where to extract archive
    Returns:
            path where the archive is extracted to
    """
    # Download the archive
    response = requests.get(url)
    response.raise_for_status()

    # Create the destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)

    # Extract the archive to the destination directory
    with tarfile.open(fileobj=response.raw, mode='r:gz') as tar:
        tar.extractall(path=destination_path)

    return destination_path
import requests
from pathlib import Path
from tarfile import open as tar_open

def get_repo_archive(url: str, destination_path: Path) -> Path:
    response = requests.get(url)
    archive_path = destination_path / 'repo.tar.gz'
    with open(archive_path, 'wb') as f:
        f.write(response.content)

    archive_path.extractall(destination_path)
    return destination_path
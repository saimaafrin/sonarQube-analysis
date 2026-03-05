import requests
from pathlib import Path
import tarfile

def get_repo_archive(url: str, destination_path: Path) -> Path:
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination_path / "repo.tar.gz", "wb") as f:
            f.write(response.content)
        with tarfile.open(destination_path / "repo.tar.gz", "r:gz") as tar:
            tar.extractall(path=destination_path)
        return destination_path
    else:
        raise Exception(f"Failed to download archive from {url}")
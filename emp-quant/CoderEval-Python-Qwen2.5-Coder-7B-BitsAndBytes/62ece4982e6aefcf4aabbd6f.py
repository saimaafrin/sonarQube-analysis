import requests
from pathlib import Path
import tarfile

def get_repo_archive(url: str, destination_path: Path) -> Path:
    # Download the .tar.gz file from the given URL
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to download {url}")

    # Create the destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)

    # Define the path to save the downloaded file
    archive_path = destination_path / "repo.tar.gz"

    # Save the downloaded content to the file
    with open(archive_path, "wb") as f:
        f.write(response.content)

    # Extract the contents of the .tar.gz file to the destination directory
    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(path=destination_path)

    # Remove the downloaded .tar.gz file
    archive_path.unlink()

    return destination_path
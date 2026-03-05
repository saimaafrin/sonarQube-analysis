import requests
from pathlib import Path
import tarfile

def get_repo_archive(url: str, destination_path: Path) -> Path:
    # Download the .tar.gz file
    response = requests.get(url)
    response.raise_for_status()

    # Create the destination directory if it doesn't exist
    destination_path.mkdir(parents=True, exist_ok=True)

    # Save the downloaded file to a temporary location
    temp_file_path = destination_path / "repo_archive.tar.gz"
    with open(temp_file_path, "wb") as file:
        file.write(response.content)

    # Extract the .tar.gz file
    with tarfile.open(temp_file_path, "r:gz") as tar:
        tar.extractall(path=destination_path)

    # Remove the temporary file
    temp_file_path.unlink()

    return destination_path
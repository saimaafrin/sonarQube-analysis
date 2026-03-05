def get_repo_archive(url: str, destination_path: Path) -> Path:
	"""
	Given an url and a destination path, retrieve and extract .tar.gz archive which contains 'desc' file for each package

        Args:
            url: url of the .tar.gz archive to download
            destination_path: the path on disk where to extract archive
        Returns:
                path where the archive is extracted to
	"""
	archive_path = destination_path / "archive.tar.gz"
	if not archive_path.exists():
		print(f"Downloading archive from {url} to {archive_path}")
		urllib.request.urlretrieve(url, archive_path)
	print(f"Extracting archive to {destination_path}")
	tarfile.open(archive_path, "r:gz").extractall(destination_path)
	return destination_path
def get_repo_archive(url: str, destination_path: Path) -> Path:
# Download the tar.gz file from the given URL
	tar_gz_file = download_file(url, destination_path)

	# Extract the contents of the tar.gz file to the specified destination path
	extracted_dir = extract_tar_gz(tar_gz_file, destination_path)

	return extracted_dir
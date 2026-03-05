def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
    """
    if not isinstance(fixity, dict):
        self.error("Fixity block must be a dictionary")
        return False

    for file_id, file_info in fixity.items():
        if not isinstance(file_info, dict):
            self.error(f"File info for {file_id} must be a dictionary")
            return False

        if 'checksum' not in file_info:
            self.error(f"Checksum missing for file {file_id}")
            return False

        if 'algorithm' not in file_info:
            self.error(f"Checksum algorithm missing for file {file_id}")
            return False

        if file_id not in manifest_files:
            self.error(f"File {file_id} referenced in fixity but not in manifest")
            return False

    for file_id in manifest_files:
        if file_id not in fixity:
            self.error(f"File {file_id} in manifest but not referenced in fixity")
            return False

    return True
def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
    """
    if not isinstance(fixity, dict):
        self.error("Fixity block must be a dictionary")
        return False

    if 'files' not in fixity:
        self.error("Fixity block must contain a 'files' key")
        return False

    if not isinstance(fixity['files'], list):
        self.error("Fixity block 'files' key must be a list")
        return False

    for file_info in fixity['files']:
        if not isinstance(file_info, dict):
            self.error("Each file in fixity block must be a dictionary")
            return False

        if 'filename' not in file_info:
            self.error("Each file in fixity block must contain a 'filename' key")
            return False

        if file_info['filename'] not in manifest_files:
            self.error(f"File {file_info['filename']} referenced in fixity block is not in the manifest")
            return False

    return True
def validate_fixity(self, fixity, manifest_files):
    if not isinstance(fixity, dict):
        self.error("Fixity block must be a dictionary")
        return False

    for file_info in fixity.values():
        if not isinstance(file_info, dict):
            self.error("Each file info entry must be a dictionary")
            return False
        if 'file_name' not in file_info or 'checksum' not in file_info:
            self.error("Each file info entry must contain 'file_name' and 'checksum'")
            return False
        if file_info['file_name'] not in manifest_files:
            self.error(f"File {file_info['file_name']} is not listed in the manifest")
            return False

    return True
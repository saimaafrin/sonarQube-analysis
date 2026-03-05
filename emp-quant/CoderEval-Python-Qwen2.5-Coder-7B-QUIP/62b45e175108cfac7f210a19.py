def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
    """
    # Check if fixity block is a dictionary
    if not isinstance(fixity, dict):
        return self.error("Fixity block is not a dictionary")
    
    # Check if fixity block contains 'files' key
    if 'files' not in fixity:
        return self.error("Fixity block does not contain 'files' key")
    
    # Check if 'files' key contains a list
    if not isinstance(fixity['files'], list):
        return self.error("Fixity block 'files' key is not a list")
    
    # Check if all files in the fixity block are in the manifest
    for file in fixity['files']:
        if file not in manifest_files:
            return self.error(f"File {file} in fixity block is not in the manifest")
    
    return None
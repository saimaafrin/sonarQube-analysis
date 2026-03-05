def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
    """
    if not isinstance(fixity, dict) or 'files' not in fixity:
        self.error("Fixity block must be a dictionary with a 'files' key.")
    
    for file_info in fixity['files']:
        if not isinstance(file_info, dict) or 'filename' not in file_info or 'checksum' not in file_info:
            self.error("Each file info must be a dictionary with 'filename' and 'checksum' keys.")
        
        filename = file_info['filename']
        if filename not in manifest_files:
            self.error(f"File '{filename}' is referenced in fixity but not found in the manifest.")
    
    return True
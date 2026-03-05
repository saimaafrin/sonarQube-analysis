def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used. Return error() in the class.
    """
    for manifest_file in manifest_files:
        if manifest_file in digests_used:
            digests_used.remove(manifest_file)
        else:
            return self.error(f"Digest for {manifest_file} is missing")
    if digests_used:
        return self.error(f"Unused digests: {digests_used}")
    return None
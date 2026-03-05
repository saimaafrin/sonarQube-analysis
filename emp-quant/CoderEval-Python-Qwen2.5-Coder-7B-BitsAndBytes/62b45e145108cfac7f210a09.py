def check_digests_present_and_used(self, manifest_files, digests_used):
    for file_path, digests in manifest_files.items():
        if not digests:
            self.error(f"No digests found for file: {file_path}")
        for digest in digests:
            if digest not in digests_used:
                self.error(f"Digest {digest} from file {file_path} is not used")
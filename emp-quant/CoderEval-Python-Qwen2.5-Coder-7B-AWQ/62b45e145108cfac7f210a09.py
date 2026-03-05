def check_digests_present_and_used(self, manifest_files, digests_used):
    for file_path, expected_digest in manifest_files.items():
        if file_path not in digests_used:
            self.error(f"Digest for {file_path} is missing from digests_used.")
        elif digests_used[file_path] != expected_digest:
            self.error(f"Digest for {file_path} does not match the expected value.")
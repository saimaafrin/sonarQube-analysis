def check_digests_present_and_used(self, manifest_files, digests_used):
    for file_path in manifest_files:
        with open(file_path, 'r') as file:
            content = file.read()
            for digest in digests_used:
                if digest not in content:
                    self.error(f"Digest {digest} is used but not present in {file_path}")
def check_digests_present_and_used(self, manifest_files, digests_used):
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            manifest_data = file.read()
            for digest in digests_used:
                if digest not in manifest_data:
                    self.error(f"Digest {digest} is not present in {manifest_file}")
                if manifest_data.count(digest) > 1:
                    self.error(f"Digest {digest} is used more than once in {manifest_file}")
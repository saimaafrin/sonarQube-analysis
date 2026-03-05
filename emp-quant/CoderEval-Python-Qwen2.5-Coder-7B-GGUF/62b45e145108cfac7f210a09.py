def check_digests_present_and_used(self, manifest_files, digests_used):
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            manifest = file.read()
            for digest in digests_used:
                if digest not in manifest:
                    self.error(f"Digest {digest} not found in manifest {manifest_file}")
                else:
                    self.error(f"Digest {digest} found in manifest {manifest_file} but not used")
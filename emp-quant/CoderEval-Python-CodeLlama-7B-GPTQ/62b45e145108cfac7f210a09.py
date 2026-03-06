def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for manifest_file in manifest_files:
		manifest = Manifest(manifest_file)
		for digest in manifest.digests:
			if digest.digest_type not in digests_used:
				self.error("Digest type %s not used in any manifest" % digest.digest_type)
			if digest.digest_type not in self.digests_present:
				self.error("Digest type %s not present in any manifest" % digest.digest_type)

			if digest.digest_type in self.digests_present and digest.digest_type not in digests_used:
				self.error("Digest type %s present but not used" % digest.digest_type)

			if digest.digest_type in digests_used and digest.digest_type not in self.digests_present:
				self.error("Digest type %s used but not present" % digest.digest_type)

			if digest.digest_type in self.digests_present and digest.digest_type in digests_used:
				if digest.digest_value not in self.digests_present[digest.digest_type]:
					self.error("Digest value %s for digest type %s not present" % (digest.digest_value, digest.digest_type))

				if digest.digest_value not in digests_used[digest.digest_type]:
					self.error("Digest value %s for digest type %s not used" % (digest.digest_value, digest.digest_type))

				if digest.digest_value in self.digests_present[digest.digest_type] and digest.digest_value not in digests_used[digest.digest_type]:
					self.error("Digest value %s for digest type %s present but not used
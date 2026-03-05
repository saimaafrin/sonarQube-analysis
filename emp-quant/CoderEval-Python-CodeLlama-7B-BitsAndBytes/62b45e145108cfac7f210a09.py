def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for manifest_file in manifest_files:
		for digest in manifest_file.digests:
			if digest.digest_type not in digests_used:
				self.error("Digest type %s not used in manifest" % digest.digest_type)
				return
			if digest.digest_type not in digests_used[digest.digest_type]:
				self.error("Digest type %s not used in manifest" % digest.digest_type)
				return
			if digest.digest_value not in digests_used[digest.digest_type][digest.digest_type]:
				self.error("Digest value %s not used in manifest" % digest.digest_value)
				return
def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for manifest_file in manifest_files:
		with open(manifest_file, 'r') as f:
			manifest = json.load(f)
			for digest in manifest['digests']:
				if digest not in digests_used:
					self.error("Digest %s in manifest %s not used" % (digest, manifest_file))
					return
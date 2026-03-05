def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for manifest_file in manifest_files:
		with open(manifest_file, 'r') as f:
			manifest = json.load(f)
			for layer in manifest['layers']:
				digest = layer['digest']
				if digest not in digests_used:
					self.error("Digest %s is not used in any layer" % digest)
					return
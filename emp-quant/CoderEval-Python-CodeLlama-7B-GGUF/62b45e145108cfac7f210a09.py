def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for manifest_file in manifest_files:
		with open(manifest_file, 'r') as f:
			manifest = json.load(f)
			for digest in manifest['digests']:
				if digest not in digests_used:
					self.error("Digest %s is present in manifest %s but not used" % (digest, manifest_file))

			for digest in digests_used:
				if digest not in manifest['digests']:
					self.error("Digest %s is used in %s but not present in manifest %s" % (digest, digests_used[digest], manifest_file))

			for digest in manifest['digests']:
				if digest not in digests_used:
					self.error("Digest %s is present in manifest %s but not used" % (digest, manifest_file))

			for digest in digests_used:
				if digest not in manifest['digests']:
					self.error("Digest %s is used in %s but not present in manifest %s" % (digest, digests_used[digest], manifest_file))

			for digest in manifest['digests']:
				if digest not in digests_used:
					self.error("Digest %s is present in manifest %s but not used" % (digest, manifest_file))

			for digest in digests_used:
				if digest not in manifest['digests']:
					self.error("Digest %s is used in %s but not present in manifest %s" % (digest, digests_used[digest], manifest_file))

			for digest in manifest['digests']:
				if digest not in digests_used:
					self.error("Digest %s is present in manifest %s but not used" % (digest, manifest_file))
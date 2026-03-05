def add_asset(self, basename, file_path):
# Check if basename already exists in _assets
	if basename in self._assets:
		print(f"Asset '{basename}' already exists. Overwriting...")
	
	# Assign the file path to the basename in _assets
	self._assets[basename] = file_path
	
	# Print confirmation message
	print(f"Asset '{basename}' added successfully.")
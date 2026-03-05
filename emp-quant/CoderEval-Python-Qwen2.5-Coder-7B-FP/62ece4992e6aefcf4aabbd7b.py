def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
# Check if the file already exists and overwrite is False
	if os.path.exists(config_filename) and not overwrite:
		print(f"File {config_filename} already exists. Aborting.")
		return

	# Open the file in write mode with specified permissions
	with open(config_filename, 'w', mode=mode) as f:
		# Write the rendered configuration to the file
		f.write(rendered_config)
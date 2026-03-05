def list_of_file_names(settings_dirs, spec_option):
# Create the complex type
	file_names = cli.ListOfFileNames()

	# Set the settings directories
	file_names.settings_dirs = settings_dirs

	# Set the specification option
	file_names.spec_option = spec_option

	return file_names
```
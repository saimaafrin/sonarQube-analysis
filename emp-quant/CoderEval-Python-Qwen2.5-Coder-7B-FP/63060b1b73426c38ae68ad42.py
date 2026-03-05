def inject_config(self):
# Check if 'ANSIBLE_CONFIG' is already set in environment variables
	if 'ANSIBLE_CONFIG' not in os.environ:
		# Set 'ANSIBLE_CONFIG' to the path of the ansible configuration file
		os.environ['ANSIBLE_CONFIG'] = self.ansible_config_path
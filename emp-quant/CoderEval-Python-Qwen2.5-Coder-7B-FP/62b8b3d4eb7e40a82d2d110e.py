def _c_optimizations_ignored():
# Check if the environment variable 'PURE_PYTHON' is set to a non-empty string that is not '0'
	return os.environ.get('PURE_PYTHON', '').lower() != '0'
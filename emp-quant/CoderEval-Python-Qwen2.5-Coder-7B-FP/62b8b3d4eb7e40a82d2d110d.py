def _c_optimizations_required():
# Check if the environment variable is set to 'true'
	return os.getenv('C_OPTIMIZATIONS_REQUIRED', 'false').lower() == 'true'

if _c_optimizations_required():
	print("C Optimizations Required")
else:
	print("No C Optimizations Required")
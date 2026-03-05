def is_run_el(obj):
# Check if 'run' attribute exists in the object's class
	return hasattr(obj, 'run') and callable(getattr(obj, 'run'))
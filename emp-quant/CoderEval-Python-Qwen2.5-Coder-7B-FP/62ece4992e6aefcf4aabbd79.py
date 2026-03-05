def make_find_paths(find_paths):
# Import required module
	import fnmatch

	# Transform each path in the sequence to a glob pattern if it's not already one
	transformed_paths = tuple(fnmatch.translate(path) if '*' in path or '?' in path else path for path in find_paths)

	return transformed_paths
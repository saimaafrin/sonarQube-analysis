def _resolve_string(matcher):
# Get the name of the environment variable from the matcher
	name = matcher.group('name')
	# Check if there's a default value provided in the matcher
	default = matcher.group('default')
	if default:
		# Return the value from environment or the default value
		return os.getenv(name, default)
	else:
		# Raise an error if the environment variable is not set and no default is provided
		return os.getenv(name, f"Environment variable '{name}' is not set and no default value was provided.")
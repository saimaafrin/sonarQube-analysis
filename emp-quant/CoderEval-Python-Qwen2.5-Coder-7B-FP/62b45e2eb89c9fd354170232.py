def next_version(version):
# Split the version into its components
	components = list(map(int, version.split('.')))
	
	# Traverse the components from right to left
	for i in range(len(components) - 1, -1, -1):
		# If the current component is less than 9, increment it and return the new version
		if components[i] < 9:
			components[i] += 1
			return '.'.join(map(str, components))
		# If the current component is 9, set it to 0 and continue to the next component
	
	# If all components are 9, append a new component with value 1
	components.append(1)
	return '.'.join(map(str, components))
def plus_or_dot(pieces):
# Find the closest tag
	closest_tag = pieces[-1]
	
	# Check if the closest tag contains "+"
	if "+" in closest_tag:
		return "."
	else:
		return "+"
def unquote(name):
# import re module for regular expressions
	import re

	# use sub() function to replace all occurrences of '""' or "''" with ''
	name = re.sub(r'"|"\'', '', name)

	return name
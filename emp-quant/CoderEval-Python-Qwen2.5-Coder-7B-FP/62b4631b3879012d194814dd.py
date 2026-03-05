def fix_namespace_prefix_w(content):
# Replace occurrences of "w:st=" with "w-st="
	content = content.replace("w:st=", "w-st=")
	return content
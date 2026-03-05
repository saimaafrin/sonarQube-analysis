def match(filename):
# Check if the file extension is '.dox' or '.Doxyfile'
	return filename.lower().endswith('.dox') or filename.lower() == 'doxyfile'
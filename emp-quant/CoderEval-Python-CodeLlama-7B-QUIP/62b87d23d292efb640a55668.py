def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.version_file_template = """
# Do not modify this file!
# This file is set to PYVersioneer on import and flushed to disk by that module.
# If you need a different config, import pyv.VersioneerConfig and make a new one.
"""
	config.version_file_comment = """
# Do not modify this file!
# This file is set to PYVersioneer on import and flushed to disk by that module.
# If you need a different config, import pyv.VersioneerConfig and make a new one.
"""
	config.version_pattern = r"^#\s*Do\s+not\s+modify\s+this\s+file!\s*\n#\s*This\s+file\s+is\s+set\s+to\s+PYVersioneer\s+on\s+import\s+and\s+flushed\s+to\s+disk\s+by\s+that\s+module.\s*\n#\s*If\s+you\s+need\s+a\s+different\s+config,\s+import\s+pyv.VersioneerConfig\s+and\s+make\s+a\s+new\s+one.\s*\n"
	config.version_pattern_with_parent = r"^#\s*Do\s+not\s+modify\s+this\s+file!\s*\n#\s*This\s+file\s+is\s+set\s+to\s+PYVersioneer\s+on\s+import\s+and\s+flushed\s+to\s+disk\s+by\s+that\s+module.\s*\n#\s*If\s+you\s+need\s+a\s+different\s+config,\s+import\s+pyv.VersioneerConfig\s+and\s+make\s+a\s+new\s+one.\s*\n"
	config.version_pattern_with_parent_2 = r
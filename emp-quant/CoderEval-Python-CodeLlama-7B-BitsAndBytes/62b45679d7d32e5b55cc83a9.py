def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	return ' '.join(parser.parse_args([])._get_option_string_versions())
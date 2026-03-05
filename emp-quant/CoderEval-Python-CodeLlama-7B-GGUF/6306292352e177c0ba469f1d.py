def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
	"""
	Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.
	"""
	tags = set()
	in_code_block = False
	in_code_block_start = False
	in_code_block_end = False
	in_code_block_start_tag = False
	in_code_block_end_tag = False
	in_code_block_start_tag_end = False
	in_code_block_end_tag_end = False
	in_code_block_start_tag_end_end = False
	in_code_block_end_tag_end_end = False
	in_code_block_start_tag_end_end_end = False
	in_code_block_end_tag_end_end_end = False
	in_code_block_start_tag_end_end_end_end = False
	in_code_block_end_tag_end_end_end_end = False
	in_code_block_start_tag_end_end_end_end_end = False
	in_code_block_end_tag_end_end_end_end_end = False
	in_code_block_start_tag_end_end_end_end_end_end = False
	in_code_block_end_tag_end_end_end_end_end_end = False
	in_code_block_start_tag_end_end_end_end_end_end_end = False
	in_code_block_end_tag_end_end_end_end_end_end_end = False
	in_code_block_start_tag_end_end_end_end_end_end_end_end = False
	in_code_block_end_tag_end_end_end_end_end_end_end_end = False
	in_code_block_start_tag_end_end_end_end_end_end_end_end_end = False
	in_code_block_end_tag_end_end_end_end_end_end_end_end_end = False
	in_code_block_start_tag_end_end_end_end_end_end_end_end_end_end = False
	in_
def test_tag(tag: str) -> bool:
LEGAL_TAG_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~"
	return all(char not in LEGAL_TAG_CHARS for char in tag)
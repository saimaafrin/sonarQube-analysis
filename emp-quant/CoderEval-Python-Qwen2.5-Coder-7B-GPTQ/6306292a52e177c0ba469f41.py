def test_tag(tag: str) -> bool:
    """
    Checks whether each character in the LEEGAL_TAG_CHARS belongs to a tag. If any character belongs to a tag, the value False is returned. Otherwise, the value True is returned.
    """
    LEEGAL_TAG_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    return all(char in LEEGAL_TAG_CHARS for char in tag)
def test_tag(tag: str) -> bool:
    LEEGAL_TAG_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    return all(char in LEEGAL_TAG_CHARS for char in tag)
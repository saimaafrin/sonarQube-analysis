def test_tag(tag: str) -> bool:
    LEEGAL_TAG_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    for char in tag:
        if char not in LEEGAL_TAG_CHARS:
            return False
    return True
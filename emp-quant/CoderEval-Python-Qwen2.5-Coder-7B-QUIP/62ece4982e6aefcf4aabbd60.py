def size_to_bytes(size: str) -> int:
    """
    Convert human readable file size to bytes

    Args:
            size: str, a string representing a human readable file size (eg: '500K')
    Returns:
            int: file size in bytes
    """
    unit = size[-1]
    value = int(size[:-1])
    if unit == 'K':
        return value * 1024
    elif unit == 'M':
        return value * 1024 * 1024
    elif unit == 'G':
        return value * 1024 * 1024 * 1024
    elif unit == 'T':
        return value * 1024 * 1024 * 1024 * 1024
    else:
        raise ValueError("Invalid size format")
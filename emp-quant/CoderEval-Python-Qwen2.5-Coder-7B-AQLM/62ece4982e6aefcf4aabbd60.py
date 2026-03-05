def size_to_bytes(size: str) -> int:
    size = size.upper()
    if size.endswith('B'):
        return int(size[:-1])
    elif size.endswith('K'):
        return int(size[:-1]) * 1024
    elif size.endswith('M'):
        return int(size[:-1]) * 1024 * 1024
    elif size.endswith('G'):
        return int(size[:-1]) * 1024 * 1024 * 1024
    else:
        raise ValueError("Invalid size format")
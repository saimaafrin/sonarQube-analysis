import re

def size_to_bytes(size: str) -> int:
    size = size.upper()
    if size.endswith('B'):
        return int(size[:-1])
    elif size.endswith('KB'):
        return int(float(size[:-2]) * 1024)
    elif size.endswith('MB'):
        return int(float(size[:-2]) * 1024 ** 2)
    elif size.endswith('GB'):
        return int(float(size[:-2]) * 1024 ** 3)
    elif size.endswith('TB'):
        return int(float(size[:-2]) * 1024 ** 4)
    else:
        raise ValueError("Invalid size format")
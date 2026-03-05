def size_to_bytes(size: str) -> int:
    units = {'B': 1, 'K': 1024, 'M': 1024**2, 'G': 1024**3, 'T': 1024**4}
    value, unit = size[:-1], size[-1].upper()
    return int(float(value) * units[unit])
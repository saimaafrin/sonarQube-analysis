def next_version(version):
    """
    Given next version identifier following existing pattern
    """
    parts = list(map(int, version.split('.')))
    for i in range(len(parts) - 1, -1, -1):
        if parts[i] < 9:
            parts[i] += 1
            break
        parts[i] = 0
    else:
        parts.append(1)
    return '.'.join(map(str, parts))
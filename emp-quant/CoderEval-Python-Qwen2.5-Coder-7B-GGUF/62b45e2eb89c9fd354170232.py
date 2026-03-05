def next_version(version):
    parts = list(map(int, version.split('.')))
    for i in range(len(parts)-1, -1, -1):
        if parts[i] < 9:
            parts[i] += 1
            return '.'.join(map(str, parts))
        parts[i] = 0
    return '.'.join(map(str, [1] + parts))
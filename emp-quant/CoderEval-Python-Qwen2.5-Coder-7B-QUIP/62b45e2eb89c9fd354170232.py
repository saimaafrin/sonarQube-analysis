def next_version(version):
    version_parts = list(map(int, version.split('.')))
    version_parts[-1] += 1
    return '.'.join(map(str, version_parts))
import fnmatch

def make_find_paths(find_paths):
    return tuple(fnmatch.translate(path) if '*' in path or '?' in path else path for path in find_paths)
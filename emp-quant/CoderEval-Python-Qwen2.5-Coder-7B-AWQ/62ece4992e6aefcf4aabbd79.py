import fnmatch

def make_find_paths(find_paths):
    return tuple(fnmatch.translate(path) if isinstance(path, str) else path for path in find_paths)
import glob

def make_find_paths(find_paths):
    return tuple(glob.glob(path) if '*' in path else path for path in find_paths)
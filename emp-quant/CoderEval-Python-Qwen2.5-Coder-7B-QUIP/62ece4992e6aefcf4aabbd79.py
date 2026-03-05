import fnmatch

def make_find_paths(find_paths):
    """
    Given a sequence of path, transform all path into glob patterns. Pass through existing patterns untouched.

    Args:
        find_paths: sequence of path
    Returns:
        tuple of transformed path
    """
    transformed_paths = []
    for path in find_paths:
        if fnmatch.fnmatch.fnmatch(path, '*') or fnmatch.fnmatch.fnmatch(path, '**'):
            transformed_paths.append(path)
        else:
            transformed_paths.append(fnmatch.translate(path))
    return tuple(transformed_paths)
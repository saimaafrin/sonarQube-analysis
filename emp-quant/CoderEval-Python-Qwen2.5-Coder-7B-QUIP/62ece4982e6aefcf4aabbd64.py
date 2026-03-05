from pathlib import Path

def strip_root(path, root):
    """
    Remove root from path. If fails, throw exception

    Returns:
        A path without root
    """
    try:
        return path.relative_to(root)
    except ValueError:
        raise Exception(f"Failed to strip root: {root} from path: {path}")
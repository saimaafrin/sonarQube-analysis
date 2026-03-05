def get_logical_path_map(inventory, version):
    """
    Returns the file paths of the states in the inventory in the dict type.
    """
    path_map = {}
    for state in inventory:
        path_map[state] = f"path/to/state/{state}_{version}.txt"
    return path_map
def get_logical_path_map(inventory, version):
    """
    Returns the file paths of the states in the inventory in the dict type.
    """
    path_map = {}
    for state_name, state_info in inventory.items():
        if 'file' in state_info:
            path_map[state_name] = state_info['file']
    return path_map
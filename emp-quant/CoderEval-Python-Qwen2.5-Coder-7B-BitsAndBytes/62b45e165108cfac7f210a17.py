def get_logical_path_map(inventory, version):
    """
    Returns the file paths of the states in the inventory in the dict type.
    """
    logical_path_map = {}
    for state_name, state_info in inventory.items():
        if 'file_paths' in state_info:
            logical_path_map[state_name] = state_info['file_paths']
    return logical_path_map
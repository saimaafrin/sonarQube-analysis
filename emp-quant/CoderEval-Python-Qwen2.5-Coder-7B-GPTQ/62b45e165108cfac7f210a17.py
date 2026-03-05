def get_logical_path_map(inventory, version):
    """
    Returns the file paths of the states in the inventory in the dict type.
    """
    logical_path_map = {}
    for item in inventory:
        if 'states' in item and 'path' in item['states']:
            logical_path_map[item['name']] = item['states']['path']
    return logical_path_map
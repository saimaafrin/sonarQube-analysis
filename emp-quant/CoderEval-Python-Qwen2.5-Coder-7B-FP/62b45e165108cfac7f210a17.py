def get_logical_path_map(inventory, version):
# Get the logical path map from the inventory
	logical_path_map = inventory.get_logical_path_map(version)
	
	return logical_path_map
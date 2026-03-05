def _get_err_indices(self, coord_name):
# Get the index of the coordinate
	index = self._coord_names.index(coord_name)
	
	# Find all error indexes corresponding to this coordinate
	err_indexes = [i for i, name in enumerate(self._err_coord_names) if name == coord_name]
	
	return err_indexes
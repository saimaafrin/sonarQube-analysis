def _get_err_indices(self, coord_name):
	"""
	Find all error indexes corresponding to coord_name.
	"""
	err_indices = []
	for i, err in enumerate(self.errors):
		if err[0] == coord_name:
			err_indices.append(i)
	return err_indices
def _get_err_indices(self, coord_name):
    """
    Find all error indexes corresponding to coord_name.
    """
    error_indices = []
    for i, coord in enumerate(self.coords):
        if coord.name == coord_name and coord.has_errors():
            error_indices.append(i)
    return error_indices
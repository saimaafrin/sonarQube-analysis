def _get_err_indices(self, coord_name):
    """
    Find all error indexes corresponding to coord_name.
    """
    return [i for i, name in enumerate(self.coords) if name == coord_name]
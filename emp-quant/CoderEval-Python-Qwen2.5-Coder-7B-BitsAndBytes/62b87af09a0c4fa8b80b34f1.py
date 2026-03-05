if self._is_valid_coord(coord):
    bin_index = self._get_bin_index(coord)
    if bin_index is not None:
        self._hist[bin_index] += weight
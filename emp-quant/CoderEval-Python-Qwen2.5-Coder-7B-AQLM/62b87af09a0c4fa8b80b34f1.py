def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    if self._edges[0] <= coord <= self._edges[-1]:
        bin_index = int((coord - self._edges[0]) / self._bin_width)
        self._data[bin_index] += weight
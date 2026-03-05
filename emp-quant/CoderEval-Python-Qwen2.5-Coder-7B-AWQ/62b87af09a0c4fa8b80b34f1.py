if self._edges[0] <= coord < self._edges[-1]:
    bin_index = bisect.bisect_left(self._edges, coord)
    self._counts[bin_index] += weight
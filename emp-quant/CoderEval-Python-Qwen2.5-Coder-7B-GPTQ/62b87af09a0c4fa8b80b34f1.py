if self.edges[0] <= coord < self.edges[-1]:
    bin_index = bisect.bisect_left(self.edges, coord)
    self.values[bin_index - 1] += weight
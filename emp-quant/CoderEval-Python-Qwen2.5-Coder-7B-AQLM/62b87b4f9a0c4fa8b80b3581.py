def scale(self, other=None, recompute=False):
    if other is None:
        if self._scale is None or recompute:
            self._scale = self._compute_scale()
        return self._scale
    else:
        if self._scale == 0:
            raise LenaValueError("Histogram with scale equal to zero can't be rescaled.")
        self._scale = other
        self._rescale()
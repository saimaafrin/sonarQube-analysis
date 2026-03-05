def scale(self, other=None, recompute=False):
    if other is None:
        if self._scale is None or recompute:
            self._scale = self._compute_scale()
        return self._scale
    elif isinstance(other, float):
        if self._scale == 0:
            raise LenaValueError("Histogram with scale equal to zero can't be rescaled.")
        self._data = [x * (other / self._scale) for x in self._data]
        self._scale = other
    else:
        raise TypeError("Invalid type for 'other'. Expected None or float.")
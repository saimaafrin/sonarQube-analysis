def scale(self, other=None, recompute=False):
    if other is None:
        if self._scale is None or recompute:
            self._scale = sum(self._data)
        return self._scale
    elif isinstance(other, (int, float)):
        if self._scale == 0:
            raise LenaValueError("Can't rescale a histogram with scale equal to zero.")
        new_scale = other
        factor = new_scale / self._scale
        self._data = [x * factor for x in self._data]
        self._scale = new_scale
    else:
        raise TypeError("Invalid type for 'other'. Expected None or float.")
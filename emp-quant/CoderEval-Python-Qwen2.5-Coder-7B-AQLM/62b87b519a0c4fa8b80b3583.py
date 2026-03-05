def scale(self, other=None):
    if other is None:
        return self._scale
    else:
        if self._scale is None or self._scale == 0:
            raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        self._scale = other
        for field in self._fields:
            field.scale(other)
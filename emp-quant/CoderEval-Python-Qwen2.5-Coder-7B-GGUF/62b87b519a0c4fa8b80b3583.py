def scale(self, other=None):
    if other is None:
        return self._scale
    elif isinstance(other, (int, float)):
        if self._scale == 0 or self._scale is None:
            raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        self._scale = other
        for field in self.fields:
            if field.scale is not None:
                field.scale *= other / self._scale
        self._scale = other
    else:
        raise TypeError("Invalid type for scale")
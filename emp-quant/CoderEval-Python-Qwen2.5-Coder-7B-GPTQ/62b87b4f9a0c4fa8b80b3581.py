def scale(self, other=None, recompute=False):
    if other is None:
        if self.scale_computed and not recompute:
            return self._scale
        else:
            self._scale = sum(self.values())
            self.scale_computed = True
            return self._scale
    elif isinstance(other, float):
        if self._scale == 0:
            raise LenaValueError("Can't rescale histogram with scale equal to zero.")
        new_scale = other
        factor = new_scale / self._scale
        self.values()[:] = [v * factor for v in self.values()]
        self._scale = new_scale
        return new_scale
    else:
        raise TypeError("Invalid type for 'other'. Expected None or float.")
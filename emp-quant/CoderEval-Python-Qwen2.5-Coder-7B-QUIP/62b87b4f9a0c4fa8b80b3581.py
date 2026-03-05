def scale(self, other=None, recompute=False):
    if other is None:
        if self.scale is None or recompute:
            self.scale = self.compute_scale()
        return self.scale
    elif isinstance(other, float):
        if self.scale == 0:
            raise ValueError("Histograms with scale equal to zero can't be rescaled.")
        self.scale = other
        self.data *= other / self.scale
        self.scale = other
    else:
        raise ValueError("Invalid value for 'other'")

    return self.scale
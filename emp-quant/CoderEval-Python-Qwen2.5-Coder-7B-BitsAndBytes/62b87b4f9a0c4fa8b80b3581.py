import numpy as np

class Histogram:
    def __init__(self, data):
        self.data = data
        self.scale_ = None

    def scale(self, other=None, recompute=False):
        if other is None:
            if self.scale_ is None or recompute:
                self.scale_ = np.sum(self.data)
            return self.scale_
        else:
            if self.scale_ == 0:
                raise ValueError("Can't rescale histogram with scale equal to zero.")
            new_scale = other
            factor = new_scale / self.scale_
            self.data *= factor
            self.scale_ = new_scale
            return self.scale_
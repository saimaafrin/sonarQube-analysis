def scale(self, other=None, recompute=False):
	"""
	Compute or set scale (integral of the histogram).

If *other* is ``None``, return scale of this histogram.
If its scale was not computed before,
it is computed and stored for subsequent use
(unless explicitly asked to *recompute*).
Note that after changing (filling) the histogram
one must explicitly recompute the scale
if it was computed before.

If a float *other* is provided, rescale self to *other*.

Histograms with scale equal to zero can't be rescaled.
:exc:`.LenaValueError` is raised if one tries to do that.
	"""
	if other is None:
		if self._scale is None:
			self._scale = self.compute_scale()
		return self._scale
	if self._scale is None:
		raise LenaValueError("scale is not computed")
	if self._scale == 0:
		raise LenaValueError("scale is zero")
	if recompute:
		self._scale = self.compute_scale()
	self._scale = other
	return self._scale
def scale(self, other=None, recompute=False):
# BEGIN SOLUTION
	if other is None:
		return self.scale if self.scale is not None else self.compute_scale(recompute=recompute)
	elif isinstance(other, float):
		if self.scale == 0:
			raise LenaValueError("Can't rescale histogram with scale equal to zero.")
		self.scale = other
		self.data *= other / self.scale
	else:
		raise LenaTypeError("Unsupported type for 'other': {}".format(type(other)))
	# END SOLUTION
def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	return type(name, (object,), {
		'__init__': lambda self, x, y: setattr(self, 'coords', (x, y)),
		'__repr__': lambda self: 'Point(%s, %s)' % self.coords,
		'__iter__': lambda self: iter(self.coords),
		'__getitem__': lambda self, i: self.coords[i],
		'__len__': lambda self: len(self.coords),
		'__add__': lambda self, other: self.coords + other.coords,
		'__sub__': lambda self, other: self.coords - other.coords,
		'__mul__': lambda self, other: self.coords * other.coords,
		'__div__': lambda self, other: self.coords / other.coords,
		'__floordiv__': lambda self, other: self.coords // other.coords,
		'__mod__': lambda self, other: self.coords % other.coords,
		'__pow__': lambda self, other: self.coords ** other.coords,
		'__lshift__': lambda self, other: self.coords << other.coords,
		'__rshift__': lambda self, other: self.coords >> other.coords,
		'__and__': lambda self, other: self.coords & other.coords,
		'__or__': lambda self, other: self.coords | other.coords,
		'__xor__': lambda self, other: self.coords ^ other.coords,
		'__invert__': lambda self: ~self.coords,
		'__neg__': lambda self: -self.coords,
		'__pos__': lambda self: +self.coords,
		'__abs__': lambda self: abs(self.coords),
		'__round__': lambda self, n: round(self.coords, n),
		'__floor__': lambda self, n: math.floor
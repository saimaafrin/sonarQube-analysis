def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	class Point(object):
		"""
		Point Class
		"""
		def __init__(self, *args, **kwargs):
			"""
			Point Class Constructor
			"""
			if len(args) == 1 and isinstance(args[0], dict):
				for k, v in args[0].items():
					setattr(self, k, v)
			else:
				for k, v in zip(fields, args):
					setattr(self, k, v)
			for k, v in kwargs.items():
				setattr(self, k, v)
			self.srid = srid_map[name]
		def __repr__(self):
			"""
			Point Class Representation
			"""
			return "<%s: %s>" % (name, ", ".join(["%s=%s" % (k, v) for k, v in self.__dict__.items()]))
		def __str__(self):
			"""
			Point Class String Representation
			"""
			return self.__repr__()
		def __eq__(self, other):
			"""
			Point Class Equality
			"""
			return all([getattr(self, k) == getattr(other, k) for k in fields])
		def __ne__(self, other):
			"""
			Point Class Inequality
			"""
			return not self.__eq__(other)
		def __hash__(self):
			"""
			Point Class Hash
			"""
			return hash(tuple([getattr(self, k) for k in fields]))
	return Point
def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	class Point(object):
		def __init__(self, x, y):
			self.x = x
			self.y = y
			self.srid = srid_map[name]

		def __str__(self):
			return "Point({0}, {1})".format(self.x, self.y)

		def __repr__(self):
			return "Point({0}, {1})".format(self.x, self.y)

		def __eq__(self, other):
			return self.x == other.x and self.y == other.y

		def __ne__(self, other):
			return self.x != other.x or self.y != other.y

		def __hash__(self):
			return hash((self.x, self.y))

		def __getattr__(self, name):
			if name in fields:
				return getattr(self, name)
			raise AttributeError("'{0}' object has no attribute '{1}'".format(self.__class__.__name__, name))

		def __setattr__(self, name, value):
			if name in fields:
				setattr(self, name, value)
			else:
				raise AttributeError("'{0}' object has no attribute '{1}'".format(self.__class__.__name__, name))

	return Point
def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	class Point(object):
		"""
		Point Class
		"""
		def __init__(self, x, y):
			self.x = x
			self.y = y
			self.srid = srid_map[name]

		def __repr__(self):
			return "Point(%s, %s)" % (self.x, self.y)

		def __str__(self):
			return "Point(%s, %s)" % (self.x, self.y)

		def __eq__(self, other):
			return self.x == other.x and self.y == other.y

		def __ne__(self, other):
			return not self.__eq__(other)

		def __hash__(self):
			return hash((self.x, self.y))

		def __getattr__(self, name):
			if name in fields:
				return getattr(self, name)
			else:
				raise AttributeError

		def __setattr__(self, name, value):
			if name in fields:
				object.__setattr__(self, name, value)
			else:
				raise AttributeError

		def __delattr__(self, name):
			if name in fields:
				object.__delattr__(self, name)
			else:
				raise AttributeError

	return Point
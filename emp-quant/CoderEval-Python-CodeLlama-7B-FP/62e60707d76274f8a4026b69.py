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
			Point Constructor
			"""
			if len(args) == 1 and isinstance(args[0], dict):
				for field in fields:
					setattr(self, field, args[0].get(field, None))
			elif len(args) == 2:
				setattr(self, fields[0], args[0])
				setattr(self, fields[1], args[1])
			elif len(args) == 3:
				setattr(self, fields[0], args[0])
				setattr(self, fields[1], args[1])
				setattr(self, fields[2], args[2])
			else:
				raise ValueError("Invalid number of arguments")

			for field in fields:
				if field not in kwargs:
					continue
				setattr(self, field, kwargs[field])

			if hasattr(self, 'srid'):
				self.srid = srid_map.get(self.srid, self.srid)

		def __str__(self):
			"""
			Point String Representation
			"""
			return "Point({0}, {1})".format(getattr(self, fields[0]), getattr(self, fields[1]))

		def __repr__(self):
			"""
			Point Representation
			"""
			return "Point({0}, {1})".format(getattr(self, fields[0]), getattr(self, fields[1]))

		def __eq__(self, other):
			"""
			Point Equality
			"""
			if not isinstance(other, Point):
				return False
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
			if len(args) == 1:
				if isinstance(args[0], dict):
					for field in fields:
						if field in args[0]:
							setattr(self, field, args[0][field])
						else:
							setattr(self, field, None)
				else:
					for field in fields:
						setattr(self, field, args[0])
			else:
				for field in fields:
					setattr(self, field, kwargs.get(field, None))

		def __str__(self):
			"""
			Point String Representation
			"""
			return "Point(%s)" % ", ".join(map(str, [getattr(self, field) for field in fields]))

		def __repr__(self):
			"""
			Point Representation
			"""
			return "Point(%s)" % ", ".join(map(str, [getattr(self, field) for field in fields]))

		def __eq__(self, other):
			"""
			Point Equality
			"""
			if isinstance(other, Point):
				return all(getattr(self, field) == getattr(other, field) for field in fields)
			else:
				return False

		def __ne__(self, other):
			"""
			Point Inequality
			"""
			return not self.__eq__(other)

		def __hash__(self):
			"""
			Point Hash
			"""
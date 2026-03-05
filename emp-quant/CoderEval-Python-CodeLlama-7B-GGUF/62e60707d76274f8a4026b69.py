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
				for k, v in args[0].items():
					setattr(self, k, v)
			elif len(args) == 2:
				setattr(self, 'x', args[0])
				setattr(self, 'y', args[1])
			elif len(args) == 3:
				setattr(self, 'x', args[0])
				setattr(self, 'y', args[1])
				setattr(self, 'z', args[2])
			elif len(args) == 4:
				setattr(self, 'x', args[0])
				setattr(self, 'y', args[1])
				setattr(self, 'z', args[2])
				setattr(self, 'm', args[3])
			else:
				raise ValueError('Invalid number of arguments')

			for k, v in kwargs.items():
				setattr(self, k, v)

			for k, v in fields.items():
				if k not in self.__dict__:
					setattr(self, k, None)

		def __str__(self):
			"""
			Point String Representation
			"""
			return 'Point({}, {}, {}, {})'.format(self.x, self.y, self.z, self.m)

		def __repr__(self):
			"""
			Point Representation
			"""
			return 'Point({}, {}, {}, {})'.format(self.x, self.y, self.z, self
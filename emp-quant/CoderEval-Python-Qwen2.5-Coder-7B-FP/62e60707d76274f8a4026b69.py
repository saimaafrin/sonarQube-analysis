def point_type(name, fields, srid_map):
# Create a new class that inherits from the base Point class
	class Point:
		def __init__(self, *args, **kwargs):
			self.name = name
			self.fields = fields
			self.srid_map = srid_map
			for field in self.fields:
				if field in kwargs:
					setattr(self, field, kwargs[field])
				else:
					setattr(self, field, None)

		def __str__(self):
			return f"{self.name}({', '.join([f'{field}: {getattr(self, field)}' for field in self.fields])})"

		def to_dict(self):
			return {field: getattr(self, field) for field in self.fields}

		def get_srid(self):
			return self.srid_map.get(self.name, None)

	@classmethod
	def from_dict(cls, data):
		return cls(**data)

	return Point
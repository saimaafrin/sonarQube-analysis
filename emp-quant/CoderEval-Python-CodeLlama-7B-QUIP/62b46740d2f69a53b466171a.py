def pretty(self, indent=0, debug=False):
	"""
	Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
	"""
	def __init__(self, obj, indent=0, debug=False):
		"""
		Create a pretty printer.
		"""
		self.obj = obj
		self.indent = indent
		self.debug = debug
		
	def __repr__(self):
		"""
		Return a pretty formatted representation of self.
		"""
		return self.pretty()
	
	def __str__(self):
		"""
		Return a pretty formatted representation of self.
		"""
		return self.pretty()
	
	def pretty(self, indent=0, debug=False):
		"""
		Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
		"""
		obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
		return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
	
	def pretty(self, indent=0, debug=False):
		"""
		Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
		"""
		obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
		return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
	
	def pretty(self, indent=0, debug=False):
		"""
		Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent
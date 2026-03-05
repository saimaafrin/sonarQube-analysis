def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	return "." if pieces[-1].endswith("+") else "+"
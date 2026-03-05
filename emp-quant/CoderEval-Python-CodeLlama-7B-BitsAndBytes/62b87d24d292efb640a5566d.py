def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if pieces[-1].tag == "plus":
		return "."
	else:
		return "+"
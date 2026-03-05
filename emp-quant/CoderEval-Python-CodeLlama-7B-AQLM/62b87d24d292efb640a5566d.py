def plus_or_dot(pieces):
	"""
	Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".
	"""
	if pieces[-1].closet_tag == "+":
		return "."
	else:
		return "+"
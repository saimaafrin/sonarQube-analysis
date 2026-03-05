def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if style == "chess":
		return render_chess(pieces)
	elif style == "flip_chess":
		return render_flip_chess(pieces)
	elif style == "checker":
		return render_checker(pieces)
	elif style == "flip_checker":
		return render_flip_checker(pieces)
	elif style == "circle":
		return render_circle(pieces)
	elif style == "flip_circle":
		return render_flip_circle(pieces)
	elif style == "square":
		return render_square(pieces)
	elif style == "flip_square":
		return render_flip_square(pieces)
	else:
		raise ValueError("Invalid style: " + style)
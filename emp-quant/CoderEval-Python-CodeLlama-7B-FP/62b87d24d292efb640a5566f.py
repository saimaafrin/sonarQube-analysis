def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if style == "chess":
		return render_chess(pieces)
	elif style == "chess960":
		return render_chess960(pieces)
	elif style == "fischerandom":
		return render_fischerandom(pieces)
	elif style == "crazyhouse":
		return render_crazyhouse(pieces)
	elif style == "kingofthehill":
		return render_kingofthehill(pieces)
	elif style == "threecheck":
		return render_threecheck(pieces)
	elif style == "antichess":
		return render_antichess(pieces)
	elif style == "atomic":
		return render_atomic(pieces)
	elif style == "horde":
		return render_horde(pieces)
	elif style == "racingking":
		return render_racingking(pieces)
	elif style == "racingqueen":
		return render_racingqueen(pieces)
	elif style == "shatranj":
		return render_shatranj(pieces)
	elif style == "fromfile":
		return render_fromfile(pieces)
	elif style == "jump":
		return render_jump(pieces)
	elif style == "flip":
		return render_flip(pieces)
	elif style == "flip2":
		return render_flip2(pieces)
	elif style == "flip3":
		return render_flip3(pieces)
	elif style == "flip4":
		return render_flip4(pieces)
	elif style == "flip5":
		return render_flip5(pieces)
	elif style == "flip6":
		return render_flip6(pieces)
	elif style == "flip7":
		return render_flip7(pieces)
	elif style == "flip8":
		return render_flip8(pieces)
	elif style == "flip9":